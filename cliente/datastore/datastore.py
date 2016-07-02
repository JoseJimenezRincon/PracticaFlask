#/usr/bin/python
# -*- cod:ing: utf-8; mode: python -*-

#JoseJimenezRincon

from google.appengine.ext import ndb
from google.appengine.api import memcache
from flask import Flask, jsonify, abort, make_response, request, url_for
from dataTypes import Clients, Wines, Carts, Items


app = Flask(__name__)
app.config['DEBUG'] = True

@app.errorhandler(400)
def bad_request(error):
	return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not Found'}), 404)

#---------------------------------Cliente--------------------------------#

@app.route('/search', methods = ['GET'])
def manager_search():
        if request.args.get('ClientID') and request.args.get('CartID'):
                return getCartItems()
        elif request.args.get('ClientID'):
                return getClientCarts()
        else:
                abort(404)

def getClientCarts():
        if not request.args.get('ClientID'):
                abort(400)
        client_id = request.args.get('ClientID')
        client_key = ndb.Key(Clients, ClientID)
        client = client_key.get()
        carts =  client.cartsANDitems(client_key)
        return make_response(jsonify({"carts":carts}))

def getCartItems():
        if not request.args.get('ClientID') and request.args.get('CartID'):
                abort(400)
        client_id = request.args.get('ClientID')
        cart_id = request.args.get('CartID')
        client_key = ndb.Key(urlsafe=client_id)
        cart_key = ndb.Key(urlsafe=cart_id)
        ItemList = Items.query(ancestor=cart_key)
        auxJSON = Items.toJSONlist(ItemList)
        client = client_key.get()
        cart = cart_key.get()
        return make_response(jsonify({"items":auxJSON}))

@app.route('/', methods = ['GET', 'DELETE'])
def nabo():
        if request.method == 'GET':
                return make_response(jsonify({'carts':Carts.getName()}), 200)
        else:
                for cart in Carts.query():
                        cart.key.delete()
                return make_response('deleted')


@app.route('/clients', methods = ['GET', 'POST', 'DELETE'])
def manager_clients():
        if request.method == 'POST':
                return newClient()
        elif request.method == 'GET':
                return getClients()
        elif request.method == 'DELETE':
                return deleteClients()

def newClient():
        if not request.json or not 'email' in request.json or not 'pass' in request.json:
                abort(400)
        email = request.json['email']
        password = request.json['pass']
        client = Clients(
                email = email,
                password = password,
                carts = [],
                address = request.json.get('address', ),
                phone = request.json.get('phone', ),
                id = email)
        client.put()
        memcache.flush_all()
        return make_response(jsonify({'created':client.key.id()}), 201)

def getClients():
        return make_response(jsonify({'clients':Clients.getName()}), 200)

def deleteClients():
        for client in Clients.query():
                client.key.delete()
        return make_response('deleted')


@app.route('/clients/<path:client_id>', methods = ['DELETE', 'PUT', 'GET'])
def manager_client(client_id):
        if request.method == 'DELETE':
                return deleteClient(client_id)
        elif request.method == 'PUT':
                return updateClient(client_id)
	elif request.method == 'GET':
		return getClientDetails(client_id)
	else:
		abort(404)

def deleteClient(client_id):
	try:
		client_key = ndb.Key(Clients, client_id)
	except:
		abort(404)
	client_key.delete()
	memcache.delete(client_id)	
	return make_response(jsonify({"deleted":client_id}), 200)

def updateClient(client_id):
	try:
		client_key = ndb.Key(Clients, client_id)
	except:
		abort(404)
	client = client_key.get()
	client.email = request.json.get('email', client.email)
        client.password = request.json.get('pass', client.password)
        client.carts = request.json.get('carts', client.carts)
        client.address = request.json.get('address', client.address)
        client.phone = request.json.get('phone', client.phone)
	client_id = client.put()
	memcache.flush_all()
	return make_response(jsonify({'updated':client.to_dict()}), 200)

def getClientDetails(client_id):
	email = memcache.get(client_id)
	try:
		client_key = ndb.Key(Clients, client_id)
	except:
		abort(404)
	client = client_key.get()
	email = client.email
	password = client.password
	carts =	 client.queryToName(client_key)
	address = client.address
	phone = client.phone	
	return make_response(jsonify({"email":email, "pass":password, "carts":carts, "address":address, "phone":phone}))


