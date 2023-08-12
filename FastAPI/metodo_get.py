#empezemos a usar los metodos http 
from fastapi import FastAPI
#podemso tambien importar html pero debemos hacer un from:
from fastapi.responses import HTMLResponse #para importar html 
pag = FastAPI()
pag.title = "metodos HTTP con FastAPI"
pag.version = "1.2"

movies = [ # creamos una lista de diccionarios en este caso solo tiene uno
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

@pag.get("/Movies", tags= ["movies"] ) #con el metodo get creamos una nueva ruta

def get_movies(): #esta funcion nos retorna la listga de peliculas que tenemos
    return movies # la lista ubicada esta debajo de la delcaracion del fastapi


