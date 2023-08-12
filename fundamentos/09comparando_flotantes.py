#comparemos 3.3 con (1.1+2.2)
x = 3.3
print(x)
y = 1.1 +2.2
print(y)
#el resultado es falso ya que al ver uno tiene solo un decimal mientras el otro tiene mas
print(x == y)
#para quitarle los decimales a (y) y sea tru al compararlo con (x) podemos :
tolerance = 0.00001
print(abs(x-y) < tolerance)

#abs() es un operador que nos lleva todo los numeros a positivo
numero = -20.2
print (abs(numero))

