#!/usr/bin/make -f
#-*- mode:makefile -*-

newClient:
	curl -X POST -H "Content-Type: application/Json" -d '{"email":"email@gmail.com", "pass":"ajdfksd", "address":"calle", "phone":"66666666"}' https://natural-bus-135323.appspot.com/clients
	curl -X POST -H "Content-Type: application/Json" -d '{"email":"email2@gmail.com", "pass":"ajdfksd", "address":"calle", "phone":"66666666"}'  https://natural-bus-135323.appspot.com/clients


addCart:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Botellon"}' https://natural-bus-135323.appspot.com/clients/email@gmail.com/carts 
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Inem"}' https://natural-bus-135323.appspot.com/clients/email@gmail.com/carts
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Verano"}'  https://natural-bus-135323.appspot.com/clients/email@gmail.com/carts

addWine:	
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Rosa", "type":"Rosado", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":54, "photo":"Gepeto" }' https://natural-bus-135323.appspot.com/wines 
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Senorio de los Llanos", "type":"Tinto", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":12, "photo":"Gepeto" }'  https://natural-bus-135323.appspot.com/wines
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Black", "type":"Tinto", "grade":12.4 , "size":75, "varietals":"nsnc", "do":false, "price":15, "photo":"Gepeto", "cask":"hola", "bottle":"botella"}'  https://natural-bus-135323.appspot.com/wines


addItem:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Yugo"}'  https://natural-bus-135323.appspot.com/clients/email@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IuCxIHQ2xpZW50cyIPZW1haWxAZ21haWwuY29tDAsSBUNhcnRzGICAgIDAiJ0LDA/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Rioja"}'  https://natural-bus-135323.appspot.com/clients/email@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IuCxIHQ2xpZW50cyIPZW1haWxAZ21haWwuY29tDAsSBUNhcnRzGICAgIDAiJ0LDA/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Montilla"}'  https://natural-bus-135323.appspot.com/clients/email@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IuCxIHQ2xpZW50cyIPZW1haWxAZ21haWwuY29tDAsSBUNhcnRzGICAgICArpkLDA/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Rivera del Duelo"}'  https://natural-bus-135323.appspot.com/clients/email@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IuCxIHQ2xpZW50cyIPZW1haWxAZ21haWwuY29tDAsSBUNhcnRzGICAgIDgsIUJDA/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Montillo"}'  https://natural-bus-135323.appspot.com/clients/email@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IuCxIHQ2xpZW50cyIPZW1haWxAZ21haWwuY29tDAsSBUNhcnRzGICAgICArpkLDA/items
	#curl -X POST -H "Content-Type: application/Json" -d '{"name":"vinoBlanco"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICA3qWFCgw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3I4CxIHQ2xpZW50cxiAgICA3qWFCgwLEgVDYXJ0cxiAgICAgICACgwLEgVJdGVtcxiAgICAgPKICQw/items
	#curl -X POST -H "Content-Type: application/Json" -d '{"name":"White"}'  https://natural-bus-135323.appspot.com/clients/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IUCxIHQ2xpZW50cxiAgICA3qWFCgw/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3I4CxIHQ2xpZW50cxiAgICA3qWFCgwLEgVDYXJ0cxiAgICAgICACgwLEgVJdGVtcxiAgICAgPKICQw/items

deleteCarts:
	curl -X DELETE https://natural-bus-135323.appspot.com/

deleteClients:
	curl -X DELETE https://natural-bus-135323.appspot.com/clients

deleteCart:
	curl -X DELETE https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IvCxIHQ2xpZW50cyIQZW1haWwyQGdtYWlsLmNvbQwLEgVDYXJ0cxiAgICAgPKICgw

getItems:
	curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IvCxIHQ2xpZW50cyIQZW1haWwyQGdtYWlsLmNvbQwLEgVDYXJ0cxiAgICAgOSRCgw/items
