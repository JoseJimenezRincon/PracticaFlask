#!/usr/bin/make -f
#-*- mode:makefile -*-

newClient:
	curl -X POST -H "Content-Type: application/Json" -d '{"email":"Jose", "pass":"ajdfksd", "address":"hola", "phone":"4904399043"}'  https://natural-bus-135323.appspot.com/clients > client1.json

getAll:
	curl -X GET -H "Content-Type: application/Json" https://natural-bus-135323.appspot.com/clients

deleteClient:
	cat client1.json	
	#No sé ejecutar la orden desde el makefile, le dejo las intrucciones aqui.
	#
	#curl -X DELETE https://natural-bus-135323.appspot.com/clients/ID_CLIENTE
	#
	#Añadimos al final de la sentencia curl de arriba el id del cliente (newClient) 'Created': "ID_CLIENTE"
	#
	
updateClient:
	#Introduzca el ID_Cliente al final del enlace.
	#
	#curl -X PUT -H "Content-Type: application/Json" -d '{"email":"akan", "pass":"ole", "address":"adios", "phone":"4904"}'  https://natural-bus-135323.appspot.com/clients/

getClientDetails:
	#Introduzca el ID_Cliente al final del enlace:
	#curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/
	#
	#Aqui le muestro un ejemplo de la peticion:
	curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAuqiOCgw

addCart:
	#Introduzca el id del cliente donde pone ID_CLIENTE:
	#curl -X POST -H "Content-Type: application/Json" -d '{"name":"Jerez"}'  https://natural-bus-135323.appspot.com/clients/ID_CLIENTE/carts
	#
	#Un Ejemplo sería el siguiente:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Blanco"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAuqiOCgw/carts

deleteCart:
	#Introduzca el id del cliente donde pone ID_CLIENTE y el id de la carta donde pone ID_CARTA:
	#curl -X DELETE https://natural-bus-135323.appspot.com/clients/ID_CLIENTE/carts/ID_CARTA
	#
	#Un ejemplo es el siguiente:
	curl -X DELETE https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAuqiOCgw/carts/

addItem:
	#Introduzca el id del cliente donde pone ID_CLIENTE y el id de la carta donde pone ID_CARTA:
	#curl -X POST -H "Content-Type: application/Json" -d '{"name":"Rioja"}'  https://natural-bus-135323.appspot.com/clients/ID_CLIENTE/carts/ID_CARTA/items
	#
	#Un ejemplo sería el siguiente:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Yugo"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAuqiOCgw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAuqiOCgwLEgVDYXJ0cxiAgICAgLmECgw/items

getItems:
	#Introduzca el id del cliente donde pone ID_CLIENTE y el id de la carta donde pone ID_CARTA:
	#curl -X GET -H "Content-Type: application/Json" -d '{"name":"Rioja"}'  https://natural-bus-135323.appspot.com/clients/ID_CLIENTE/carts/ID_CARTA/items
	#
	#Un ejemplo sería el siguiente:
	curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAuqiOCgw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAuqiOCgwLEgVDYXJ0cxiAgICAgLmECgw/items

delItem:
	#Introduzca el id del cliente donde pone ID_CLIENTE, el id de la carta donde pone ID_CARTA y el id del item donde pone ID_ITEM:
	#curl -X DELETE -H "Content-Type: application/Json" -d '{"name":"Rioja"}'  https://natural-bus-135323.appspot.com/clients/ID_CLIENTE/carts/ID_CARTA/items/ID_ITEM
	#
	#Un ejemplo sería el siguiente:
	curl -X DELETE -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAuqiOCgw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAuqiOCgwLEgVDYXJ0cxiAgICAgLmECgw/items/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3I4CxIHQ2xpZW50cxiAgICAuqiOCgwLEgVDYXJ0cxiAgICAgLmECgwLEgVJdGVtcxiAgICAgNeMCgw

updateItem:
	#Introduzca el id del cliente donde pone ID_CLIENTE, el id de la carta donde pone ID_CARTA y el id del item donde pone ID_ITEM:
	#curl -X UPDATE -H "Content-Type: application/Json" -d '{"name":"Rioja"}'  https://natural-bus-135323.appspot.com/clients/ID_CLIENTE/carts/ID_CARTA/items/ID_ITEM
	#
	#Un ejemplo sería el siguiente:
	curl -X PUT -H "Content-Type: application/Json" -d '{"name":"esperanza"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAuqiOCgw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAuqiOCgwLEgVDYXJ0cxiAgICAgLmECgw/items/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3I4CxIHQ2xpZW50cxiAgICAuqiOCgwLEgVDYXJ0cxiAgICAgLmECgwLEgVJdGVtcxiAgICAwPqTCgw

getWineByName:
	curl -X GET 'https://natural-bus-135323.appspot.com/wines?name=vinoBlanco'
	
getWineByType:
	curl -X GET 'https://natural-bus-135323.appspot.com/wines?type=Blanco'

getWineBetweenPrices:
	curl -X GET 'https://natural-bus-135323.appspot.com/wines?min=10&max=100'

addWine:
	#curl -X POST -H "Content-Type: application/Json" -d '{"name":"vinoRosado", "type":"Rosado", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":100, "photo":"Gepeto" }'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"vinoTintoPrueba", "type":"Tinto", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":100, "photo":"Gepeto", "cask":"hola", "bottle":"botella"}'  https://natural-bus-135323.appspot.com/wines

deleteWines:
	curl -X DELETE -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/wines


allWines:
	curl -X GET -H "Content-Type: application/Json" https://natural-bus-135323.appspot.com/wines

getWineProperties:
	curl -X GET -H "Content-Type: application/Json" https://natural-bus-135323.appspot.com/wines/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ISCxIFV2luZXMYgICAgJnOlAsM

updateWine:
	curl -X PUT -H "Content-Type: application/Json" -d '{"name":"vinoUpdated", "varietals":"ole", "cask":"adios"}'  https://natural-bus-135323.appspot.com/wines/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ISCxIFV2luZXMYgICAgPiWlQkM	

deleteWine:
	curl -X DELETE -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/wines/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ISCxIFV2luZXMYgICAgPiWlQkM
