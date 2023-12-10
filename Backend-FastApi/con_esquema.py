from fastapi import FastAPI #se importa fastapi
from fastapi.responses import HTMLResponse, JSONResponse #las distintas respuestas
from pydantic import BaseModel, Field #basemodel que es la clase para el esquema

app = FastAPI() 
app.title = "Mi app con FastAPi"
app.version = "v1.0"

class Usuarios (BaseModel): #se crea clase y a este se le asigna el basemodel de pydantic
    id : int #se define cada uno de las propiedas y se especifica el tipo de dato
    nombre : str
    correo : str
    edad : int
    profesion : str

    model_config = { # dentro de la clase se escribe model_config que sera el esquema ejemplo
        "json_schema_extra" : { #contendra un diccionario con la llave json_scshema_extra que tendra como clave otro dict
            "example" : { #este dic contenido en json schema sera le example
                "id" : 0, #donde finalmente colocaremos el ejemplo del esquema que queramos
                "nombre" : "Angel Jimenez",
                "correo" : "angel@gmail.com",
                "edad" : 30,
                "profesion" : "backend developer"
            }
        }
    }

user_list = [ #creamos una lista de objetos basados en el esquema al cual le asignaremos cada propiedad con su valor
    Usuarios(id=1, nombre= "Albany", correo= "albany@gmail.com", edad= 31, profesion= "orientadora"),
    Usuarios(id=2, nombre= "Nestor", correo= "nestor@gmail.com", edad= 24, profesion= "escritor"),
    Usuarios(id=3, nombre= "Gaston", correo= "gaston@gmail.com", edad= 37, profesion= "militar"),
    Usuarios(id=4, nombre= "Edilxon", correo= "edilxon@gmail.com", edad= 54, profesion= "electricista"),
    Usuarios(id=5, nombre= "Lorena", correo= "lorena@gmail.com", edad= 41, profesion= "analista de datos")
]

@app.get("/") #el primero metodo es get en este meotodo especificamos la ruta entre comillas
async def inicio(): #las funciones deben ser asyncronas
    return HTMLResponse("<h1>Usiarios.com</h1> <p>Bievenido a la pagina de los usuarios</p>" ) # en esta funcion retornamos un html con htmle responde de fastapi

@app.get("/usuarios/", tags=["Usuarios"]) #podemos colocarle etiquetas dentro de una lista entre comillas 
async def list_user() : #creamos una fucion que retornara en lista el contenido de los objetos creados anteriormente
    return user_list 

@app.get("/usuarios/{id}", tags=["Usuarios"]) #utilizamos un parametro ruta en este caso el id, este parametro ira al lado de la ruta en este caso un entero que simbolizara el id del elemento que queremos buscar
async def get_id_user(id:int): #creamos la funcion y como parametro el id y espeficicamos que tipo de dato es
    global user_list #utilizamos le global para poder acceder a la lista de propiedades de los objetos que creamos
    return get_id(id) #en este caso hemos creado un funcion que filtra por id y devuelve lo encontrado

@app.get("/usuarios/", tags= ["Usuarios"]) #en este caso usamos el metodo get para buscar por nobre
async def get_name(name:str): #en este caso es un parametro query y no de ruta ya que no especidicamos en la ruta como en id anterior
    global user_list #utilizamos el global para acceder desde el scope
    resultado = list(filter(lambda x : x.nombre == name, user_list)) #filtramos dentro de la lista por el nombre usando (.) ya que este actua como un objeto
    try:
        if len(resultado) > 0 : #solo si la longuitud del resultado en ,mayor a 1 significa que encontro algo y lo devolvera en caso de no entonces retornara que no existe
            return resultado
        else:
            return {"messaje" : "nombre no existe"}
    except:
        return {"messaje" : "datos invalidos"}

@app.post("/usuarios/", tags=["usuarios"]) #aqui usamos el metodo post
async def post_user(user:Usuarios): #al parametro le decimos que es de tipo Usuario ya que esta es la clase que creamos con basemodel de esta manera reconocera automaticamente que el esquema creado anteriormente
    global user_list
    user_list.append(user) #simplemente agregamos con metodo apend el user 
    return {"messaje": "se creo nuevo usuario con exito"}

@app.put("/usuarios/", tags= ["usuarios"]) #creamo el metodo put para actualizar
async def update_user(id:int, user:Usuarios): #en este caso llamamos el id y especificamos el tipo de dato por que aqui elejiremos el objeto segun su id para modificar seguido tambien de un paramtro que viene representado con el objeto
    global user_list
    for i in user_list: 
        if i.id == id: #cuando coindcida con el ciclo entonces ingresamos a cada uno de sus datos para poder modificarlos
            i.nombre = user.nombre 
            i.correo = user.correo
            i.edad = user.edad # se debe actuar como si se tratara de objetos siempre
            i.profesion = user.profesion
            return {"messaje" : "usuario modificado con exito"}
    return {"messaje" : "id no existe"}

@app.delete("/usuarios/", tags=["usuarios"]) #finalmente borramos o eliminamos un elemento
async def delete_user(id:int): #usamos el id para ubicar le metodo que vamos a eliminar 
    global user_list
    for index, i in enumerate(user_list): #se crea un ciclo con un enumarte para obtener tambien el index a eliminar cunaod coincida con nuestro id
        if i.id == id:
            user_list.pop(index) #con metrodo pop mas el index eliminamos el elemento
            return {"messaje" : "usuario eliminado con exito"}
    return {"messaje" : "id no existente"}
    

            
        
     
   #esta funcion solo nos permite buscar por el id 
    
def get_id(id:int):
    global user_list
    resultado = list(filter(lambda x : x.id == id, user_list))
    try:
        if len(resultado) > 0 :
            return resultado
        else:
            return {"messaje" : "id no existe"}
    except:
        return {"messaje" : "datos invalidos"}
        

    
    
    
