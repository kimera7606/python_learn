from fastapi import FastAPI
from fastapi.responses import HTMLResponse
pag = FastAPI ()
pag.title = "Pag de Pelis"
pag.version = "1.0"

pelis = [
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
        "categoria" : "fantasia"
     }
]

@pag.get("/peliculas", tags= ["catalogo"])

def menu():
    return HTMLResponse("<h1> Bievenido a mi pagina de pelis </h1>")

@pag.get("/movies", tags= ["movies"])

def get_movies ():
    return pelis




