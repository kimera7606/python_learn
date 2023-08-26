#empezemos a usar los metodos http 
from fastapi import FastAPI, Body
#podemso tambien importar html pero debemos hacer un from:
from fastapi.responses import HTMLResponse #para importar html 
pag = FastAPI()
pag.title = "metodos HTTP con FastAPI"
pag.version = "1.2"

movies = [ # creamos una lista de diccionarios en este caso solo tiene uno
    {
        "id" : 1,
        "titulo" : "El Señor De Los Anillos",
        "year ": 2000,
        "categoria" : "fantasia"
     },
    {
        "id" : 2,
        "titulo" : "300",
        "year ": 2000,
        "categoria" : "fantasia"
     }
]

@pag.get("/", tags=["catalogo"])

def msj ():
    return HTMLResponse("<h1> Hola </h> ") #como podemos ver es un operador 

@pag.get("/Movies", tags= ["movies"] ) #con el metodo get creamos una nueva ruta

def get_movies(): #esta funcion nos retorna la listga de peliculas que tenemos
    return movies # la lista ubicada esta debajo de la declaracion del fastapi

#filtrado de busqueda por su id, como recibir parametros en la ruta

@pag.get("/Movies/{id}", tags= ["movies"]) #para recibir parametro luego de la ruta 
#usamos {} y dentro el parametro, luego de la ruta un / seguido del parametro 
#encerrado en {} en este caso es {id} esta alimentara a la funcion de busqueda
def get_movie(id: int): #se crea una funcion con el parametro,se le asigna que sea int
    for item in movies: #se crea un ciclo for que iterara entre la lista de dict
        if item["id"] == id: #si i en su id coincide con nuestro parametro 
            return item #retornara esa lista
    
    return [] # si no retorna una lista vacia

#parametro query , son una serie clave valor que nos ayudaran a ampliar mas las busquedas sea en bases 
# de datos o en este caso lista de peliculas

@pag.get("/Movies/", tags= ["movies"]) #creamos dentro de la ubicacion
def get_movie_by_category(category:str,year : int): #una funcion con parametros
    for i in movies:
        if i["categoria"] == category:
            return i
    return []
#metodo post()

@pag.post("/Movies/", tags= ["movies"]) #aqui usamos le metodo post
def create_movie(id:int = Body(), titulo:str = Body(),year:int = Body(),categoria:str = Body()): #como vemos suvimos que importar body de fastapi, y le asignamos a cada parametro, en este caso es para alimentar nuestra api de nueva informacion
    movies.append( { #utilizamos el metodo de lista append() para agregar el nuevo dicc
        "id" : id, #asignamos las variables al diccionario
        "titulo" : titulo,
        "year" : year,
        "categoria" : categoria
    })
    return movies #una vez terminado retornamos la lista con el dict que añadimos nuevo
#podemos incluirlo en la documentacion de swangger, se cguardara mientras este en line la api

