#la lista es una variable que puede almacenar mas de un datos sin importar el tipo
lista = [1,"string",True, 2.35] #la lista se contiene en parentesis cuadrados
tareas = ["lavar los platos", "sacar la basura", "comprar la comida"]
numeros = [1,2,5,5,6,4,8,9,5,4,6,2]
#estos son ejemplos de listas
# a las listas tambien las podemos indexar es decir buscar sus datos dependiendo de su pocision 
print(tareas[2]) # me dara ""comprar la comida" que es la que esta en la posicion 2 de la variable tareas

#podemos tambien cambiar el valor de los datos contenidos en listas
#colocando la ubicacion a remplazar y luego el dato nuevo

cosas = ["plato", "mesa", "table", "lavadora", "pc", "tv"]
print(cosas)
#si quisieramos reemplazar alguno de esos datos por otro primero invocamos la varibale con la ubicacion a remmplazar , el signo de asginacion  (=) y luego el nuevo dato

cosas[2] = "aire acondicionado"
print(cosas) 

#tambien podemos usar slicing en las listas
print(cosas[1:3]) # este me retornara "mesa", "aire aocndicionado"

# (in) podmeos preguntar si algun dato esta contenido dentro de la lista
print("mesa" in cosas) #true
print("computadora" in cosas) #false

