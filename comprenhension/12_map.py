'''
#MAP :
# su funcion principal es hacer traformaciones en una lista
dada de elementos, normalmente en listas o iterables
simepre obtendras le mismo numero de elemtos despues de la transformacion
'''
#crearemos una variamos con numeros y luego sus diferentes metodos para traformarla
numbers = list(range(1,11)) #se crea una lista de numero de numeros (1-20)
print(numbers)#se imprime la lista de numeros

#*** List comprehension ***#
numbers_lch = [i * 2 for i in numbers] #se trasfroma con list comprehension
print(numbers_lch)#se muestra en la consola

#**** usando ciclo for ****#
numbers_for = [] #se crea una lista vacia
for i in numbers: #se inicia un ciclo for en la lista
    numbers_for.append(i * 2) #se adiciona cada elemento y se multiplica x 2 en lista vacia
print(numbers_for) # se muestra el resultado en la consola
#***** MAP *******#
numers_map = list(map(lambda x : x * 2,numbers)) #se usa el metodo map
print(numers_map)
'''
como podemos observar le metodo map contiene un lambda, primero se mete dentro de 
una lista ya que map es un objeto, luego se usa le operador map, y dentro de este
se usa una lamda la cual recibe un dato, y retorna o adiciona que ese dato
sera multiplicado por 2, y al final se coloca la lista de la cual se esta alimentando
'''
print("*" * 15 )
#otro ejemplo seria, donde sumemos dos listas
numeros1 = list(range(1,21))# se crean una lista con range
print(numeros1)
numeros2 = [i for i in range(22,41)] #se crea una lista con lch
print(numeros2)

suma_de_listas= list(map(lambda a,b : a +b, numeros1,numeros2)) #se usa con map se suma
print(suma_de_listas)
print("*" * 15)
suma_2 = sum(numeros1) + sum(numeros2)
print(suma_2)
print(sum(suma_de_listas))
