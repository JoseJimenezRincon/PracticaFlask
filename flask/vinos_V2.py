#/usr/bin/python
# -*- coding: utf-8; mode: python -*-

#JoseJimenezRincon

from flask import Flask, jsonify, abort, make_response, request, url_for
import json

app = Flask(__name__)
app.config['DEBUG'] = True

clients = []
carts = []
wines = []

@app.errorhandler(400)
def bad_request(error):
	return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not Found'}), 404)

@app.errorhandler(409)
def not_found(error):
	return make_response(jsonify({'error': 'Email already in use'}), 409)

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
@app.route('/clients/<path:email>/carts/<int:cart_id>', methods = ['DELETE'])
def manager_cart_delete(email, cart_id):
	if request.method == 'DELETE':
		return deleteCart(email, cart_id)
	else:
		abort(404)

def newClient():
	if not request.json or not 'email' in request.json or not 'pass' in request.json:
		abort(400)
	if request.json in clients:
		abort(409)	

	email = request.json['email']
	password = request.json['pass']
	carts = request.json.get('carts', [])
	address = request.json.get('address', '')
	phone = request.json.get('phone', )

	clients.append({'email':email, 'pass':password, 'carts':carts, 'address':address, 'phone':phone})
	return make_response(jsonify({"created":email}), 201)

def deleteClient(email):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)
	clientToDelete = client[0]
	clients.remove(clientToDelete)
	return make_response(jsonify({"deleted":email}), 200)

def updateClient(email):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)
	client[0]['email'] = request.json.get('email', client[0]['email'])
        client[0]['pass'] = request.json.get('pass', client[0]['pass'])
        client[0]['carts'] = request.json.get('carts', client[0]['carts'])
        client[0]['address'] = request.json.get('address', client[0]['address'])
        client[0]['phone'] = request.json.get('phone', client[0]['phone'])
	return make_response(jsonify({"updated":email}), 200)

def getClientDetails(email):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)
	client_Details = client[0]
	return make_response(jsonify({'clients':client_Details}))

def getClients():
	return make_response(jsonify({'clients':clients}), 200)

def addCart(email): 
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)
	cart_id = request.json.get('cart_id',)
	name = request.json.get('name', '')
	items = request.json.get('items', [])
	carts_client = client[0]['carts']	
	carts_client.append({'cart_id':cart_id, 'name':name, 'items':items })
	return make_response(jsonify({'created':cart_id}), 201)

def deleteCart(email, cart_id):	
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)
	carts_client = client[0]['carts']	
	cart = filter(lambda b:b['cart_id'] == cart_id, carts_client)
	if len(cart) == 0:
		abort(404)
	carts_client.remove(cart[0])
	return	make_response(jsonify({'deleted':cart_id}), 200)


#-----------------------------CESTA-----------------------------#

@app.route('/clients/<path:email>/carts/<int:cart_id>/items', methods = ['GET', 'POST'])
def manager_items(email, cart_id, item_id):
	if request.method == 'GET':
		return getItems(email, cart_id)
	elif request.method == 'POST':
		return addItem(email, cart_id, item_id)
	else:
		abort(404)

@app.route('/clients/<path:email>/carts/<int:cart_id>/items/<int:item_id>', methods = ['DELETE', 'PUT'])
def manager_item(email, cart_id, item_id):
	if request.method == 'DELETE':
		return delItem(email, cart_id, item_id)
	elif request.method == 'PUT':
		return updateItem(email, cart_id, item_id)
	else:
		abort(404)
	
def addItem(email, cart_id, item_id):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)
	carts_client = client[0]['carts']	
	cart = filter(lambda b:b['cart_id'] == cart_id, carts_client)
	if len(cart) == 0:
		abort(404)
	wine = filter(lambda b:b['wine_id'] == item_id,wines)
	if len(wine) == 0:
		abort(404)
	cart_wines = cart[0]['items']
	cart_wines.append(wine)
	return make_response(jsonify({'added':item_id}), 201)

def delItem(email, cart_id, item_id):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)	
	carts_client = client[0]['carts']	
	cart = filter(lambda b:b['cart_id'] == cart_id, carts_client)
	if len(cart) == 0:
		abort(404)
	cart_wines = cart[0]['items']
	item = filter(lambda b:b['wine_id'] == item_id, cart_wines)
	if len(item) == 0:
		abort(404)
	cart_wines.remove(item[0])
	return make_response(jsonify({'deleted':item_id}), 200)

