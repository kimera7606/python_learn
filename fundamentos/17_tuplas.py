#Tuplas son como  listas que no se pueden modificar encerradas en parentesis ()
mi_tupla = ("hola", 12, True, 1.2) #datos encerrados con parenteiss 
print(type(mi_tupla)) #tuple

#las tuplas puede usar tanto index, como slicing 
#son inmutables es decir no se pueden modificar
# lo que si podemos hacer es index(), count(), 

#si quisieramos modiciar un tupla la podemos traformar a una lista y devolverla a tupal

mi_tupla = list(mi_tupla) #la comvertimos a lista
mi_tupla.append("he podido infiltrarme en la tupla") #usamos le metodo append() de lista
mi_tupla = tuple(mi_tupla)#la volvemos a convertir en tupla
print(mi_tupla) #aqui se puede visualizar el cambio





