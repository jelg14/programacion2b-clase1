#------------------LISTAS ENLAZADAS (clase 2)
#Nodo: cada uno de los objetos enlazados
#como mayor desventaja es que consume demasiados recursos del ordenador 

#creacion de nodo como primer paso
class Nodo(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

#creacion de lista como segundo paso -> Agregar al inicio, agregar al final, eliminar, obtener, vacio
class LinkedList():
    def __init__(self):
        self.head = None
    #agregando al inicio de la lista
    def agregarInicio(self,data):
        self.head = Nodo(data=data, next = self.head)
    #agregando al final de la lista
    def agregarFinal(self,data):
        if not self.head:
            self.head = Nodo(data=data)
            return
        actual = self.head
        while actual.next:
            actual.next            
        actual.next = Nodo(data = data)
    #vacio
    def esta_vacio(self):
        return self.head == None
    #eliminar 
    def eliminarNodo(self,index):
        actual = self.head
        previo = None
        #valida que el valor sea dif. a none
        while actual and actual.data != index:
            previo = actual
            actual = actual.next
        if previo is None:
            self.head = actual.next
        elif actual:
            previo = actual.next
            actual.next = None
    #obtener ultimo nodo
    def obtenerNodo(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp.data
    #imprimir nodos
    def printList(self):
        data = self.head
        while data != None:
            print(data.data)
            data = data.next
    
lista = LinkedList()
lista.agregarInicio(100)
lista.agregarFinal(200)
lista.agregarInicio(300)
lista.printList()

