# Cada uno haga su implementación de la función maximo la cual 
# devuelve el máximo valor en una lista dada
def maximo(lista):

    largo_lista = len(lista)

    """ 
    ## Repasando bubble-sort

    Ejemplo: [7,4,3]
    largo_lista = 3
    
    i = 0
    j = 0, ... , 3-0-1 = 2
        j = 0: 7 > 4  =>  [4,7,3]
        j = 1: 7 > 3 => [4,3,7]
        j = 2: 7 > (j = 3 > 2) => Sale
    
    i = 1
    j = 0, ... , 3-1-1 = 1
        j = 0: 4 > 3 => [3,4,7]
        j = 1: 4 > j = 2 > 1 => Sale

    devuelve: [3,4,7]

    """
    # Primero ordeno la lista:
    
    # Recorremos la lista
    for i in range(largo_lista):
        for j in range(0, largo_lista-i-1):

            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    # Una vez terminemos de ordenar,
    # El valor máximo será el último elemento de la lista.

    valor_maximo = lista[largo_lista - 1]

    # Acomodando un poco la salida si es entero.
    return int(valor_maximo) if valor_maximo.is_integer() else valor_maximo