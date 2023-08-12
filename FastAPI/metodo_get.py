#empezemos a usar los metodos http 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse #para importar html 
pag = FastAPI()
pag.title = "metodos HTTP con FastAPI"
pag.version = "1.2"

@pag.get("/", tags=["catalogo"])

def msj ():
    return HTMLResponse("<h1> Hola </h> ") #como podemos ver es un operador 

