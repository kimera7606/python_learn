#CRUD , crear, leer, actualizar, borrar

numbers = [1,2,5,6,2,54,5,46,6]
print (numbers)

'''
si quieiseramos remplazar un elemento la lista podemos usar el index con igualdad (=)
pero tambien existen otros metodos cuales serian para agregar insert() y append()
appen() #agrega al final de la lista
insert() # agrega con un index el nuevo dato a la lista , este recibira dos parametros
'''
numbers.append(700) #ejemplo de append()
print(numbers)
numbers.insert(2, "hola") #ejemplo de insert()
print(numbers)
# recordemos que estos metodos no remplazan, mas bien agregan
#y corren la lista a la derecha

#podemos tambien sumar listas por ejemplo
lista1 = [1,2,32,4,5]
lista2 = ["hola","como","estas","tu"]
lista_nueva = lista1 + lista2 #une ambas listas
print(lista_nueva)

#index() para conocer la posicion de un dato podemos usar le metodo index
#este llevara como parametro el dato que se quiere tener la poscision
print(lista_nueva.index("como")) # retornara la posicion si existe de ese dato

#para borrar datos existen dos metodos pop(), remove()
listita = [1,2,5,5,656,"hola","casa", True, "123", False,1.2]
#remove pedira como parametro el dato a elminar
listita.remove(5) #removeremos el 5 que esta repetido
print(listita)
#pop() por defecto elimina el ultimo elemento, pero tambien puede recibir un index
listita.pop()
print(listita) #aqui elimianmos el ultimo elemento
listita.pop(1) #aqui elminamos el segundo elemento de la lista
print(listita) 

#reverse() nos sirve para invertir la lista
listita.reverse()
print(listita)
#sort() lo que hace es ordenar nuestra lista, simepre y cuando sean del mismo tipo de dato
prueba = [3,5,1,2,12,15,1,5,6,3,496,4,1,1,6,4]
print(prueba)
prueba.sort()
print(prueba)



