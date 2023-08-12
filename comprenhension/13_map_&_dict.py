'''
en este caso usaremos map con una lista de diccionarios
en este caso primero:
'''
items = [ #creamos una lista de diccionarios
    {
        "producto": "camisa", #esta lista tiene llaves producto
        "precio" : 120 #y precio
    },
    {
        "producto" : "pantalon",
        "precio" : 120
    },
    {
        "producto" : "zapatos",
        "precio" : 150
    }
]
precios = list(map(lambda x : x["precio"], items)) #en este caso usamos map
print(precios) #para obtener solo los precios de cada diccionario
#ahora queremos agrear una nueva llave a la lista de diccionarios
def add_taxes (dicc): #creamos una funcion
    new_item = dicc.copy()#creamos una copia para evitar modificar le original 
    new_item["taxes"] = new_item["precio"] * .15 #esta funcion recibe un dicc y le adiciona taxes
    return new_item #retorna el diccionario

taxes = list(map(add_taxes,items)) 
print(taxes)
'''
en este map : como se puede observar no hay lambda, se creo una funcion, esta funcion
se aplicara para cada diccionario dentro de la lista recordemos que el map itera
, una vez dentro aplica la funcion , y luego le damos de donde se alimentara
en este caso de la lista de diccionarios que es items
'''
print("************modificado con copia************")
print(taxes)
print("**************original*************")
print(items)
