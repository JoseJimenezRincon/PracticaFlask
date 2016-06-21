#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

#JoseJimenezRincon

from flask import Flask, jsonify, abort, make_response, request, url_for
import json

app = Flask(__name__)
app.conig['DEBUG'] = True

clients = []
carts = []
wines = []

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
def manager_client():
	if request.method == 'DELETE':
		return deleteClient(email)
	elif request.method == 'PUT':
		return updateClient(email)
	elif request.method == 'GET':
		return getClientDetails(email)
	else
		abort(404)

@app.route('/clients/<path:email>/carts', methods = ['POST'])
def manager_cart_add():
	if request.method == 'POST':
		return addCart(email)
	else:
		abort(404)
@app.route('/clients/<path:email>/carts/<int:cart_id>', methods = ['DELETE'])
def manager_cart_delete():
	if request.method == 'DELETE':
		return deleteCart(email, cart_id)
	else:
		abort(404)

def newClient():
	if not request.json or not 'email' in request.json:
		abort(400)
	
	email = request.json['email']
	passw = request.json['passw']
	carts = request.json['carts']
	adress = request.json['adress']
	phone = request.json['phone']

	Clients.append({'email':email, 'passw':passw, 'carts':carts, 'address':address, 'phone':phone})
	return make_response(jsonify({"Created: "email}), 201)

def deleteClient(email):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)
	clients.remove(client[0])
	return make_response(jsonify({"deleted: "email}), 200)

def updateClient(email):
	client = filter(lambda a:a['email'] == email, clients)
	if len (client) == 0:
		abort(400)
	client[0]['email'] = request.json.get('email', client[0]['email']
        client[0]['passw'] = request.json.get('passw', client[0]['passw']
        client[0]['carts'] = request.json.get('carts', client[0]['carts']
        client[0]['address'] = request.json.get('address', client[0]['address']
        client[0]['phone'] = request.json.get('phone', client[0]['phone']
	return make_response(jsonify({'updated: 'email}), 200)

def getClientDetails(email):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)
	return make_response(jsonify({'clients':client[0]))

def getClients():
	return make_response(jsonify({'clients':clients}), 200)

def addCart(email): 
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)
	cart_id = int(max(cart_information.keys()).lstrip('clients')) + 1
	cart_id = 'cart%i' % cart_id
	name = request.json['name']
	items = request.json['items']
	clients[0]['carts'].append({'cart_id':cart_id, 'name':name, 'items':items })
	return make_response(jsonify({'Cart added': name}), 200)

def deleteCart(email, cart_id):	
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)	
	cart = filter(lambda b:b['id'] == cart_id, client[0]['carts'])
	if len(cart) == 0:
		abort(404)
	client[0]['carts'].remove(cart[0])
	return	make_response(jsonify({'deleted':cart_id}), 200)


#-----------------------------CESTA-----------------------------#

@app.route('/clients/<path:email>/carts/<int:cart_id>/items', methods = ['GET', 'POST'])
def manager_items(email, cart_id):
	if request.method == 'POST':
		return addItem(email, cart_id)
	elif request.method == 'GET':
		return getItems(email, cart_id)
	else:
		abort(404)

@app.route('/clients/<path:email>/carts/<int:cart_id>/items/<int:item_id>', methods = ['DELETE', 'PUT'])
def manager_client(email, cart_id, item_id):
	if request.method == 'DELETE':
		return delItem(email, cart_id, item_id)
	elif request.method == 'PUT':
		return updateItem(email, cart_id, item_id)
	else:
		abort(404)

def addItem(email, cart_id, wine_id):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)	
	cart = filter(lambda b:b['id'] == cart_id, client[0]['carts'])
	if len(cart) == 0:
		abort(404)
	wine = filter(lambda b:b['id'] == wine_id, wines)
	if len(wine) == 0:
		abort(404)
	cart[0]['items'].append(wine)
	return make_response(jsonify({'added':item['id']})

def delItem(email, cart_id, item_id):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)	
	cart = filter(lambda b:b['id'] == cart_id, client[0]['carts'])
	if len(cart) == 0:
		abort(404)
	item = filter(lambda b:b['id'] == item_id, cart[0]['items'])
	if len(item) == 0:
		abort(404)
	cart[0]['items'].remove(item[0])
	return make_response(jsonify({'deleted':item_id}), 200)

def updateItem(email, cart_id, item_id):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)	
	cart = filter(lambda b:b['id'] == cart_id, client[0]['carts'])
	if len(cart) == 0:
		abort(404)
	item = filter(lambda b:b['id'] == item_id, cart[0]['items'])
	if len(item) == 0:
		abort(404)
	item[0]['id'] = request.json.get('id', item[0]['id'])
	return make_response(jsonify({'updated':item_id}), 200)

def getItems(email, cart_id):
	client = filter(lambda a:a['email'] == email, clients)
	if len(client) == 0:
		abort(404)	
	cart = filter(lambda b:b['id'] == cart_id, client[0]['carts'])
	if len(cart) == 0:
		abort(404)
	return jsonify({'items':cart[0]['items']})

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
	wine = filter(lambda t:t['id'] == wine_id, wines)
	if len(wine) == 0:
		abort(404)
	return jsonify({'wines':wine[0]})

def addWine():
	if not request.json or not 'name' in request.json:
		abort(400)
	wine_id = int(max(cart_information.keys()).lstrip('clients')) + 1
	wine_id = 'wine_id%i' % wine_id
	wine_name = request.json['name']
	wine_type = request.json['type']
	wine_grade = request.json['grade']
	wine_size = request.json['size']
	wine_varietals = request.json['varietals']
	wine_do = request.json['do', False]
	wine_price = request.json['price']
	wine_photo = request.json['photo']
	if wine_type == 'Tinto':
		wine_cask = request.json['cask']
		wine_bottle = request.json['bottle']
		wine = {'wine_id':wine_id, 'grade':grade, 'size':size, 'varietals':varietals, 'do':do, 'price':price, 'name':name,
			'photo':photo, 'cask':cask, 'bottle':bottle}
	else:	
		wine = {'wine_id':wine_id, 'grade':grade, 'size':size, 'varietals':varietals, 'do':do, 'price':price, 'name':name,
			'photo':photo}
	wines.append(wine)
	return make_response(jsonify({"created":wine_id}), 201)

def updateWine(wine_id):
	wine = filter(lambda t:t['id'] == wine_id, wines)
	if len(wine) == 0:
		abort(404)
	elif not request.json:
		abort(400)
	wine[0]['id'] = request.json.get('id', wine[0]['id'])
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
	wine = filter(lambda t:t['id'] == wine_id, wines)
	if len(wine) == 0:
		abort(404)
	wines.remove(wine[0])
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
	del wines
	return make_response(jsonify({'wines':wines}), 200)		


if __name__ == '__main__':
	app.run(debug=True, port=8000)
		
	
	
	
	


		

		
	
	


