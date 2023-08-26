#ne ocaciones queremos controlar que ciertos valores en nuestra plicacion cumplen con ciertos
#requerimientos, el temea de las validaciones
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from pydantic import BaseModel, Field #primero importamos de pydantic field
from typing import Optional

app = FastAPI()
app.title = "holis"
app.version= "3.1"

class Movies(BaseModel):
    id: Optional[int] = None
    titulo:str = Field(min_length= 1, max_length=30)#default= "valor o dato por defecto"
    año: int = Field(le= 2024) #le : que sea menor
    categoria:str = Field(min_length= 1, max_length= 30) #longuitud min, long max

    
    model_config = { #se crea model_config , se le asigna un diccionario
        "json_schema_extra": {#que contiene json_schema_extra que contiene otro diccionario
            "examples":  #que contiene exapmles la cual tiene como valor una lista
                { #esta lista lleva por dentro un diccionario ya asi con el ejemplo
                    "id": 1,
                    "titulo": "el padrino",
                    "año": 1999,
                    "categoria": "accion",
                }
            
        }
    }

movies = [
    {
        "id": 1,
        "titulo": "bastador sin gloria",
        "año" : 2019,
        "categoria" : "accion"
    },
    {
        "id": 2,
        "titulo": "300",
        "año" : 2008,
        "categoria" : "accion"
    },
    {
        "id": 3,
        "titulo": "el señor de los anillos",
        "año" : 2005,
        "categoria" : "fantasia"
    },
    {
        "id": 4,
        "titulo": "un sueño sin fin",
        "año" : 2018,
        "categoria" : "aventura"
    },
    {
        "id": 5,
        "titulo": "get out",
        "año" : 2015,
        "categoria" : "terror"
    },
    {
        "id": 6,
        "titulo": "medias de abejita",
        "año" : 2001,
        "categoria" : "drama"
    }
]
@app.get("/")
async def home():
    return HTMLResponse("<h1>PelisPerronas.com</h1>")

@app.get("/peliculas")
async def list_peliculas():
    return movies

@app.get("/peliculas/{id}")
async def get_id_movies(id: int):
    return [i for i in movies if i["id"] == id]

@app.get("/peliculas/categoria")
async def get_movie_category(category:str):
    return [i for i in movies if i["categoria"] == category]

@app.post("/peliculas")
async def post_movie(peli:Movies):
    movies.append(peli)
    return movies

@app.put("/peliculas/{id}")
async def upgrade_movie(id:int, peli:Movies):
    for i in movies:
        if i["id"] == id:
            i["titulo"] = peli.titulo
            i["año"] = peli.año
            i["categoria"] = peli.categoria
    return movies

@app.delete("/pelicula/{id}")
async def delete_movie(id:int):
    for i in movies:
        if i["id"] == id:
            movies.remove(i)
    return movies
