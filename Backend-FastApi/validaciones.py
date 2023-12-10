from fastapi import FastAPI, Path, Query #path se usa para parametros de ruta #query para parametor query
from fastapi.responses import HTMLResponse, JSONResponse 
from pydantic import BaseModel, Field #con fiel validamos la clase nuestros esquemas

app = FastAPI() 
app.title = "Mi app con FastAPi"
app.version = "v1.0"
#la clase field se utiliza en la clase, y se le asigna a cada propiedad despues del tipo de dato
class Usuarios (BaseModel): 
    id : int = Field(le= 200, ge= 0) #en el id elejimos dentro del field el minino y le maximo
    nombre : str = Field(min_length=3, max_length=16)
    correo : str = Field(min_length=8, max_length= 35)
    edad : int = Field(le= 200, ge= 10) # en este caso usamos el menor igual y el mayor igual
    profesion : str = Field(min_length=3, max_length= 50)

    model_config = { 
        "json_schema_extra" : { 
            "example" : { 
                "id" : 0,
                "nombre" : "Angel Jimenez",
                "correo" : "angel@gmail.com",
                "edad" : 30,
                "profesion" : "backend developer"
            }
        }
    }

user_list = [ 
    Usuarios(id=1, nombre= "Albany", correo= "albany@gmail.com", edad= 31, profesion= "orientadora"),
    Usuarios(id=2, nombre= "Nestor", correo= "nestor@gmail.com", edad= 24, profesion= "escritor"),
    Usuarios(id=3, nombre= "Gaston", correo= "gaston@gmail.com", edad= 37, profesion= "militar"),
    Usuarios(id=4, nombre= "Edilxon", correo= "edilxon@gmail.com", edad= 54, profesion= "electricista"),
    Usuarios(id=5, nombre= "Lorena", correo= "lorena@gmail.com", edad= 41, profesion= "analista de datos")
]

@app.get("/") 
async def inicio(): 
    return HTMLResponse("<h1>Usiarios.com</h1> <p>Bievenido a la pagina de los usuarios</p>" ) 

@app.get("/usuarios/", tags=["usuarios"], status_code= 200) #podemos con status code asignar un estado de respuesta correta en este caso 200 
async def list_user() : 
    return user_list
#las validacviones de tura se colocan en la dentro de la funcion despues de espeficicar le tipo de dato

@app.get("/usuarios/{id}", tags=["Usuarios"], status_code= 200)
async def get_id_user(id:int = Path(le= 2000, ge= 0 )):  #aqui un ejemplo de una validacion por ruta
    global user_list 
    return get_id(id)   

@app.get("/usuarios/", tags= ["Usuarios"], status_code= 200)
async def get_name(name:str = Query(min_length= 3, max_length= 30)): #ejemplo de un parametro query 
    global user_list 
    resultado = list(filter(lambda x : x.nombre == name, user_list)) 
    try:
        if len(resultado) > 0 : 
            return resultado
        else:
            return {"messaje" : "nombre no existe"}
    except:
        return {"messaje" : "datos invalidos"}

@app.post("/usuarios/", tags=["usuarios"], status_code= 201) #status code  200 
async def post_user(user:Usuarios): 
    global user_list
    user_list.append(user) 
    return {"messaje": "se creo nuevo usuario con exito"}

@app.put("/usuarios/", tags= ["usuarios"], status_code= 200) 
async def update_user(id:int, user:Usuarios): 
    global user_list
    for i in user_list: 
        if i.id == id: 
            i.nombre = user.nombre 
            i.correo = user.correo
            i.edad = user.edad 
            i.profesion = user.profesion
            return {"messaje" : "usuario modificado con exito"}
    return {"messaje" : "id no existe"}

@app.delete("/usuarios/", tags=["usuarios"], status_code= 200) 
async def delete_user(id:int): 
    global user_list
    for index, i in enumerate(user_list): 
        if i.id == id:
            user_list.pop(index) 
            return {"messaje" : "usuario eliminado con exito"}
    return {"messaje" : "id no existente"}
    

    
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
        