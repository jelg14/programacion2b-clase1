#DEFINICION DE PUNTERO: apunta a una direccion en memoria la cual puede tener o no informacion 
alumno = "Juan Gomez"
edad = 21
#tipo de dato
print (type(edad))
print(isinstance(edad,int))

#tupla: listado que no puede cambiar en tiempo de ejecucion
input_list = (1,2,3,4,5)
print(input_list)
print(type(input_list))
input_list2 = (1,1,1,2,3,3,4,5,5,5,5,66,7,8,9,9,9,9,9,9)
print(set(tuple(input_list2)))

#diccionario
input_dict ={"0":"Leo",
    "1":"Miguel",
    "2":"José",
    "3":"Oliver",
    "4":"Mario",
    "5":"Santiago",
    "6":"Pedro",
    "7":"Calan"
    }
print(input_dict)

if "2" in input_dict:
    print("encontrado")

print(type(input_dict.get("Santiago")))    

print(input_dict.values())
print (type(input_dict.values()))

carro = {
    "marca":"BMW",
    "modelo":"328I",
    "serie":"3",
    "version":"F30",
    "año_fabricacion":"2015",
}

print(carro.keys())
print(carro.pop("modelo")) #quita un valor del diccionario carro 
print(carro.keys())

for x, y in carro.items():
    print(x,"=>",y)
    
#operaciones de punteros
#incrementar
x = 10
print("x es igual a ",x,"\n")
#direccion de memoria
print("direccion: ",id(x))
x += 1
print("x es igual a ",x,"\n")
print("direccion: ",id(x))

#decrementar
x= 100
print("x es igual a ",x,"\n")
#direccion de memoria
x -= 1
print("x es igual a ",x,"\n")
print("direccion: ",id(x))

def fun (a,b,c,d):
    print(a,b,c,d)

x=(100,200,300,400)
y={"a":'I',"b":"Love","c":"trash","d":"food"}
fun(*x)
fun(**y)