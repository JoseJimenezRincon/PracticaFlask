#/usr/bin/python
# -*- coding: utf-8; mode: python -*-

#JoseJimenezRincon

from flask import Flask, jsonify, abort, make_response, request, url_for
import json
from google.appengine.ext import ndb
from definicionEstructuras import Client, Wine, Cart, Item, RedWines

app = Flask(__name__)
app.config['DEBUG'] = True

@app.errorhandler(400)
def bad_request(error):
	return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not Found'}), 404)

#---------------------------------Cliente--------------------------------#

@app.route('/clients', methods = ['GET', 'POST'])
def manager_clients():
	if request.method == 'POST':
		return newClient()
	elif request.method == 'GET':
		return getClients()

@app.route('/clients/<path:email>', methods = ['DELETE', 'PUT', 'GET'])
def manager_client(email):
	if request.method == 'DELETE':
		return deleteClient(email)
	elif request.method == 'PUT':
		return updateClient(email)
	elif request.method == 'GET':
		return getClientDetails(email)
	else:
		abort(404)

@app.route('/clients/<path:email>/carts', methods = ['POST'])
def manager_cart_add(email):
	if request.method == 'POST':
		return addCart(email)
	else:
		abort(404)
@app.route('/clients/<path:email>/carts/<path:cart_id>', methods = ['DELETE'])
def manager_cart_delete(email, cart_id):
	if request.method == 'DELETE':
		return deleteCart(email, cart_id)
	else:
		abort(404)

def newClient():
	if not request.json or not 'email' in request.json or not 'pass' in request.json:
		abort(400)
	
	client = Client(
	email = request.json['email'],
	password = request.json['pass'],
	carts = request.json.get('carts', []),
	address = request.json.get('address', ''),
	phone = request.json.get('phone', ))

	client.put()
	
	return make_response(jsonify({'created':client.key.id()}), 201)

def deleteClient(email):
	key = ndb.Key(Client, email)
	key.delete()	
	return make_response(jsonify({"deleted":email}), 200)

def updateClient(email):
	if not request.json:
		abort(400)
		
	key = ndb.Key(Client, email)
	client = key.get()
	
	
	client.email = request.json.get('email', client.email)
        client.password = request.json.get('pass', client.password)
        client.carts = request.json.get('carts', client.carts)
        client.address = request.json.get('address', client.address)
        client.phone = request.json.get('phone', client.phone)

	client.put()
	return make_response(jsonify({'updated':client.to_dict()}), 200)

def getClientDetails(email):
	key = ndb.Key(Client, email)
	client = key.get().toJson()	
	return make_response(jsonify({'clients':client}))

def getClients():
	return make_response(jsonify({'clients':Clients.getAll()}), 200)

def addCart(email):
	key = ndb.Key(Client, email) 
	cart = Cart(
		parent = key,
		name = request.json.get("name", "")
	)
	cart.put()
	return make_response(jsonify({'created':cart.key.id()}), 201)

def deleteCart(email, cart_id):
	client_key = ndb.Key(Client, email)
	cart_key = ndb.Key(Cart,vcart_id)
	client = client_key.get()
	client.carts.remove(cart_key)
	cart_Key.delete()
	return	make_response(jsonify({'deleted':cart_id}), 200)


#-----------------------------CESTA-----------------------------#

@app.route('/clients/<path:email>/carts/<path:cart_id>/items', methods = ['GET', 'POST'])
def manager_items(email, cart_id, item_id):
	if request.method == 'GET':
		return getItems(email, cart_id)
	elif request.method == 'POST':
		return addItem(email, cart_id, item_id)
	else:
		abort(404)

@app.route('/clients/<path:email>/carts/<path:cart_id>/items/<path:item_id>', methods = ['DELETE', 'PUT'])
def manager_item(email, cart_id, item_id):
	if request.method == 'DELETE':
		return delItem(email, cart_id, item_id)
	elif request.method == 'PUT':
		return updateItem(email, cart_id, item_id)
	else:
		abort(404)
	
def addItem(email, cart_id, item_id):
	client_key = ndb.Key(Client, email)
	cart_key = ndb.Key(Cart, cart_id)
	
	item = Item(
		parent = cart_key
		item_key = item_id
	)
	
	item.put() 	

	return make_response(jsonify({'added':item_id}), 201)

def delItem(email, cart_id, item_id):
	client_key = ndb.Key(Client, email)
	cart_key = ndb.Key(Cart, cart_id)
	item_key = ndb.Key(Wine, item_id)

	client = client_key.get()
	cart = client.carts.get(cart_key)
	#cart = client.cart_key.get()
	cart.items.remove(item_key)
	item_key.delete()
	
	return make_response(jsonify({'deleted':item_id}), 200)

def updateItem(email, cart_id, item_id):
	client_key = ndb.Key(Client, email)
	cart_key = ndb.Key(Cart, cart_id)
	item_key = ndb.Key(Wine, item_id)

	item = item_key.get()
	item.item_key = request.json.get("item_key", item.item_key)
	item.put()
	return make_response(jsonify({'updated':item.toJson()}), 200)

def getItems(email, cart_id):
	client_key = ndb.Key(Client, email)
	cart_key = ndb.Key(Cart, cart_id)
	
	items = Item.query(ancestor=cart_key)
	items_json = Item.toJSONlist(items)
	return make_response(jsonify({'items':items_json}), 200)

