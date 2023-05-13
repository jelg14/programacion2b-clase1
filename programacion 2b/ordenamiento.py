from random import sample
def metodoBurbuja():
    #100 valores aleatorios en una list
    lista = list(range(100))
    #sub lista en base a la lista inicial
    lista2 = sample(lista, 8)
    #imprimir valores
    print("los valores son: ",lista2 )
    c = 0
    #contamos cuantos caracteres hay en lista2
    for x in lista2: 
        c += 1
    for i in range(c-1):
        for j in range(0,c-i-1):
            #revisa lista de 0 a n-i-1
            if lista2[j] > lista2[j+1]:
                lista2[j],lista2[j+1] = lista2[j+1],lista2[j]
    print ("La lista ordenada es: ",lista2)
lista = list(range(100))
vector = sample(lista, 8)
#recursividad
def QuickSort(vector, start= 0, end=len(vector)-1):
    print("lista a ordenar:",lista)
    def quick (vector, start =0, end = len(vector)-1):
        if start >= end: # si el inicio es igual a final, ya no se recorre
            return
        def particion(vector, start=0, end = len(vector)-1):
            pivot = vector[start]
            menor = start+1
            mayor = end
            while True:
                #si el valor actual es mayor a pivot, entonces esta en lugar correcto
                #caso contrario, moverlo
                while menor <= mayor and vector[mayor] >= pivot:
                    mayor = mayor - 1
                # ahora lo mismo para el menor
                while menor <= mayor and vector[menor] <= pivot:
                    menor = menor + 1
                if menor  <= mayor:
                    vector[menor], vector[mayor] = vector[mayor],vector[menor]
                else:
                    break
            vector[start], vector[mayor] = vector[mayor], vector[start]
            return mayor    
        p = particion(vector,start,end)
        quick(vector,start,p-1)
        quick(vector,p+1,end)
    quick(vector)
    print("vector ordenado con quick: ", vector)

QuickSort(vector)
print("QuickSort: ", vector)
#metodoBurbuja()
                
