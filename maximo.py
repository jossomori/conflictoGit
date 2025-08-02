# Cada uno haga su implementación de la función maximo la cual 
# devuelve el máximo valor en una lista dada
def maximo(lista):
    n = len(lista)

    # Caso borde
    if n == 0:
        print('La lista es vacía')
        return None
    
    max = lista[0]
    for i in range(1, n):
        if lista[i] > max:
            max = lista[i]

    return max