lista = [
    {
        "name" : "angel",
        "edad" : 30
    },
    {
        "name" : "albany",
        "edad" : 31
    },
    {
        "name" : "barbara",
        "edad" : 9    
    }
]
for i in lista:
    print (i) #en este caso i vale por el diccionario clave valor entero ya que es una lista
    #de diccionarios
#en caso de que quieras iterar por sus claves puedes hacerlo aqui un ejemplo

for i in lista: #aqui recorremos la lista
    print(f"nombre =>>", i["name"]) #asi que podemos mostrar i con su clave: para que
    print(i["edad"])#este solo muestre los valores de cada llave que encuentre con ese valor

productos = [
    {
    "producto" : "camisa",
    "color" : "negro",
    "precio" : 100,
    "stock" : 50
    },
    {
    "producto" : "pantalon",
    "color" : "azul",
    "precio" : 10,
    "stock" : 7
    },
    {
    "producto" : "corbata",
    "color" : "vede",
    "precio" : 23,
    "stock" : 5
    },
    {
    "producto" : "zapato",
    "color" : ["negro","marron"],
    "precio" : 30,
    "stock" : 99 
    },
    {
    "producto" : "sueter",
    "color" : "rosado",
    "precio" : 5,
    "stock" : 50 
    }
]

for i in productos:
    print("colores >>", i["color"])