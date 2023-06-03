from Nodo import Node 
class Arbol():
    def __init__(self,dato):
        self.raiz = Node(dato)
        
#Recursividad = funcion que se llama a si misma
    def __agregar_recursivo(self,nodo,dato):
        if dato< nodo.data:
            if nodo.izquierda is None:
                nodo.izquierda = Node(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda,dato)#recursividad
            
        else:
            if nodo.derecha is None:
                nodo.derecha = Node(dato)
            else: 
                self.__agregar_recursivo(nodo.derecha,dato) #recursividad

    def __inorder_recursivo(self,nodo):
        if nodo is not None:
            self.__inorder_recursivo(nodo.izquierda)
            print(nodo.data,end=" ")
            self.__inorder_recursivo(nodo.derecha)

    def __preorder_recursivo (self,nodo):
        if nodo is not None:
            print(nodo.data,end=" ")
            self.__preorder_recursivo(nodo.izquierda)
            self.__preorder_recursivo(nodo.derecha)

    def __postorder_recursivo (self,nodo):
        if nodo is not None:
            self.__postorder_recursivo(nodo.izquierda)
            self.__postorder_recursivo(nodo.derecha)
            print(nodo.data,end=" ")        

    def __buscar (self,nodo,busqueda):
        if nodo is None: return None
        if nodo.data == busqueda: return nodo
        if busqueda < nodo.data:
            return self.__buscar(nodo.izquierda,busqueda)
        else: 
            return self.__buscar(nodo.derecha,busqueda)
        
    #Metodos publicos
    def agregar (self,dato):
        self.__agregar_recursivo(self.raiz,dato)
        
    def iniorder(self):
        print(" IN ORDER ")
        self.__inorder_recursivo(self.raiz)
        print(" ")

    def preorder(self):
        print(" PREORDER ")
        self.__preorder_recursivo(self.raiz)
        print(" ")
        
    def postorder(self):
        print(" POSTORDER ")
        self.__postorder_recursivo(self.raiz)
        print(" ")
        
    def buscar(self,busqueda):
        return self.__buscar(self.raiz,busqueda)

arbolito = Arbol(5)
arbolito.agregar (10)
arbolito.agregar (15)
arbolito.agregar (20)
arbolito.agregar (22)

arbolito.preorder()
arbolito.postorder()
arbolito.iniorder()

busqueda = int(input("ingrese parametro de busqueda: "))
valor = arbolito.buscar(busqueda)
if valor is not None:
    print("si existe")
else: print("no existe")