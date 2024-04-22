#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('characters.facx', 'r')


soup = BeautifulSoup(file, 'xml')

characters = soup.find_all("character")

file.close()


title = "BIENVENIDOS A FARYADVENTURES"
print(title)
print("="*len(title))

print("\nQuien quieres ser?\n")

for character in characters:
	print(f"{character['id']}\t{character.find['name'].text}")

encontrado = False

while not encontrado:
id = input("\nIntroduce un numero: ")

file = open('characters.facx', 'r')
	#etiqueta = character.find('id')
	#print(etiqueta['value'])
soup = BeautifulSoup(file, 'xml')

file.close()



character = soup.find('character', {'id': choose})

if not character:
	print('ERROR: ID NO ENCONTRADO')
	exit()
else:
	encontrado = True

print("\nEl personaje escogido es:\n")
print(f"\tNombre: {character.find('name').text}")
print(f"\tEdad: {character.find('age').text}")
print(f"\tGenero: {character.find('gender')['value']}")
print(f"\tNivel: {character.find('level')['value']}")






