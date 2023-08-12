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
     },
    {
        "id" : 2,
        "titulo" : "300",
        "yer ": 2000,
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

    


