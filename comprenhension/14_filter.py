#con filter seleccionaremos elementos para que pertenezcana  una lista
#a travez de una condicional, los elementos se reducen a los que cumplan la condicional

numbers = list(range(1,11)) #creamos una lista de numeros
new_filter = list(filter(lambda x : x % 2 == 0, numbers))
'''
tiene la misma sintaxis que un map() solo que se crea una condicion, si algun dato
dentro de la lista a iterar cumple con esa condicion sera asignada a la variable con filter
'''
print(new_filter) #imprmimos el resultado

