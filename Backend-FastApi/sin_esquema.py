#aqui haremos un  servidor sin esquemas:
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

app = FastAPI()
app.title = "Api con FastApi"
app.version = "v1,0"

user_list = [
    {
        "id" : 1,
        "nombre" : "angel",
        "edad" : 31,
        "ocupacion" : "backend developer"
    },
    {
        "id" : 2,
        "nombre" : "albany",
        "edad" : 31,
        "ocupacion" : "orientadora"
    },
    {
        "id" : 3,
        "nombre" : "barbara",
        "edad" : 18,
        "ocupacion" : "diseñadora UX"
    }
]

@app.get("/")
async def inicio ():
    return HTMLResponse("<h1>Usuarios</h1>")

@app.get("/usuarios", tags= ["Usuarios"])
async def get_list():
    return user_list

@app.get("/usuarios/{id}")
async def get_id(id :int):
    return buscar_dato(id)

@app.get("/usuarios/", tags=["usuarios"])
async def get_name(name:str):
    global user_list
    resultado = list(filter(lambda x : x["nombre"]== name, user_list))
    try :
        if len(resultado) > 0:
            return resultado
        else:
            return {"error" : "id no existe"}
    except:
        return {"error" : "datos invalidos"}
    

@app.post("/usuarios/add/")
async def create_user(id : int = Body(), nombre : str = Body(), edad : int = Body(), 
ocupacion : str = Body()):
    global user_list
    add = {
        "id" : id,
        "nombre" : nombre,
        "edad" : edad,
        "ocupacion" : ocupacion
    }
    
    for i in user_list:
        if add["id"] ==  i["id"]:
            return {"error" : "id existente"}
    user_list.append(add)
    return {"messaje" : "se ha agregado nuevo usuario con exito"}

@app.put("/usuarios/{id}")
async def update_user(id : int, nombre : str = Body(), edad : int = Body(), 
ocupacion : str = Body()):
    global user_list
    for i in user_list:
        if i["id"] == id:
            i["nombre"] = nombre
            i["edad"] = edad
            i["ocupacion"] = ocupacion
            return {"messahje" : "usuario acualizado con exito"}
    return {"messaje" : "id no encontrado"}
    
    

@app.delete("/peliculas/{id}", tags= ["peliculas"])
async def delete_user (id:int):
    global user_list
    for index,i in enumerate(user_list):
        if i["id"] == id:
            print({"messaje" : "usuario eliminado con exito"})
            return user_list.pop(index)
        
    return {"messaje" : "id no encontrado"}
    
    

def buscar_dato(dato:int):
    global user_list
    resultado = list(filter(lambda x : x["id"]== dato, user_list))
    try :
        if len(resultado) > 0:
            return resultado
        else:
            return {"error" : "id no existe"}
    except:
        return {"error" : "datos invalidos"}

    

    

