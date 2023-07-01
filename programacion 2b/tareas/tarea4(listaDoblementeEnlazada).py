class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.ultimo is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def insertar_en_segunda_posicion(self, dato):
        if self.primero is None or self.primero.siguiente is None:
            return

        nuevo_nodo = Nodo(dato)
        segundo_nodo = self.primero.siguiente
        nuevo_nodo.siguiente = segundo_nodo
        segundo_nodo.anterior = nuevo_nodo
        self.primero.siguiente = nuevo_nodo
        nuevo_nodo.anterior = self.primero

    def insertar_en_ante_ultima_posicion(self, dato):
        if self.ultimo is None or self.ultimo.anterior is None:
            return

        nuevo_nodo = Nodo(dato)
        ante_ultimo_nodo = self.ultimo.anterior
        nuevo_nodo.anterior = ante_ultimo_nodo
        ante_ultimo_nodo.siguiente = nuevo_nodo
        self.ultimo.anterior = nuevo_nodo
        nuevo_nodo.siguiente = self.ultimo

    def borrar_primer_nodo(self):
        if self.primero is None:
            return

        if self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            siguiente_nodo = self.primero.siguiente
            siguiente_nodo.anterior = None
            self.primero = siguiente_nodo

    def borrar_segundo_nodo(self):
        if self.primero is None or self.primero.siguiente is None:
            return

        segundo_nodo = self.primero.siguiente
        if segundo_nodo == self.ultimo:
            self.primero.siguiente = None
            self.ultimo.anterior = None
            self.ultimo = self.primero
        else:
            siguiente_nodo = segundo_nodo.siguiente
            self.primero.siguiente = siguiente_nodo
            siguiente_nodo.anterior = self.primero

    def borrar_ultimo_nodo(self):
        if self.ultimo is None:
            return

        if self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            anterior_nodo = self.ultimo.anterior
            anterior_nodo.siguiente = None
            self.ultimo = anterior_nodo

    def eliminar_nodo_mayor_info(self):
        if self.esta_vacia():
            return None

        nodo_actual = self.primero
        nodo_max = self.primero
        max_dato = self.primero.dato

        while nodo_actual is not None:
            if nodo_actual.dato > max_dato:
                max_dato = nodo_actual.dato
                nodo_max = nodo_actual
            nodo_actual = nodo_actual.siguiente

        if nodo_max.anterior is not None:
            nodo_max.anterior.siguiente = nodo_max.siguiente
        else:
            self.primero = nodo_max.siguiente

        if nodo_max.siguiente is not None:
            nodo_max.siguiente.anterior = nodo_max.anterior
        else:
            self.ultimo = nodo_max.anterior

        return nodo_max.dato

    def printList(self):
        dato = self.primero
        print("SINTOMAS COVID-19:")
        while dato != None:
            print("#",dato.dato, end='\n')
            dato = dato.siguiente

# Ejemplo de uso:
lista = ListaDoblementeEnlazada()
lista.insertar_al_principio(10)
lista.insertar_al_final(5)
lista.insertar_al_final(20)
lista.insertar_en_ante_ultima_posicion(8)
lista.insertar_en_segunda_posicion(15)
print("LISTA COMPLETA:")
lista.printList()


# Eliminar el nodo con mayor información
mayor_informacion = lista.eliminar_nodo_mayor_info()
print("Nodo con mayor información eliminado:", mayor_informacion)
lista.printList()