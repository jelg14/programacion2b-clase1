"""
    **Autor: José Eduardo López González - 2204002004
    **Curso: Programacion IIB
    **Tarea 1: Llenar una estructura de datos con palabras e implementar el método de búsqueda por burbuja
"""
palabras = input("ingrese palabras a ordenar (separadas por espacios): ").lower().split()
c = 0
for x in palabras:
    c += 1
for i in range(c-1):
    for j in range(0,c-i-1):
        if palabras[j] > palabras[j+1]:
            palabras[j],palabras[j+1] = palabras[j+1],palabras[j]
print ("La lista ordenada es: \n",palabras)
