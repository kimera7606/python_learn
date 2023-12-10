from fastapi import FastAPI, Query, Path
from fastapi.responses import HTMLResponse
from pydantic import Field, BaseModel

app = FastAPI()
app.title = "Servidor Peliculas con FastApi"
app.version = "v1.0"

class Peliculas(BaseModel):
    id : int
    nombre : str
    categoria : str
    sinopsis : str
    clasificacion : str
    
    model_config = {
        "json_schema_extra" : {
            "example" : {
                "id" : 0,
                "nombre" : "tropa de elite",
                "categoria" : "accion",
                "sinopsis" : "dos policias quedan atrapados en un tiroteo en las favelas, y son rescatados por el grupo especial Bope, y en los cuales ellos deciden formar parte despues",
                "clasificacion" : "B"
            }
        }
    }

lista_pelis= [
    Peliculas(id= 1,nombre ="el señor de los anillos",categoria = "aventura", sinopsis= "buscan destruir el anillo del señor oscuro", clasificacion= "A"),
    Peliculas(id= 2, nombre = "volver al futuro", categoria = "ciencia ficcion", sinopsis=  "viajar al pasado para construir le futuro", clasificacion= "A"),
    Peliculas(id= 3, nombre =  "troya", categoria = "accion", sinopsis = "la historia de aquiles", clasificacion= "B"),
    Peliculas(id= 4, nombre= "300",categoria= "accion", sinopsis= "300 spartanos van a la batalla en contra del rey jerges por la libertad de su pueblo", clasificacion= "C"),
    Peliculas(id= 5, nombre= "la sirenita",categoria= "aventura", sinopsis= "Ariel una sirena hija del rey triton rescata a un marinero de ahogarse, pero la verlo se enamora de el, e intenta acercarse mas conocerlo", clasificacion= "A")
]

@app.get("/" , tags= ["Inicio"])
async def inicio():
    return HTMLResponse("<h1>OpinaPelis.com</h1>")

@app.get("/peliculas", tags= ["CRUD"], status_code= 200)
async def lista():
    return lista_pelis

@app.get("/peliculas/{id}", tags=["Peliculas"], status_code= 200 )
async def id_pelis(id:int = Path(le= 2000)):
    resultado =  list(filter(lambda x : x.id == id, lista_pelis))
    if len(resultado) >= 1:
        return resultado
    else:
        return {"mensaje" : "id no existe"}
    
@app.get("/peliculas/", tags= ["Peliculas"], status_code= 200)
async def pelis_nombre(name:str):
    resultado = list(filter(lambda x : name in x.nombre, lista_pelis))
    if len(resultado) >= 1:
        return resultado
    else:
        return {"mensaje" : "nombre no esta registrado"}

@app.post("/peliculas/", tags= ["CRUD"], status_code= 201)
async def add_pelis(peli:Peliculas):
    global lista_pelis
    found = False
    resultado = list(filter(lambda x : x.id == peli.id, lista_pelis))
    if len(resultado) >= 1:
        return {"messaje" : "no se pudo registrar la pelicula debido a que el Id ya existe"}
    else:
        found = True
    if found == True:
        lista_pelis.append(peli)
        return {"mensaje" : "Pelicula registrada con exito"}

@app.put("/peliculas/{id}", tags= ["CRUD"], status_code= 200)
async def actualizar_pelicula(id:int, peli:Peliculas):
    global lista_pelis
    for i in lista_pelis:
        if i.id == id:
            i.nombre = peli.nombre
            i.categoria = peli.categoria
            i.sinopsis = peli.sinopsis
            i.clasificacion = peli.clasificacion
            return {"mensaje" : "se ha modificado la pelicula con exito"}
        else:
            return {"mensaje" : "id no encontrado"}

@app.delete("/peliculas/{id}", tags= ["CRUD"], status_code= 200)
async def borrar_pelicula(id:int):
    global lista_pelis
    for index, i in enumerate(lista_pelis):
        if i.id == id:
            lista_pelis.pop(index)
            return {"messaje" : "pelicula eliminada con exito"}
        else :
            return {"messaje" :"Id no encontrado"}
    