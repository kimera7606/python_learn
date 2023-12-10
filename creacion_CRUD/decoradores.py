
#funcion decoradora

def decorador(funcion_simple):
    def decorando():
        print("se realizara un calculo")
        funcion_simple()
        print("se ha realizado la operacion")
    return decorando
@decorador
def suma():
    print (20 + 20)

@decorador
def multiplicacon(n1,n2):
    print( n1 * n2)

print(suma())
print(multiplicacon(3,5))