'''
normalmente tenemos varios bloques de codigo, en vez de escribir esos bloques de codigos
multiples veces los encerramos en bloques de funciones para poderlos reutilizar
nuevamente desde diferentes puntos, con eso ganamos mantenibilidad 
'''
print("hola") #creamos un print que mostrara en patalla "hola"
#la podemos volver una funcion un aque imprima cualquier dato que se le asigne 

def my_print(msj): #utilizamos def palabra reservada para declarar un funcion
    print(msj) #dentro de la funcion definimos el comportamiento del codigo
mansaje_secreto = "Hola este es un msj secreto"
mensaja_2 = "hola este es un segundo msj"
#ejemplos
my_print(mansaje_secreto) #imprimira el contenido de la variable
my_print(mensaja_2) #imprimira el contenido de la variable
my_print(5+5) #imprimira le resultado de la operacion matematica
my_print("imprimamos un txt") #imprimra el string

#ejemplos 2

def sumita (a,b): # creamos un funcion que requiere dos parametros a y b
    return a+ b # dentro de la funcion tomara ambos parametros y los sumara
print(sumita(10,89)) #sumara ambos valores
print(sumita(99,2544)) #sumara ambos valores

#tambien podemos usar funciones dentro de las funciones

def multi (number): # creamos una funcion con un parametro
    return sumita(number,number) * number #dentro de la funcion ejecutamos otra funcion
#y multiplicamos su resultado por le mismo parametro de entrada, para ambas funciones
print(multi(2))




