#los ciclos for se itulizan para recorrer rangos o iterables

for i in range(20): #para i(i es una variable que sera igual a cada elemento que recorra)
    print (i)
'''
en este ejemplo tenemos la variable i que sera la que recorrera en el rango 
dado de 20, lo que pasara internamente es que i sera igual a cada dato dentro del rango
es decir, al pricio valdra 0, luego volvera a iterar, y valdra 1, luego entrara y continuara
su recorrido, hasta que recorra todo el rango, al ejecutarlo veras que se imprime
el valor de i mientras recorria la el rango de 20

#tambien el ciclo for puede recorrer listas, tuplas, o iterables
'''

lista = ["angel", "barbara", "thais", "albany", "yoshi"] #aqui tenemos una lista
for i in lista: # aqui decimmos que para i en la lista, es decir recorrera la lista 
    print(i) #obteniendo i el valor de cada dato que encuentre y imprimiendolo
    
numeros = [1,2,3,4,5,6,7,8,9]
#tambien podemos dentro del ciclo utilizarlo para realizar operaciones matematicas
numeros_por_2 = [] #creamos una lista vacia
for i in numeros: #para i en la lista de numeros
    numeros_por_2.append(i * 2) #numeros por dos le agregamos a i*2 es decir
    #tomara el valor de i de la lista de numeros y los multiplicara * 2
    #y finalmente los agregara a numeros_por_2 con metodo append()

print(numeros_por_2)

#for con diccionarios:
producto = { #tenemos un diccionario con su clave , valor
    "camisas" : 20,
    "precio" : 10,
    "color" : "negro"
}

for i in producto: #aqui para i dentro del producto osea el diccionario
    print(i) #imprimira el valor de i que seran sus claves
    
for i in producto.values(): #se utiliza el operador values para mostrar sus valores
    print(i) #en este caso imprimira sus valores

for i,x in producto.items(): #aqui se utilizan el operador items() para que muestre clave:valor
    print(f"clave: {i} , valor: {x}") # se crearon dos variables para que a cada uno se le asigne un dato sea el valor o la clave


