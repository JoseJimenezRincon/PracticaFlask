#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

from flask import Flask, Api, Resource
import json

app = Flask(__name__)
api = Api(app)

class Client(Resource):
	
	def newClient(self):
		pass

	def deleteClient(self):
		pass

	def updateClient(self, id):
		pass

	def getClientDetails(self, id):
		pass

	def getClients(self, id):
		pass
	
	def addCart(self):
		pass

	def deleteCart(self):
		pass

class Cart(Resource):
	
	def addItem(self):
		pass
	
	def delItem(self):
		pass

	def updateItem(self):
		pass

	def getItems(self):
		pass

class Wines(Resource):
	
	def getWineProperties(self):
		pass

	def addWine(self):
		pass

	def updateWine(self):
		pass

	def deleteWine(self):
		pass

	def wineByType(self):
		pass

	def allWines(self):
		pass

	def deleteWines(self):
		pass


#Registra la ruta con el framework, utilizando el endpoint asignado.
api.add_resource(Client, '/clients/<int:id>', endpoint 'client')
api.add_resource(Cart, '/cart', endpoint 'cart')
api.add_resource(Wines, '/wines/<int:id>', endpoint 'wines')


