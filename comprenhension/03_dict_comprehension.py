from random import randint
'''
#diccionario comprehension
al igual que las listas estos deben ser invocados con {} ya que es la representacion
de listas, luego iniciamos con un par clave valor seguid de un ciclo for
'''

diccionario = {} #creamos el diccionario vacio
for i in range (1,11): #un ciclo for 
    diccionario[i] = i *2 #por cada iteracion de i, se le asigna un valor al dic vacio
print (diccionario) #se imprime el dict para poderlo visualizar

#dict comprehension
dict_comprehension = {i : i*2 for i in range(1,11)}
'''
iniciamos con {}, luego colocamos clave valor aseparados con (:) esto vendra de
nuestra iteracion con for 
'''
print(dict_comprehension)
#creando dict comprehension a partir de listas

countries = ["venezuela", "canada", "usa", "nicaragua", "panama", "colombia"]
#creamos una lista
population_dict_comprenh = {i : randint(20000,90000) for i in countries}
#decimos que la variable recorrera una lista tomara su valor y como llave un randint
print(population_dict_comprenh)
#imprimimos el diccionario

#de forma tradicional
dict_lista = {}
for i in countries:
    dict_lista[i] = randint(1,50)
print(dict_lista)

#zip: es para unir dos listas y crear un diccionario
nombres = ["angel","albany","pochita","barbie"]
edades = [30,31,25,9]
union_con_zip = dict(zip(nombres,edades))
print(union_con_zip)
#otra opcion seria
union_zip_comprenhension= {name:age for (name,age) in zip(nombres,edades)}
print(union_zip_comprenhension)