@app.route('/clients/<path:client_id>/carts', methods = ['POST'])
def manager_cart_add(client_id):
	if request.method == 'POST':
		return addCart(client_id)
	else:
		abort(404)


def addCart(client_id):	
	if not request.json or not 'name' in request.json:
		abort(400)
	name = request.json['name']
	try:
		client_key = ndb.Key(Clients, client_id)
	except:
		abort(404)
	new_cart = Carts(
		parent = client_key,
		name = name,
		items = [])
	cart_id = new_cart.put()
	return make_response(jsonify({'created':cart_id.key.id()}), 201)


@app.route('/clients/<path:client_id>/carts/<path:cart_id>', methods = ['DELETE'])
def manager_cart_delete(client_id, cart_id):
	if request.method == 'DELETE':
		return deleteCart(client_id, cart_id)
	else:
		abort(404)


def deleteCart(client_id, cart_id):
	try:
		cart_key = ndb.Key(Carts, cart_id)
	except:
		abort(404)
	cart_key.delete()
	memcache.delete(cart_id)
	return	make_response(jsonify({'deleted':cart_id}), 200)


#-----------------------------CESTA-----------------------------#

@app.route('/clients/<path:client_id>/carts/<path:cart_id>/items', methods = ['GET', 'POST'])
def manager_items(client_id ,cart_id):
	if request.method == 'GET':
		return getItems(client_id, cart_id)
	elif request.method == 'POST':
		return addItem(client_id, cart_id)
	else:
		abort(404)


def addItem(client_id, cart_id):
	if not request.json or not 'name' in request.json:
		abort(400)
	name = request.json['name']
	try:
		cart_key = ndb.Key(Carts, cart_id)
	except:
		abort(404)
	new_item = Items(
		parent = cart_key,
		name = name
	)
	cart = cart_key.get()
	cart.items.append(name)
	item_id = new_item.put()
	return make_response(jsonify({'added':item_id.urlsafe()}), 201)

def getItems(client_id, cart_id):
	auxJSON = []
	try:
		client_key = ndb.Key(Clients, client_id)
		cart_key = ndb.Key(Carts, cart_id) #Entiendo que el cart_id es unico.
	except:
		abort(404)
	ItemList = Items.query(ancestor=cart_key)
	auxJSON = Items.toJSONlist(ItemList)
	client = client_key.get()
	return make_response(jsonify({'email_client':client.email,'items':auxJSON}), 200)


@app.route('/clients/<path:client_id>/carts/<path:cart_id>/items/<path:item_id>', methods = ['DELETE', 'PUT'])
def manager_item(client_id, cart_id, item_id):
	if request.method == 'DELETE':
		return delItem(client_id, cart_id, item_id)
	elif request.method == 'PUT':
		return updateItem(client_id, cart_id, item_id)
	else:
		abort(404)
	

def delItem(client_id, cart_id, item_id):
	try:
		item_key = ndb.Key(Items, item_id) #Entiendo que el item_id es unico.
	except:
		abort(404)
	item_key.delete()
	memcache.delete(item_id)
	return make_response(jsonify({'deleted':item_id}), 200)


def updateItem(client_id, cart_id, item_id):
	try:
		client_key = ndb.Key(Clients, client_id)
		cart_key = ndb.Key(Carts, cart_id)
		item_key = ndb.Key(Items, item_id)
	except:
		abort(404)
	item = item_key.get()	
	item.name = request.json.get('name', item.name)
	item.put()
	client = client_key.get()
	cart = cart_key.get()
	memcache.flush_all()
	return make_response(jsonify({'Client_Email':client.email, 'Cart_name':cart.name ,'updated':item.to_dict()}), 200)


#-----------------------------WINES-------------------------------#
	
@app.route('/wines', methods = ['DELETE', 'POST', 'GET'])
def manager_wines():
	
	if request.method == 'GET':
		if request.args.get('type'):
			return wineByType()
		if request.args.get('name'):
			return wineByName()
		if request.args.get('min'):
			return wineBetweenPrices()
	if request.method == 'POST':
		return addWine()
	elif request.method == 'DELETE':
		return deleteWines()
	elif request.method == 'GET':
		return allWines()
	else:
		abort(404)


def wineByType():
	if not request.args.get('type'):
		abort(400)
	wine_type = request.args.get('type')
	auxJSON = []
	winesByType = Wines.query(Wines.wine_type == wine_type)
	auxJSON = Wines.toJSONlist(winesByType)
	return make_response(jsonify({'winesbytype':auxJSON}), 200)


