#empezemos primero a la importacion de los modulos para nuestra API con FastApi()
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import schema

#lo primero que tenemos que hacer es crear una variable y asignarle una instancia fastAPi

app = FastAPI()
app.title = "mi Api con FastApi"
app.version = "v.0.1"
#empezamos con el metodo GET
@app.get("/") #primero con @ + vairable de instancia fastapi + .get ("es decir el metodo http que queremos") seguido de la tura entre comillas, esta ruta sera la que se refleja en el link de la pagina en este caso el inici es / 
def inicio():
    return HTMLResponse("<h1> Pelis.com </h1>")

#para iniciar nuestra api debemos ir a la terminal y colocar uvicorn #nombre_de_archivo: #nombre_de_instacia --reload 
#opcinalmente podemos asigarnal el puerto que queramos con --port 5000 
#opcinalmente tambine podemos asignarla a la red del la cual estamos conectados con --host 0.0.0.0 

#en la ruta podemos entrar en /docs para manipular nuestra api con #swinger

