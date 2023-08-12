#metodos para crear, leer, actualizar, y borrar conjuntos (crud)

#len()
set_countries = {"venezuela", "colombia", "francia", "canada"}
print (len(set_countries))  #metodo len para saber su longuitud

#in () para conocer si un dato existe dentro de la estructura set()
print ("bolivia" in set_countries) #False
print ("canada" in set_countries) #True

# add()
set_countries.add("bolivia") #con le metodo add() se adiciono un dato mas al conjunto
print (set_countries) #solo adiciona un nuevo dato

#update()
set_countries.update({"argentina", "ecuador", "panama"}) #adiciona mas de un dato
print(set_countries)#podemos ver que en este caso adiciono 3 datos mas

#remove()
set_countries.remove("bolivia") # se removio un dato con su nombre
print (set_countries) #en caso de de que no exista lanzara error

#discard # es mejor usar este preferiblemente
set_countries.discard("argentina") #remueve argentina
print(set_countries)
set_countries.discard("peru")#avisa que el elemento no esta sin lanzar error
print(set_countries)

#clear () borra todo el conjunto
set_countries.clear()
print(set_countries) #mostarara un set en vacio


