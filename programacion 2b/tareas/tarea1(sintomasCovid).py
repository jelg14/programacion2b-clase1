"""
    **Autor: José Eduardo López González
    **Curso: Programacion IIB
    **Tarea 1: Crear lista enlazada con sintomas de covid
"""


class Nodo(object):# clase que permite crear un nuevo nodo para la lista
    def __init__(self, data=None, next = None):
        self.data = data # guarda informacion dentro del nodo
        self.next = next # muestra el puntero donde se ubica el siguiente nodo


class linkedList(): # clase para crear lista enlazada
    def __init__(self):
        """ indica el primer nodo ingresado en la lista,
        al ser nueva, no tendra nodo, por lo cual esta vacio """
        self.head = None

    def insertEndNode(self, new_node):# inserta nuevo nodo al final de la lista
        """ valida si posee encabezado (primer nodo) o no, de ser
            verdadero, guarda el puntero actual (encabezado) como ultimo nodo """
        if self.head:
            last_node = self.head
            """ si el ultimo nodo no esta vacio, asigna el puntero del actual nodo como ultimo
                en caso contrario, asigna el nuevo nodo como puntero de ultimo nodo """
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = new_node

        # si el encabezado esta vacio, asigna el nuevo nodo como tal
        else:
            self.head = new_node

    def printList(self):
        data = self.head
        print("SINTOMAS COVID-19:")
        while data != None:
            print("#",data.data, end='\n')
            data = data.next

sintomas_covid = linkedList()
sintomas_covid.insertEndNode(Nodo("fiebre"))
sintomas_covid.insertEndNode(Nodo("tos"))
sintomas_covid.insertEndNode(Nodo("dificultad para respirar"))
sintomas_covid.insertEndNode(Nodo("fatiga"))
sintomas_covid.insertEndNode(Nodo("dolor muscular"))
sintomas_covid.printList()