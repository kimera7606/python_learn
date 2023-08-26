from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()
app.title = "Pelis.com"
app.version = "4.0"

class Movies(BaseModel):
    id: Optional[int] = None
    titulo : str = Field(min_length= 1, max_length=25)
    año : int = Field(le= 2024)
    categoria : str = Field(min_length= 1, max_length= 15)
    
    model_config = {
        "json_schema_extra":{
            "example" : 
                {
                    "id" : 1,
                    "titulo" : "el padrino",
                    "año" : 1999,
                    "categoria" : "accion"
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
async def inicio():
    return HTMLResponse("<h1>PelisBuenas.com</h1>")

@app.get("/peliculas")
async def movie_list():
    return movies

@app.get("/peliculas/{id}")
async def get_movie_id(id:int):
    return [i for i in movies if i["id"] == id]

@app.get("/peliculas/")
async def get_movie_category(category:str):
    return list(filter(lambda x : x["categoria"] == category, movies))

@app.post("/peliculas/")
async def post_movie(peli:Movies):
    movies.append(peli)
    return movies

@app.put("/peliculas/{id}")
async def update_movie(id:int, peli:Movies):
    for i in movies:
        if i["id"] == id:
            i["titulo"] = peli.titulo
            i["año"] = peli.año
            i["categoria"] = peli.categoria
    return movies

@app.delete("/peliculas/{id}")
async def delete_movie(id:int):
    for i in movies:
        if i["id"] == id:
            movies.remove(i)
    return movies


