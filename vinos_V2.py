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


		

		
	
	


