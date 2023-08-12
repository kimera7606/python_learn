#se pueden transformar las variables, cambiar sus tipos de datos de forma dinamica o con operadoress
#cambio dinamico
name = "angel"
print (type(name))
name = 23
print (type(name))

#cambio con operador
age = 23
print(type(age))
age = str(23)
print(type(age))

#para cambiar los input() que solo son cadenas de texto sin importar le dato
#puedes al final del operador int(input("")) eso comvierte directamente el dato entero
#los puedes hacer tambiien con los flotantes

#aqui trasformamos el input en entero 
edad = int(input("digita tu edad >> "))
print(type(edad))
#en futuro podemos usar el input para realizar una operacion matematica
futuro = 10 + edad
print (f"tu edad en 10 años sera {futuro}")
