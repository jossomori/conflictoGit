# Importamos función maximo del módulo maximo.py
from maximo import maximo

def main():
    n = int(input('Cuántos elementos vas a agregar a la lista?\n'))
    lista = []

    for i in range(n):
        valor = float(input(f'Ingresa el elemento {i+1} de la lista:\n'))
        lista.append(valor)

    print(f'Lista final: {lista}')
    print(f'El máximo valor de la lista es {maximo(lista)}')

# Esto significa: 'Si este archivo se ejecuta..'
if __name__ == '__main__':
    main()