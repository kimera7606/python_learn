# ahora usaremos pydantic una libreria echa de clases que nos ayudara en la sintaxis de modelos
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "pagina de pelis"
app.version = "2.0"

class Movie(BaseModel): #creamos una clase con parametro basemodel de pydantic
    id: Optional[int] = None #importamos opcional de typing
    titulo : str #definimos cada variable u objeto con su tipo
    year : int
    categoria : str

movies = [ # creamos una lista de diccionarios en este caso solo tiene uno
    {
        "id" : 1,
        "titulo" : "El Señor De Los Anillos",
        "yer ": 2000,
        "categoria" : "fantasia"
     },
    {
        "id" : 2,
        "titulo" : "300",
        "yer ": 2000,
        "categoria" : "accion"
     }
]

@app.get("/")
async def inicio():
    return HTMLResponse("<h1>Bienvenido a PelisPELIS.COM</h1><p>El mejor sitio para peliculas facheras <strong>FACHERITAS</storng></p>")

@app.get("/Movies", tags= ["movies"])
async def movie_list():
    return movies

@app.get("/Movies/{id}", tags= ["movies"])
async def get_movies_id(id:int):
    return [i for i in movies if i["id"] == id]

@app.get("/Movies/", tags=["movies"])
async def get_category_movies(category:str):
    return [i for i in movies if i["categoria"] == category]

@app.post("/Movies/add/", tags=["movies"])
async def add_movie(movie:Movie): #como parametro asigamos nuestra clase movie que se ligara al metodo post para que este con esos parametros pueda asignar valores 
    movies.append(movie)
    return movies #retonamos la nueva lista

@app.put("/Movies/{id}", tags= ["movies"])
async def update_movie(id:int, movie:Movie): #al momento de modificar dejamos el id
    #e incluimos nuestra classe movies
    for i in movies:
        if i["id"] == id:
            i["titulo"] = Movie.titulo #asignamos las varibales de la clase
            i["year"] = Movie.year
            i["categoria"] = Movie.categoria
    return movies

@app.delete("/Movies/{id}", tags=["movies"])
async def remove_movie(id:int):
    for i in movies:
        if i["id"] == id:
            movies.remove(i)
    return movies
            