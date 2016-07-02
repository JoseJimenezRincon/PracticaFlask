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
	curl -X DELETE https://natural-bus-135323.appspot.com/clients/email@gmail.com
	
updateClient:
	curl -X PUT -H "Content-Type: application/Json" -d '{"pass":"updated", "address":"updated", "phone":"updated"}'  https://natural-bus-135323.appspot.com/clients/email2@gmail.com

getClientDetails:
	curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/email2@gmail.com

addCart:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Blanco"}'  https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Navidad"}'  https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Nochevieja"}'  https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts

deleteCart:
	curl -X DELETE https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IvCxIHQ2xpZW50cyIQZW1haWwyQGdtYWlsLmNvbQwLEgVDYXJ0cxiAgICAgPKICgw

deleteCarts:
	curl -X DELETE https://natural-bus-135323.appspot.com/

addItem:
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"Yugo"}'  https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IvCxIHQ2xpZW50cyIQZW1haWwyQGdtYWlsLmNvbQwLEgVDYXJ0cxiAgICAgOSRCgw/items
	curl -X POST -H "Content-Type: application/Json" -d '{"name":"DonSimon"}'  https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IvCxIHQ2xpZW50cyIQZW1haWwyQGdtYWlsLmNvbQwLEgVDYXJ0cxiAgICAgOSRCgw/items

getItems:
	curl -X GET -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IvCxIHQ2xpZW50cyIQZW1haWwyQGdtYWlsLmNvbQwLEgVDYXJ0cxiAgICAgOSRCgw/items

delItem:
	curl -X DELETE -H "Content-Type: application/Json"  https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IvCxIHQ2xpZW50cyIQZW1haWwyQGdtYWlsLmNvbQwLEgVDYXJ0cxiAgICAgOSRCgw/items/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3J8CxIFQ2FydHMiX2FoUnpmbTVoZEhWeVlXd3RZblZ6TFRFek5UTXlNM0l2Q3hJSFEyeHBaVzUwY3lJUVpXMWhhV3d5UUdkdFlXbHNMbU52YlF3TEVnVkRZWEowY3hpQWdJQ0FnT1NSQ2d3DAsSBUl0ZW1zGICAgICAgIAKDA

updateItem:
	curl -X PUT -H "Content-Type: application/Json" -d '{"name":"Updated"}'  https://natural-bus-135323.appspot.com/clients/email2@gmail.com/carts/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3IvCxIHQ2xpZW50cyIQZW1haWwyQGdtYWlsLmNvbQwLEgVDYXJ0cxiAgICAgOSRCgw/items/ahRzfm5hdHVyYWwtYnVzLTEzNTMyM3J8CxIFQ2FydHMiX2FoUnpmbTVoZEhWeVlXd3RZblZ6TFRFek5UTXlNM0l2Q3hJSFEyeHBaVzUwY3lJUVpXMWhhV3d5UUdkdFlXbHNMbU52YlF3TEVnVkRZWEowY3hpQWdJQ0FnT1NSQ2d3DAsSBUl0ZW1zGICAgICA5JEKDA

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

