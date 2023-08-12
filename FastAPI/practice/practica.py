from fastapi import FastAPI

app = FastAPI()
app.title = "Aprendiendo API con FastAPI en PLATZI"
app.version = "3.3.9"

@app.get("/", tags= ["inicio", "servicios", "menu"])

def msj ():
    return "holis cara de bolis"



