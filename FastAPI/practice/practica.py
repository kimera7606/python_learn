from fastapi import FastAPI
from fastapi.responses import HTMLResponse

pag = FastAPI()
pag.title = "mi paginita"
pag.version = "1.2"

movies = [ 
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

@pag.get("/", tags= ["menu"])

def inicio():
    return HTMLResponse ("<h1> Bievenidos a mi pagina </h1> <p> tendramos muchas pelis para ti </p>")

@pag.get("/movies/{id}", tags= ["films"])
def get_movie(id:int):
    for i in movies:
        if i["id"] == id:
            return i
    return []


