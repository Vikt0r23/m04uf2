#!/usr/bin/python3

from xml.dom import minidom

faix = minidom.parse('items.faix')
root = faix.getElementsByTagName('item')

root = root[0].childNodes

for element in root:
	if element.nodeType == element.TEXT_NODE:
	continue
	
		id = element.getAttribute('id')

		item = element.getElementsByTagname('item')
		item_value = item[0].firstChild.nodeValue

		type = element.getElementsByTagname('type')
		type_value = type[0].firstChild.nodeValue

		rarity = element.getElementsByTagname('rarity')
		rarity_value = rarity[0].getAttribute('value')


		 print(f"{id}\t {item_value}\t {type_value}\t {rarity_value}")

		 print("-"*64)

