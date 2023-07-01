from Nodo import Node 
import time

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


print("ingrese usuario y contraseña")
user = input("ingrese usuario: ")
password = int(input("ingrese contraseña: "))
u = "admin"
p = 123

if(user == u and password == p):
    arbolito = Arbol(1)
    while (True):
        print("""
    ***************************************************
                ___  ___ _____  _   _  _   _
                |  \/  ||  ___|| \ | || | | |
                | .  . || |__  |  \| || | | |
                | |\/| ||  __| | . ` || | | |
                | |  | || |___ | |\  || |_| |
                \_|  |_/\____/ \_| \_/ \___/
    ***************************************************
    ***************************************************
    ** ingresar datos al arbol.................(1)
    ** mostrar datos del arbol ................(2)
    ** buscar dato especifico .................(3)
    ** Salir de la aplicacion .................(4)
    ***************************************************""")
        
        opcion = int(input())
        if opcion == 1:
            while (True):
                print("""indique metodo de llenado de informacion
                    1 ------ random
                    2 ------ teclado
                    3 ------ regresar""")
                decision = int(input())
                if decision == 1:
                    no = int(input("ingrese cantidad de datos aleatorios"))
                    print("llenando datos...")
                    time.sleep(1)
                    lista = list(range(no))
                    for i in lista:
                        arbolito.agregar(i)
                    print("datos ingresados exitosamente")
                elif decision == 2:
                    datos = input("ingrese los numeros que desea agregar separados por espacios: ").split()
                    for x in datos:
                        x = int(x)
                        arbolito.agregar (x)
                    print("datos ingresados exitosamente")
                elif decision == 3:
                    print("desea agregar otro dato?")
                    res = input()
                    if(res == 'no'):
                        break
        elif opcion == 2:
            print("opcion 2 ingresada")
            while (True):
                print("""indique orden de impresion
                    1 ------ preorden
                    2 ------ postorden
                    3 ------ inorden
                    4 ------ regresar""")
                decision = int(input())
                if decision == 1:
                    arbolito.preorder()
                if decision == 2:
                    arbolito.postorder()
                if decision == 3:
                    arbolito.iniorder()
                if decision == 4:
                    print("desea realizar otra impresion?")
                    res = input()
                    if(res == 'no'):
                        break
        elif opcion == 3:
            busqueda = int(input("ingrese parametro de busqueda: "))
            valor = arbolito.buscar(busqueda)
            if valor is not None:
                print("si existe")
            else: print("no existe")
        elif opcion == 4:
            print("Adios...")
            break
        else: print("ERROR: Comando desconocido")
else:
    print("Error: usuario no encontrado")

