from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()
app.title = "Mi app con FastApi"
app.version = "V1.0"

class Peliculas(BaseModel):
    id : int
    nombre : str
    categoria : str
    sinopsis : str

    model_config = {
        "json_schema_extra" : {
            "example" : {
                "id" : 0,
                "nombre" : "tropa de elite",
                "categoria" : "accion",
                "sinopsis" : "unos policias honestos de rio de janeiro deciden enfrentar la corrupcion ingresando a el grupo de elite bope"
            }
        }
    }

pelis_list = [
    Peliculas(id= 1,nombre ="el señor de los anillos",categoria = "aventura", sinopsis= "buscan destruir el anillo del señor oscuro"),
    Peliculas(id =2, nombre = "volver al futuro", categoria = "ciencia ficcion", sinopsis=  "viajar al pasado para construir le futuro"),
    Peliculas(id = 3, nombre =  "troya", categoria = "accion", sinopsis = "la historia de aquiles")
]

@app.get("/", tags=["menu"])
def inicio():
    return HTMLResponse ("<h1> Pelis.com </h1> " )

@app.get("lista")
def lista():
    return pelis_list
