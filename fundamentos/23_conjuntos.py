'''
#conjuntos: son estructuras de datos que tienen algo en comun, su principal 
caracteristica es que es mutable, e incluso podemos realizar operaciones entre ella
los conjuntos no tienen orden es especifico
los ocnjuntos no permiten duplicados, es decir no pueden tener datos repetido
el conjunto se encierra entre corchetes, pero sin clave calor, solo datos u elementos
'''
conjuntos_paises = {"colombia", "bolivia", "venezuela"} #ejemplo de sintaxis
print (type(conjuntos_paises)) #dara como output type (set)

set_numbers = {1,2,2,2,3,4,4,2,5} #conjunto de numeros
print (set_numbers) #su output nos dara solo los numeros unicos, que no se repitan

#podemos definir tambien un conjunto a travez de otra estructura
numeros = [1,2,3,3,5,444,6,7,7,77] #se crea una lista de numeros
print (numeros)
numeros = set(numeros) #lo volvemos un conjunto
print (numeros)
#recordemos que cuando convertimos alguna estructura en set() elimina los datos repetidos
