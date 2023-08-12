#lo primero es importar el modulo de fast Api
from fastapi import FastAPI

app = FastAPI() # se crea una variable con la instancia de FastAPI
#podemos tambien accedel al localhot:#port/docs 
#nos llevara a una documentacion que nos describira toda sel endpoints
app.title = "Mi Aplicacion con FastAPI" #podemos agregarle un titulo
app.version = "3.2"
@app.get("/", tags=["home","film"])#creamos nuestro primero endpoint usando el @ + nombre instancia de fastapi
             # mas el metodo .get("aqui ira la ruta") 
#al lado de la ubicacion podemos añadir una lista de etiquetas
def messaje(): #creamos una funcion que se ejecutara
    return "Hola mundo!" # en este caso retornamos un msj

'''
una vez creado: debemos irnos a la terminal y utilizar los isguientes comandos
****************   uvicorn main:app --reload   *********************  
#luego de uvicorn viene le nombre del archivo:nombreapp("instancia")
#presionamos enter y se ejecutara y podemos verlo en el navedagor en el puerto 8000
#lo podemos comprobar en el localhost
'''
# para cambiar el puerto deberiamos añadir ejemplo: 
#  ****              --port 5000                  ****
#otra forma que podemos ver nuestra app es a travez de la red propia
#para hacer esto añadimos:
#*****              --host 0.0.0.0                *****
#podemos comprobarlo desde otro dispositivo con 
#                   http//0.0.0.0:500

