#!/usr/bin/python

from google.appengine.ext import ndb

class Clients(ndb.Model):
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	carts = ndb.KeyProperty()
	address = ndb.StringProperty()
	phone = ndb.StringProperty()

	def cart2json(self):
		return {"name":self.name}
	
	def queryToName(self):
		name_carts = []
		cart_query = Carts.query(ancestor=self.client_key)
		for cart in cart_query:
			cart.append(cart.cart2json())
		return name_carts	
	


class Carts(ndb.Model):
	name = ndb.StringProperty(required=True)
	items = ndb.KeyProperty()

	def item2json(self):
		return {"name":self.name}

	def toJSONlist(self, entriesList):
		auxJSON = []
		for item in entriesList:
			auxJSON.append(item.item2json())
		return auxJSON

class Wines(ndb.Model):
	name = ndb.StringProperty(required=True)
	wine_type = ndb.StringProperty(required=True)
	grade = ndb.FloatProperty()
	size = ndb.IntegerProperty()
	varietals = ndb.StringProperty()
	do = ndb.BooleanProperty()
	price = ndb.FloatProperty()
	photo = ndb.StringProperty()


	def wine2json(self):
		return {"name":self.name}

	
	def toJSONlist(self, entriesList):
		auxJSON = []
		for wine in entriesList:
			auxJSON.append(wine.wine2json())
		return auxJSON

class RedWines(ndb.Model):
	cask = ndb.StringProperty()
	bottle = ndb.StringProperty()

class Items(ndb.Model):
	name = ndb.StringProperty(required=True)	

	
	
