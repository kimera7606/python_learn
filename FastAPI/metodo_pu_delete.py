from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "pagina de pelis"
app.version = "2.0"

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
async def add_movie(id:int = Body(), titulo:str = Body(), year:int = Body(), categoria:str = Body()):
    movies.append(
        {
            "id": id,
            "titulo": titulo,
            "year" : year,
            "categoria": categoria
        }
    )
    return movies
#aqui tenemos ambos metodos seguidos es facil poder leer la sintexis
@app.put("/Movies/{id}", tags= ["movies"]) #para modifica pedimos el id
async def update_movie(id:int, titulo:str = Body(),year:int = Body(), categoria:str = Body() ):
    for i in movies: #en este bloque modificamos el diccionario segun su id
        if i["id"] == id:
            i["titulo"] = titulo,
            i["year"] = year,
            i["categoria"] = categoria
    return movies #retinamos la lista nueva con el dicc modificado

@app.delete("/Movies/{id}", tags=["movies"]) #aqui usamos el metodo para borrar por id
async def remove_movie(id:int):
    for i in movies:
        if i["id"] == id:
            movies.remove(i) #utilizando el metodo de remove de las listas
    return movies
            