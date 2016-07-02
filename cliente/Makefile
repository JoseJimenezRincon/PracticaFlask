#!/usr/bin/make -f
#-*- mode:makefile -*-

newClient:
	curl -X POST -H "Content-Type: application/Json" -d '{"email":"akanthor@gmail.com", "pass":"ajdfksd", "address":"calle", "phone":"66666666"}' https://natural-bus-135323.appspot.com/clients
	curl -X POST -H "Content-Type: application/Json" -d '{"email":"monillo@gmail.com", "pass":"ajdfksd", "address":"calle", "phone":"66666666"}'  https://natural-bus-135323.appspot.com/clients


addCart:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Botellon"}' https://natural-bus-135323.appspot.com/clients/akanthor@gmail.com/carts 
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Inem"}' https://natural-bus-135323.appspot.com/clients/akanthor@gmail.com/carts
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Verano"}'  https://natural-bus-135323.appspot.com/clients/monillo@gmail.com/carts

addWine:	
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Rosa", "type":"Rosado", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":54, "photo":"Gepeto" }' https://natural-bus-135323.appspot.com/wines 
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Senorio de los Llanos", "type":"Tinto", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":12, "photo":"Gepeto" }'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Black", "type":"Tinto", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":15, "photo":"Gepeto", "cask":"hola", "bottle":"botella"}'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Yugo", "type":"Rosado", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":15, "photo":"Gepeto", "cask":"hola", "bottle":"botella"}'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Rioja", "type":"Tinto", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":15, "photo":"Gepeto", "cask":"hola", "bottle":"botella"}'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Montilla", "type":"Tinto", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":15, "photo":"Gepeto", "cask":"hola", "bottle":"botella"}'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Rivera del Duero", "type":"Tinto", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":15, "photo":"Gepeto", "cask":"hola", "bottle":"botella"}'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Lando", "type":"Blanco", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":15, "photo":"Gepeto", "cask":"hola", "bottle":"botella"}'  https://natural-bus-135323.appspot.com/wines


addItem:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Rosa"}'  https://natural-bus-135323.appspot.com/clients/akanthor@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IxCxIHQ2xpZW50cyISYWthbnRob3JAZ21haWwuY29tDAsSBUNhcnRzGICAgICAgIAKDA/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Senorio de los Llanos"}'  https://natural-bus-135323.appspot.com/clients/akanthor@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IxCxIHQ2xpZW50cyISYWthbnRob3JAZ21haWwuY29tDAsSBUNhcnRzGICAgICAgIAKDA/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Black"}'  https://natural-bus-135323.appspot.com/clients/akanthor@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IxCxIHQ2xpZW50cyISYWthbnRob3JAZ21haWwuY29tDAsSBUNhcnRzGICAgICAgIAKDA/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Yugo"}'  https://natural-bus-135323.appspot.com/clients/akanthor@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IxCxIHQ2xpZW50cyISYWthbnRob3JAZ21haWwuY29tDAsSBUNhcnRzGICAgICA5JEKDA/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Rioja"}'  https://natural-bus-135323.appspot.com/clients/akanthor@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IxCxIHQ2xpZW50cyISYWthbnRob3JAZ21haWwuY29tDAsSBUNhcnRzGICAgICA5JEKDA/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Montilla"}'  https://natural-bus-135323.appspot.com/clients/akanthor@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IxCxIHQ2xpZW50cyISYWthbnRob3JAZ21haWwuY29tDAsSBUNhcnRzGICAgICA5JEKDA/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Rivera del Duero"}'  https://natural-bus-135323.appspot.com/clients/akanthor@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IwCxIHQ2xpZW50cyIRbW9uaWxsb0BnbWFpbC5jb20MCxIFQ2FydHMYgICAgICAgAoM/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Lando"}'  https://natural-bus-135323.appspot.com/clients/monillo@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IwCxIHQ2xpZW50cyIRbW9uaWxsb0BnbWFpbC5jb20MCxIFQ2FydHMYgICAgICAgAoM/items

deleteCarts:
	curl -X DELETE https://natural-bus-135323.appspot.com/

deleteClients:
	curl -X DELETE https://natural-bus-135323.appspot.com/clients

deleteCart:
	curl -X DELETE https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IvCxIHQ2xpZW50cyIQZW1haWwyQGdtYWlsLmNvbQwLEgVDYXJ0cxiAgICAgPKICgw

getItems:
	curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IvCxIHQ2xpZW50cyIQZW1haWwyQGdtYWlsLmNvbQwLEgVDYXJ0cxiAgICAgOSRCgw/items
