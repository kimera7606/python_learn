'''
#list comprenhension
en este concepto vamos a aprender generar listas de una manera mas rapida
, primero inicia con  [] y la primera parte con el elemento que sea parte de la lista
ese elemento lo obtenemos de un ciclo for, en le cual vamos a iterar cualquier
estructura de datos que tengamos def, como una lista, tupla o diccionario 
'''
#lista normal
lista = [] #creamos una variable de lista
for i in range(1,11): #un ciclo for en un rango espeficico
    lista.append(i) # por cada iteracion se le asignara le valor de i a la lista []
print(lista) #imprmimos la lista para ver su resultado

#lista con list comprehension
list_comprehension = [i for i in range(1,11)]
'''
el primer elemento es i, es el valor interno de lista, seguido de un for con la misma
variable la cual le sera asignado un valor por cada iteracion que le adicionara 
a la lista por cada valor obtenido por i
'''
print(list_comprehension)

#esta es otra manera de crear un lista esta vez con rango
lista_rango = list(range(1,11))
print(lista_rango)

#list comprehension con operadores
list_comprehension_operator = [i * 2 for i in range(1,11)]
print(list_comprehension_operator)
'''
como se puede observar una vez que el valor de i retorne un valor se debe multiplicar
*2 , luego de esa operacion es que se agregara a la lista
'''
list_comprehension_operator_conditional = [i *2 for i in range(1,101) if i % 2 == 0]
print(list_comprehension_operator_conditional)