from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Aprendiendo Backend con FastAPI"
app.version = "1.2"

movies = [ 
    {
        "id" : 1,
        "titulo" : "El Señor De Los Anillos",
        "year ": 2000,
        "categoria" : "fantasia"
     },
    {
        "id" : 2,
        "titulo" : "300",
        "year ": 2008,
        "categoria" : "accion"
     }
]

@app.get("/")
def inicio ():
    return HTMLResponse("<h1>Bievenido a mi pagina de pelis</h1><p>La mejor pagina de pelis del mundo</p>")

@app.get("/Movies" , tags= ["list_movies"])
def content():
    return movies

@app.get("/Movies/{id}", tags= ["movies"])
def get_movie_id(id:int):
    for i in movies:
        if i["id"] == id:
            return i
    return []
@app.get("/Movies/", tags= ["movies"])
def get_movies_category(category:str):
    for i in movies:
        if i["categoria"] == category:
            return i
    return []

@app.post("/Movies/add/", tags= ["movies"])
def add_movie(id:int = Body(), titulo:str = Body(),year:int = Body(), categoria :str = Body() ):
    movies.append(
        {
            "id" : id,
            "titulo" : titulo,
            "year" : year,
            "categoria" :categoria
        }
    )
    return movies