#empezemos a usar los metodos http 
from fastapi import FastAPI
#podemso tambien importar html pero debemos hacer un from:
from fastapi.responses import HTMLResponse #para importar html 
pag = FastAPI()
pag.title = "metodos HTTP con FastAPI"
pag.version = "1.2"

movies = [
    {
        "id" : 1,
        "titulo" : "El Señor De Los Anillos",
        "yer ": 2000,
        "categoria" : "fantasia"
     }
]

@pag.get("/", tags=["catalogo"])

def msj ():
    return HTMLResponse("<h1> Hola </h> ") #como podemos ver es un operador 

@pag.get("/Movies", tags= ["movies"] )

def get_movies():
    return movies