def wineByName():	
	if not request.args.get('name'):
		abort(400)
	name = request.args.get('name')
	auxJSON = []
	winesByName = Wines.query(Wines.name == name)
	auxJSON = Wines.toJSONlist(winesByName)
	return make_response(jsonify({'winesbyname':auxJSON}), 200)	

def wineBetweenPrices():
	if not request.args.get('min') or not request.args.get('max'):
		abort(400)
	minimum = float(request.args.get('min'))
	maximum = float(request.args.get('max'))
	auxJSON = [] 
	winesBetweenPrices = Wines.query(Wines.price >= minimum, Wines.price <= maximum)
	auxJSON = Wines.toJSONlist(winesBetweenPrices)
	return make_response(jsonify({'winesbetweenprices':auxJSON}))


def addWine():
	if not request.json or not 'name' in request.json or not 'type' in request.json:
		abort(400)
	name = request.json['name']
	wine_type = request.json['type']
	new_wine = Wines(
		name = name,
		wine_type = wine_type,
		grade = request.json.get('grade', ),	
		size = request.json.get('size', ),	
		varietals = request.json.get('varietals', ),	
		do = request.json.get('do', ),	
		price = request.json.get('price', ),
		photo = request.json.get('photo', ))
	if wine_type == 'Tinto':
		new_wine.cask = request.json.get('cask', )
		new_wine.bottle = request.json.get('bottle', )	
	wine_id = new_wine.put()
	return make_response(jsonify({'created':wine_id.urlsafe()}), 201)

def deleteWines():
	for wines in Wines.query():
		wines.key.delete()
	return make_response('deleted')

def allWines():
	return make_response(jsonify({'wines':Wines.getWinesName()}))


@app.route('/wines/<path:wine_id>', methods = ['DELETE', 'PUT', 'GET'])
def manager_wine(wine_id):	
	if request.method == 'GET':
		return getWineProperties(wine_id)
	elif request.method == 'PUT':
		return updateWine(wine_id)
	elif request.method == 'DELETE':
		return deleteWine(wine_id)
	else:
		abort(404)


def getWineProperties(wine_id):
	name = memcache.get(wine_id)	
	try:
		wine_key = ndb.Key(urlsafe=wine_id)
		wine = wine_key.get()
		name = wine.name
	except:
		abort(404)
	wine_type = wine.wine_type
	grade = wine.grade	
	size = wine.size	
	varietals = wine.varietals
	do = wine.do	
	price = wine.price
	photo = wine.photo
	if wine_type == "Tinto":	
		cask  = wine.cask
		bottle = wine.bottle
		return make_response(jsonify({'name':name, 'type':wine_type, 'grade':grade, 'size':size, 'varietals':varietals, 'do':do, 'price':price, 'photo':photo,'cask':cask, 'bottle':bottle}))
	else:
		return make_response(jsonify({'name':name, 'type':wine_type, 'grade':grade, 'size':size, 'varietals':varietals, 'do':do, 'price':price, 'photo':photo}))	

	
def updateWine(wine_id):
	try:
		wine_key = ndb.Key(urlsafe=wine_id)
	except:
		abort(404)
	wine = wine_key.get()
	wine.name = request.json.get('name', wine.name)
	wine.wine_type = request.json.get('type', wine.wine_type)
	wine.grade = request.json.get('grade', wine.grade)	
	wine.size = request.json.get('size', wine.size)	
	wine.varietals = request.json.get('varietals', wine.varietals)	
	wine.do = request.json.get('do', wine.do)	
	wine.price = request.json.get('price', wine.price)
	wine.photo = request.json.get('photo', wine.photo)
	if wine.wine_type == 'Tinto':
		wine.cask = request.json.get('cask', wine.cask)
		wine.bottle = request.json.get('bottle', wine.bottle)	
	wine.put()
	memcache.flush_all()	
	return make_response(jsonify({'updated':wine.to_dict()}), 200)

	
def deleteWine(wine_id):
	try:
		wine_key = ndb.Key(urlsafe=wine_id) #Entiendo que el wine_id es unico.
	except:
		abort(404)
	wine_key.delete()
	memcache.delete(wine_id)
	return make_response(jsonify({'deleted':wine_id}), 200)
	
	
	


		

		
	
	


