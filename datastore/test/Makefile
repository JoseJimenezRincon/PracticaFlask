#!/usr/bin/make -f
#-*- mode:makefile -*-

newClient:
	curl -X POST -H "Content-Type: application/Json" -d '{"email":"Jose", "pass":"ajdfksd", "address":"hola", "phone":"4904399043"}'  https://natural-bus-135323.appspot.com/clients > client1.json

getAll:
	curl -X GET -H "Content-Type: application/Json" https://natural-bus-135323.appspot.com/clients

deleteClient:
	#
	#	
	#No sé ejecutar la orden desde el makefile, le dejo las intrucciones aqui.
	#
	#
	#curl -X DELETE https://natural-bus-135323.appspot.com/clients/
	#Añadimos al final de la sentencia de arriba el id del cliente (newClient) 'Created': "ID_CLIENTE"
	#Así se borrará el cliente.

