#los diccionarios son variables que utilizan clave:valor, este tipo de datos
#se van encerrados entre corchetes, ({}) ej: dict = {}
my_dict = {
    "avion" : "trasporte volador",
    "cama" : "lugar de descanso",
    "nombre" : "identificativo",
    "lenguajes" : ["python", "java scrip"]    
}

print(my_dict)
#puedes usar metodos como len()
print(len(my_dict))
#in() puedes validar de que una clave este dentro del diccionario
print("avion" in my_dict)
#index(la clave),  pero este te retornara su valor, si no esta la clave lanzara error
print(my_dict["cama"])
#get() # es recomendable este operador ya que en caso de no estar la clave no lanza error
print(my_dict.get("avon"))

#actualizacion
print(my_dict)
my_dict["edad"] = 70
my_dict["edad"] -= 20
my_dict["lenguajes"].append("ruby")
print(my_dict)

 #eliminacion
 
 #del elimina una clave : valor del dict, se coloca (del) seguido de la variable y item
 
print(my_dict)
del my_dict["nombre"]
print(my_dict)

#pop()
my_dict.pop("lenguajes") #cuando se trabaja con diccionario es obligado colocar la clave
print(my_dict)

print(my_dict.items()) # muestra clave valor en lista
print(my_dict.values()) #muestra los valores en lista
print(my_dict.keys()) #muestra las claves en lista
