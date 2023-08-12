from random import choice
win_cpu = 0
win_player = 0
raunds = 1
def eleccion (x,y):
    if x == "piedra":
        print(f" {y} elije 'piedra'")
    elif x == "papel":
        print(f" {y} elije 'papel'")
    elif x == "tijera":
        print(f" {y} elije 'tijera'")
    else:
        print("datos incorrectos")

def combate(w,x,y,z):
    global win_player, win_cpu,raunds
    if w == y:
        print("'empate'")
    elif w == "piedra" and y == "tijera":
        print(f"'piedra' Gana a 'Tijera' punto para {x}  ")
        win_player += 1
    elif w == "papel" and y == "piedra":
        print(f"'papel' Gana a 'piedra' punto para {x}  ")
        win_player += 1
    elif w == "tijera" and y == "papel":
        print(f"'tijera' Gana a 'piedra' punto para {x}  ")
        win_player += 1
    else :
        print(f"'{y}' Gana a '{w}' punto para {z} ")
        win_cpu += 1
    raunds += 1
def game():    
    jugador =input("Cual es tu nombre? >> ")
   
    while True:
        opciones = ("piedra","papel","tijera")
        enemigo = "Computadora"
        print(f"Round: {raunds} - {jugador} : {win_player} - {enemigo}: {win_cpu}")
        print("*" * 15)
        usuario_eleccion = input("elije entre piedra, papel o tijera  >> ").lower()
        if not usuario_eleccion in opciones:
            continue
        usuario = usuario_eleccion
        cpu = choice(opciones)
        eleccion(usuario_eleccion,jugador)
        eleccion(cpu,enemigo)
        combate(usuario_eleccion,jugador,cpu,enemigo)
        if win_player == 3:
            print(f"Felicidades {jugador} Has ganado 3 rondas eres el GANADOR")
            break
        elif win_cpu == 3:
            print(f"lo sentimos {jugador}, has perdido 3 rondas contra {enemigo} has sido DERROTADO")
            break

if __name__ == "__main__":
    game()

