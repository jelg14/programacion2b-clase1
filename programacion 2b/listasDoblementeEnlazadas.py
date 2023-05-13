class Node():
    def __init__(self, data:str):
        self.data = data
        self.next = None
        self.prev = None
        
class DogleLinked():
    def __init__(self) :
        self.head = None
        self.end = None

    def Agregar(self, data:str):
        nodo_nuevo = Node(data)
        if self.end is not None:
            nodo_nuevo.prev = self.end
            self.end.next = nodo_nuevo
            self.end = nodo_nuevo
            return
        self.head = nodo_nuevo
        self.end = nodo_nuevo
    
    def __str__(self):
        result =""
        temp_node = self.head
        while temp_node != None:
            result += temp_node.data+" , "
            temp_node = temp_node.next
        return result
    
    def buscar (self, data:str) -> Node:
        tempo_node = self.head
        while tempo_node != None:
            if tempo_node.data == data:
                return tempo_node
            tempo_node = tempo_node.next
        return None
    
    def imprimir_inverso (self) -> str:
        result = ""
        tempo_node = self.end
        while tempo_node != None:
            result += tempo_node.data +" , "
            tempo_node = tempo_node.prev
        return result
        
        
        