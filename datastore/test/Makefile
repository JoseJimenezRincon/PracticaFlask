#!/usr/bin/make -f
#-*- mode:makefile -*-

all: newClient getAll deleteClient updateClient getClientDetails addCart deleteCart addItem getItems delItem updateItem addWine allWines getWineProperties updateWine deleteWine getWineByName getWineByType getWineBetweenPrices deleteWines

newClient:
	curl -X POST -H "Content-Type: application/Json" -d '{"email":"email@gmail.com", "pass":"ajdfksd", "address":"calle", "phone":"66666666"}'  https://natural-bus-135323.appspot.com/clients
	curl -X POST -H "Content-Type: application/Json" -d '{"email":"email2@gmail.com", "pass":"ajdfksd", "address":"calle", "phone":"66666666"}'  https://natural-bus-135323.appspot.com/clients

getAll:
	curl -X GET -H "Content-Type: application/Json" https://natural-bus-135323.appspot.com/clients

deleteClients:
	curl -X DELETE https://natural-bus-135323.appspot.com/clients

deleteClient:	
	curl -X DELETE https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICA3oyQCww
	
updateClient:
	curl -X PUT -H "Content-Type: application/Json" -d '{"email":"updated@gmail", "pass":"updated", "address":"updated", "phone":"updated"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICA7a3SCgw

getClientDetails:
	curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICA7a3SCgw

addCart:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Blanco"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICA7a3SCgw/carts
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Navidad"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICA7a3SCgw/carts
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Nochevieja"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICA7a3SCgw/carts

deleteCart:
	curl -X DELETE https://natural-bus-135323.appspot.com/clients//hRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICA7a3SCgwLEgVDYXJ0cxiAgICAgOSRCgwcarts/

addItem:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Yugo"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICA7a3SCgwLEgVDYXJ0cxiAgICAgICACgw/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"DonSimon"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICA7a3SCgwLEgVDYXJ0cxiAgICAgICACgw/items

getItems:
	curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICA7a3SCgwLEgVDYXJ0cxiAgICAgICACgw/items

delItem:
	curl -X DELETE -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAmZnNCAwLEgVDYXJ0cxiAgICAgPKICgw/items/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3I4CxIHQ2xpZW50cxiAgICA7a3SCgwLEgVDYXJ0cxiAgICAgICACgwLEgVJdGVtcxiAgICAgLmECgw

updateItem:
	curl -X PUT -H "Content-Type: application/Json" -d '{"name":"Updated"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICA7a3SCgwLEgVDYXJ0cxiAgICAgICACgw/items/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3I4CxIHQ2xpZW50cxiAgICA7a3SCgwLEgVDYXJ0cxiAgICAgICACgwLEgVJdGVtcxiAgICAgK6ZCgw

addWine:	
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"VinoBlanco2", "type":"Blanco", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":3, "photo":"Gepeto" }'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"vinoBlanco", "type":"Blanco", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":123, "photo":"Gepeto" }'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"vinoTinto", "type":"Tinto", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":100, "photo":"Gepeto", "cask":"hola", "bottle":"botella"}'  https://natural-bus-135323.appspot.com/wines

deleteWines:
	curl -X DELETE -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/wines

allWines:
	curl -X GET -H "Content-Type: application/Json" https://natural-bus-135323.appspot.com/wines

getWineProperties:
	curl -X GET -H "Content-Type: application/Json" https://natural-bus-135323.appspot.com/wines/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ISCxIFV2luZXMYgICAgNrjxggM

updateWine:
	curl -X PUT -H "Content-Type: application/Json" -d '{"name":"vinoUpdated", "varietals":"ole", "cask":"adios"}'  https://natural-bus-135323.appspot.com/wines/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ISCxIFV2luZXMYgICAgNrjxggM	

deleteWine:
	curl -X DELETE -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/wines/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ISCxIFV2luZXMYgICAwMiqhAsM

getWineByName:
	curl -X GET 'https://natural-bus-135323.appspot.com/wines?name=vinoBlanco'
	
getWineByType:
	curl -X GET 'https://natural-bus-135323.appspot.com/wines?type=Blanco'

getWineBetweenPrices:
	curl -X GET 'https://natural-bus-135323.appspot.com/wines?min=10&max=100'

