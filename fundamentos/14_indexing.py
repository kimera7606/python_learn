texto = "ella sabe python y espera pronto dominar todo para seguir avanzando"
print (texto)
#indexing : es un metodo para buscar por posicion dentro de un string, o lista
'''
primero colocamos la variable despues entre corchetes cuadrados , escribir numericamente 
la posicion del caracter al cual queramos acceder, recuerda que las pocisiones 
van de 0 en adelante es decir el primer caracter es el numero 0 
'''
print (texto[0]) # te mostrara el primer caracter 
print (texto[16]) # te mostrara el numero 17 "causalmente es un espacio"
print (texto[-1]) # te mostrara el ultimo caracter

#slacing o rebanadas, elijes el inicio y el fin con indexing, hace rebanas de lo que deseas
print (texto[0:16]) #el inicio en este caso es 0 y mostrara hasta el 16
print(texto[:16]) #por defecto si no colocas nada en el primer parametro simepre es desde el inicio
print(texto[16:]) #y si en el segundo caracter no colocas nada se entendera que ira al ultimo caracter 
#tambine exiten los saltos es decir saltar ciertos caracteres sean de dos en dos de 3 en 3 o como se quiere
print(texto[::2]) # en este caso saltara los caracteres de 2 en 2 
