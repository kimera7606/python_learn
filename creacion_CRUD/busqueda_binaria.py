import random
list_number = [random.randint(1,200) for i in range(100)]
print (list_number)

def busqueda_binaria(data,objetivo,bajo,alto):
    if bajo > alto:
        return False
    mid = (bajo + alto) //2
    if objetivo == data[mid]:
        return True
    elif objetivo < data[mid]:
        return busqueda_binaria(data, objetivo, bajo, mid -1)
    else:
        return busqueda_binaria(data, objetivo, mid +1, alto)

list_number.sort()

print(list_number)

numero = int(input("que numero te gustaria buscar"))
resultado =busqueda_binaria(list_number,numero,0,len(list_number) -1)
print (resultado)

'''
def busqueda_binaria(data,target,bajo,alto):
    if bajo > alto:
        return False
    mid = (bajo + alto) // 2
    if target == data[mid] :
        return True
    elif target < data[mid] :
        return busqueda_binaria(data, target, 0, mid-1)
    else :
        return busqueda_binaria(data, target, mid + 1, alto)
'''
