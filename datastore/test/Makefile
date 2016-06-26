#!/usr/bin/make -f
#-*- mode:makefile -*-

newClient:
	curl -X POST -H "Content-Type: application/Json" -d '{"email":"email@gmail.com", "pass":"ajdfksd", "address":"calle", "phone":"66666666"}'  https://natural-bus-135323.appspot.com/clients

getAll:
	curl -X GET -H "Content-Type: application/Json" https://natural-bus-135323.appspot.com/clients

deleteClient:	
	curl -X DELETE https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICA7a2SCww
	
updateClient:
	curl -X PUT -H "Content-Type: application/Json" -d '{"email":"updated@gmail", "pass":"updated", "address":"updated", "phone":"updated"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw

getClientDetails:
	curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw

addCart:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Blanco"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Navidad"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Nochevieja"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts

deleteCart:
	curl -X DELETE https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAmZnNCAwLEgVDYXJ0cxiAgICAgPKICgw

addItem:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Yugo"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAmZnNCAwLEgVDYXJ0cxiAgICAgPKICgw/items

getItems:
	curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAmZnNCAwLEgVDYXJ0cxiAgICAgPKICgw/items

delItem:
	curl -X DELETE -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAmZnNCAwLEgVDYXJ0cxiAgICAgPKICgw/items/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3I4CxIHQ2xpZW50cxiAgICAmZnNCAwLEgVDYXJ0cxiAgICAgPKICgwLEgVJdGVtcxiAgICAgLmECgw

updateItem:
	curl -X PUT -H "Content-Type: application/Json" -d '{"name":"Updated"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICAmZnNCAw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ImCxIHQ2xpZW50cxiAgICAmZnNCAwLEgVDYXJ0cxiAgICAgPKICgw/items/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3I4CxIHQ2xpZW50cxiAgICAmZnNCAwLEgVDYXJ0cxiAgICAgPKICgwLEgVJdGVtcxiAgICAgMOVCgw

addWine:	
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"VinoBlanco2", "type":"Blanco", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":3, "photo":"Gepeto" }'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"vinoBlanco", "type":"Blanco", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":123, "photo":"Gepeto" }'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"vinoTinto", "type":"Tinto", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":100, "photo":"Gepeto", "cask":"hola", "bottle":"botella"}'  https://natural-bus-135323.appspot.com/wines

deleteWines:
	curl -X DELETE -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/wines

allWines:
	curl -X GET -H "Content-Type: application/Json" https://natural-bus-135323.appspot.com/wines

getWineProperties:
	curl -X GET -H "Content-Type: application/Json" https://natural-bus-135323.appspot.com/wines/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ISCxIFV2luZXMYgICAgJnOlAsM

updateWine:
	curl -X PUT -H "Content-Type: application/Json" -d '{"name":"vinoUpdated", "varietals":"ole", "cask":"adios"}'  https://natural-bus-135323.appspot.com/wines/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ISCxIFV2luZXMYgICAgIDkkQoM	

deleteWine:
	curl -X DELETE -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/wines/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3ISCxIFV2luZXMYgICAgIDkkQoM

getWineByName:
	curl -X GET 'https://natural-bus-135323.appspot.com/wines?name=vinoBlanco'
	
getWineByType:
	curl -X GET 'https://natural-bus-135323.appspot.com/wines?type=Blanco'

getWineBetweenPrices:
	curl -X GET 'https://natural-bus-135323.appspot.com/wines?min=10&max=100'

