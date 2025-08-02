# Cada uno haga su implementación de la función maximo la cual 
# devuelve el máximo valor en una lista dada
def maximo(lista):

	if not lista:
		return None  

	max_valor = lista[0]
	for numero in lista[1:]:
		if numero > max_valor:
			max_valor = numero
	return max_valor