def updateItem(email, cart_id, item_id):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)	
	carts_client = client[0]['carts']	
	cart = filter(lambda b:b['cart_id'] == cart_id, carts_client)
	if len(cart) == 0:
		abort(404)
	cart_wines = cart[0]['items']
	item = filter(lambda b:b['wine_id'] == item_id, cart_wines)
	if len(item) == 0:
		abort(404)
	item_update = item[0]['wine_id']
	item_update = request.json.get('wine_id', item_update)
	return make_response(jsonify({'updated':item_id}), 200)

def getItems(email, cart_id):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)	
	carts_client = client[0]['carts']	
	cart = filter(lambda b:b['cart_id'] == cart_id, carts_client)
	if len(cart) == 0:
		abort(404)
	cart_wines = cart[0]['items']
	return jsonify({'items':cart_wines})

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
	getwine = wine[0]
	return jsonify({'wines':getwine})

def addWine():
	if not request.json or not 'name' in request.json:
		abort(400)
	
	wine_id = request.json.get('wine_id',)
	wine_name = request.json['name']
	wine_type = request.json['type']
	wine_grade = request.json.get('grade', )
	wine_size = request.json.get('size', )
	wine_varietals = request.json.get('varietals', [])
	wine_do = request.json.get('do', )
	wine_price = request.json.get('price', )
	wine_photo = request.json.get('photo', )
	if wine_type == 'Tinto':
		wine_cask = request.json.get('cask', )
		wine_bottle = request.json.get('bottle', )
		wine = {'wine_id':wine_id, 'grade':wine_grade, 'size':wine_size, 'varietals':wine_varietals, 'do':wine_do, 'price':wine_price, 'name':wine_name,'type':wine_type,
			'photo':wine_photo, 'cask':wine_cask, 'bottle':wine_bottle}
	else:	
		wine = {'wine_id':wine_id, 'grade':wine_grade, 'size':wine_size, 'varietals':wine_varietals, 'do':wine_do, 'price':wine_price, 'name':wine_name,'type':wine_type,
			'photo':wine_photo}
	wines.append(wine)
	return make_response(jsonify({'created':wine_id}), 201)

def updateWine(wine_id):
	wine = filter(lambda t:t['wine_id'] == wine_id, wines)
	if len(wine) == 0:
		abort(404)
	elif not request.json:
		abort(400)
	wine[0]['wine_id'] = request.json.get('wine_id', wine[0]['wine_id'])
	wine[0]['grade'] = request.json.get('grade', wine[0]['grade'])
	wine[0]['size'] = request.json.get('size', wine[0]['size'])
	wine[0]['varietals'] = request.json.get('varietals', wine[0]['varietals'])
	wine[0]['do'] = request.json.get('do', wine[0]['do'])
	wine[0]['price'] = request.json.get('price', wine[0]['price'])
	wine[0]['name'] = request.json.get('name', wine[0]['name'])
	wine[0]['photo'] = request.json.get('photo', wine[0]['photo'])
	wine[0]['type'] = request.json.get('type', wine[0]['type'])
	if wine[0]['type'] == 'Tinto':
		wine[0]['cask'] = request.json.get('cask', wine[0]['cask'])
		wine[0]['bottle'] = request.json.get('bottle', wine[0]['bottle'])
	return make_response(jsonify({'updated':wine_id}), 200)
		
def deleteWine(wine_id):
	wine = filter(lambda t:t['wine_id'] == wine_id, wines)
	if len(wine) == 0:
		abort(404)
	wineToDelete = wine[0]
	wines.remove(wineToDelete)
	return make_response(jsonify({'deleted':wine_id}), 200)

def wineByType(wine_type):
	selected_wines = []
	for wine in wines:
		if wine['type'] == wine_type:
			selected_wines.append(wine)
	return make_response(jsonify({'selected_wines':selected_wines}), 200)

def allWines():
	return make_response(jsonify({'wines':wines}), 200)

def deleteWines():
	wines = []
	return make_response(jsonify({'wines':wines}), 200)		


if __name__ == '__main__':
	app.run(debug=True, port=8000)
		
	
	
	
	


		

		
	
	