#-----------------------------WINES-------------------------------#
	
@app.route('/wines', methods = ['DELETE', 'POST', 'GET'])
def manager_wines():
	if request.method == 'POST':
		return addWine()
	elif request.method == 'DELETE':
		return deleteWine()
	elif request.method == 'GET':
		return allWines()
	else:
		abort(404)

@app.route('/wines/<int:wine_id>', methods = ['DELETE', 'PUT', 'GET'])
def manager_wine(wine_id):
	if request.method == 'GET':
		return getWineProperties(wine_id)
	elif request.method == 'PUT':
		return updateWine(wine_id)
	elif request.method == 'DELETE':
		return deleteWine(wine_id)
	else:
		abort(404)

@app.route('/wines/<path:wine_type>', methods = ['GET'])
def manager_wine_type(wine_type):
	if request.method == 'GET':
		return wineByType(wine_type)
	else:
		abort(404)

def getWineProperties(wine_id):
	wine = filter(lambda t:t['wine_id'] == wine_id, wines)
	if len(wine) == 0:
		abort(404)
	return jsonify({'wines':wine[0]})

def addWine():
	if not request.json or not 'name' in request.json:
		abort(400)

	wine = Wine(
		wine_name = request.json['name']
		wine_type = request.json['type']
		wine_grade = request.json.get('grade', )
		wine_size = request.json.get('size', )
		wine_varietals = request.json.get('varietals', [])
		wine_do = request.json.get('do', False)
		wine_price = request.json.get('price', )
		wine_photo = request.json.get('photo', )
	)
	wine_id = wine.put()

	if wine_type == 'Tinto':
		red_wine = RedWine(
			parent = wine.key,
			wine_cask = request.json.get('cask', )
			wine_bottle = request.json.get('bottle', )
		)
		red_wine.put()

	return make_response(jsonify({'created':wine.key.id()}), 201)

def updateWine(wine_id):
	wine_key = ndb.Key(Wine, wine_id)
	wine = wine_key.get()
	
	wine.wine_name  = request.json.get('name', wine.wine_name)
	wine.wine_type = request.json.get('type', wine.wine_type)
	wine.wine_grade = request.json.get('grade', wine.wine_grade)
	wine.wine_size = request.json.get('size', wine.wine_size)
	wine.wine_varietals = request.json.get('varietals', wine.wine_varietals)
	wine.wine_do = request.json.get('do', wine.wine_do)
	wine.wine_price = request.json.get('price', wine.wine_price)
	wine.wine_photo = request.json.get('photo', wine.wine_photo)
	
	if wine.wine_type == "Tinto" and tinto is True: # ¿Tinto? Antes: SI | Después: SI
        for red_wine in RedWines.query(ancestor=wine_key):
            red_wine.cask   = request.json.get("cask",   red_wine.cask)
            red_wine.bottle = request.json.get("bottle", red_wine.bottle)
            red_wine.put()
    	elif wine.wine_type == "Tinto" and tinto is False: # ¿Tinto? Antes: NO | Después: SI
        new_red_wine = RedWines(
            parent  = wine.key,
            cask    = request.json.get("cask", 0),
            bottle  = request.json.get("bottle", 0)
        )
        new_red_wine.put()
    	elif wine.wine_type != "Tinto" and tinto is True: # ¿Tinto? Antes: SI | Después: NO
        for red_wine in RedWines.query(ancestor=wine_key):
            red_wine.key.delete()

	return make_response(jsonify({'updated':wine.toJson()}), 200)
		
def deleteWine(wine_id):
	wine_key = ndb.Key(Wine, wine_id)
	wine = wine_key.get()
	
    	if wine.wine_type == "Tinto":
        	for red_wine in RedWines.query(ancestor=wine_key):
            	red_wine.key.delete()
	wine_key.delete()
	return make_response(jsonify({'deleted':wine_id}), 200)

def wineByType(wine_type):
	selected_wines = []
	for wine in wines:
		if wine['type'] == wine_type:
			selected_wines.append(wine)
	return make_response(jsonify({'selected_wines':selected_wines}), 200)		

@app.route('/search')
def search():
    name = request.args.get('name',"", type=str)
    wine_type = request.args.get('type',"", type=str)
    low_price = request.args.get('low_price',"0.0", type=str)
    high_price = request.args.get('high_price',"99999999.9", type=str)

    if name:
        return getWineByName(name)
    elif wine_type:
        return getWineByType(wine_type)
    elif low_price or high_price:
        return getWinesBetweenPrices(low_price, high_price)
    else:
        abort(404)

def getWinesByName(name):
    wines_json = Wines.toJSONlist(
        Wines.query(Wines.name==name))
    return make_response(jsonify({"wines":wines_json}), 200)

def getWinesByType(wine_type):
    wines_json = Wines.toJSONlist(
        Wines.query(Wines.wine_type==wine_type))
    return make_response(jsonify({"wines":wines_json}), 200)

def getWinesBetweenPrices(low_price, high_price):
    wines_json = Wines.toJSONlist(
        ndb.gql("SELECT * FROM Wines " +
                "WHERE price <= "+high_price+" AND price >= "+low_price))
    return make_response(jsonify({"wines":wines_json}), 200)
		
	
	
	
	


		

		
	
	


