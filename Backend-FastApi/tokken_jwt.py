from jwt import encode, decode #primero importamos jwt e importamos encode

def create_tokken(data: dict): #en este caso creamos una funcion que recibirar datos de tipo dict
    token = encode(payload = data, key= "my_key", algorithm= "HS256") #dentro creamos una variable en la cual asignamos el modulo encode que nos pedira 3 parametros
    return token #luego retornamos el token

def validate_token(token : str):
    data : dict = decode(token, key="my_key", algorithms= ["HS256"])
    return data
    
    
    