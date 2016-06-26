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
	curl -X DELETE https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAuqiOCgw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAuqiOCgwLEgVDYXJ0cxiAgICAgK6ZCgw
