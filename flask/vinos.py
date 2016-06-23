#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

#JoseJimenezRincon

#JULIAN, ESTA ES LA ESTRUCTURA DEL PROGRAMA. NO INTENTE COMPILARLA, YA QUE NO FUNCIONARÁ.
#ESTA ES LA ESTRUCTURA QUE TENGO PENSADA PARA CADA METODO.

from flask import Flask, Api, Resource, make_response, jsonify
import json

app = Flask(__name__)
api = Api(app)

client_information = {
	'email': email, # ID del cliente
	'pass': passw,
	'carts': carts,
	'address': address,
	'phone': phone
}

cart_information = {
	'cart_id': cart_id,
	'name': string, #(Opcional)
	'items': []
}

wines_information = {
	'wine_id': automatic,
	'grade': float, #(Opcional, 12 por defecto)
	'size': int,  #(Opcional, 75 por defecto)
	'varietals': [],
	'do': bool, # Denominacion de Origen La Mancha (False por defecto)
	'price': float, #(Opcional)
	'name': string,
	'photo':path
	'cask': int #Envejecimiento en barrica ATRIBUTOS ADICIONALES
	'bottle':int #Envejecimiento en botella ATRIBUTOS ADICIONALES
}

class Client(Resource):

	clients = []
	carts = []
	wines = []
	
	def newClient():
		if not request.json or not 'email' in request.json or not 'pass' in request.json:
			abort(400)

		email = request.json['email']
		passw = request.json['pass']
		carts = request.json['carts']
		address = request.json['address']
		phone = request.json['phone']

		clients.append({'email':email, 'passw':passw, 'carts':carts, 'address':address, 'phone':phone})
		
		return make_response(jsonify({"created:"email}), 201)

	def deleteClient():
		client = filter(lambda a: a['email'] == email, clients)
		if len(client) == 0:
			abort(400)
		clients.remove(client[0])
		return make_response(jsonify({"deleted:"email}), 200)

	def updateClient():
		client = filter(lambda a: a['email'] == email, clients)
		if len(client) == 0:
			abort(404)
		client[0]['email'] = request.json.get('email', client[0]['email']
		client[0]['passw'] = request.json.get('passw', client[0]['passw']
		client[0]['carts'] = request.json.get('carts', client[0]['carts']
		client[0]['address'] = request.json.get('address', client[0]['address']
		client[0]['phone'] = request.json.get('phone', client[0]['phone']  
		return make_response(jsonify({"email":email}), 200)

	def getClientDetails(self, client_id):
		client = fliter(lambda t:t['email'] == email, clients)
		if len(client) == 0:
			abort(404)    
		return make_response(jsonify({'clients':client[0]})

	def getClients(self, clients):
		email = request.json.get('email', clients[client_id]['email'])
		for i in clients:
			make_response(jsonify({"email":email}))

	
	def addCart(self, client_id):
		if len(client_id) == 0:
			abort(404)
		cart_id = int(max(cart_information.keys()).lstrip('clients')) + 1
		cart_id = 'cart%i' % cart_id
		name = request.json['name']
		items = request.json['items']

		cart = { 'cart_id':cart_id, 'name':name, 'items':items }

		clients[client_id].append(cart)
		
		return make_response(jsonify({"Cart added":name}), 200)

	def deleteCart(self, client_id):
		client = filter(lambda a: a['cart'] == email, clients[client_id])
		if len(client_id) == 0:
			abort(404)
		
		cart = filter(lambda b:b['id'] == cart_id, client[0]['carts'])
		if len(cart) == 0:
			abort(404)
	
		client[0]['cart'].remove(cart[0])
		return make_response(jsonify({"deleted:"cart}), 200)

class Cart(Resource):
	
	def addItem(self):
		cart_id = request.json['cart_id']
		name = request.json['name']
		items = request.json['items']

		clients.append({'cart_id':cart_id,'name':name, 'items':items})
		
		return make_response(jsonify({"cart created:"name}), 201)
	
	def delItem(self):
		item = filter(lambda a: a['item'] == item, carts)
		item.remove(item[0])
		return make_response(jsonify({"deleted:"item}), 200)

	def updateItem(self):
		items = filter(lambda a: a['item'] == item, carts)
		items[0]['items'] = request.json.get('items', items[0]['item']
		return make_response(jsonify({"items":items}), 200)

	def getItems(self):
		items = request.json.get('items', clients[client_id]['items'])
		for i in items:
			make_response(jsonify({"items":items})

class Wines(Resource):
	
	def getWineProperties(self, wine_id):
		wine = filter(lambda t:t['id'] == wine_id, wines)
		if len(wine) == 0:
			abort(404) 
    
		return jsonify({'wines':wine[0]})

	def addWine(wine_id):
		wine_id = int(max(wines_information.keys()).lstrip('wines')) + 1
		wine_id = 'wine%i' % wine_id
		grade = request.json['grade']
		size = request.json['size']
		varietals = request.json['varietals']
		do = request.json['do']
		price = request.json['price']
		name = request.json['name']
		photo = request.json['photo']
		cask = request.json['cask']
		bottle = request.json['bottle']

		cart = { 'cart_id':cart_id, 'name':name, 'items':items }
		wine = { 'wine_id':wine_id, 'grade':grade, 'size':size, 'varietals':varietals, 'do':do, 'price':price, 'name':name, 'photo':photo, 'cask':cask, 'bottle':bottle}

		wines[wine_id].append(wine)
		
		return make_response(jsonify({"Wine added":name}), 201)

	def updateWine(wine_id):
		wine = filter(lambda a: a['wine_id'] == wine_id, wines)
		if len(wine) == 0:
			abort(404)
		wine[0]['grade'] = request.json.get('grade', wine[0]['grade']
		wine[0]['size'] = request.json.get('size', wine[0]['size']
		wine[0]['varietals'] = request.json.get('varietals', wine[0]['varietals']
		wine[0]['do'] = request.json.get('do', client[0]['do']
		wine[0]['price'] = request.json.get('price', client[0]['price']
		wine[0]['name'] = request.json.get('name', client[0]['name']
		wine[0]['photo'] = request.json.get('photo', client[0]['photo']
		wine[0]['cask'] = request.json.get('cask', client[0]['cask']
		wine[0]['bottle'] = request.json.get('bottle', client[0]['bottle'] 
		return make_response(jsonify({"name":name}), 200)

	def deleteWine(wine_id):
		wine = filter(lambda a: a['wine_id'] == wine_id, wines
		if len(wine) == 0:
			abort(404)
		wines.remove(wine[0])
		return make_response(jsonify({"deleted:"name}), 200)

	def wineByType(wine_type):
		selected_wines = []

		for wine in wines:
			if wine['type'] == wine_type:
				selected_wines.append(wine)

		return make_response(jsonify({"selected_wines":selected_wines}), 200)

	def allWines(self):
		wines = request.json.get('wines', clients[client_id]['wines'])
		for i in wines:
			make_response(jsonify({"wines":wines})

	def deleteWines(self):
		del wines
		return make_response(jsonify({"deleted all wines"}))


#Registra la ruta con el framework, utilizando el endpoint asignado.
api.add_resource(Client, '/clients/<int:id>', endpoint 'client')
api.add_resource(Cart, '/cart', endpoint 'cart')
api.add_resource(Wines, '/wines/<int:id>', endpoint 'wines')


