from collections import *

raza = deque()
tamaño = deque()
edad = deque()
sexo = deque()
perros = deque()

print("""
***************************************************
            ___  ___ _____  _   _  _   _
            |  \/  ||  ___|| \ | || | | |
            | .  . || |__  |  \| || | | |
            | |\/| ||  __| | . ` || | | |
            | |  | || |___ | |\  || |_| |
            \_|  |_/\____/ \_| \_/ \___/
***************************************************
**************SELECCIONE UNA OPCION:***************
***************************************************
""")

while (True):
    print("""
** Agregar lista de perros.................(1)
** Mostrar listados ingresados ............(2)
** Salir de la aplicacion .................(3)
***************************************************""")
    opcion = int(input())
    if opcion == 1:
        print("procesando peticion...")
        while (True):
            dato1 =input("ingrese raza del perro que desea registrar: ")
            raza.append(dato1)
            dato2 =input("ingrese tamaño del perro que desea registrar: ")
            tamaño.append(dato2)
            dato3 =input("ingrese edad del perro que desea registrar: ")
            edad.append(dato3)
            dato4 =input("ingrese sexo del perro que desea registrar: ")
            sexo.append(dato4)
            print("desea agregar otro dato?")
            res = input()
            if(res == 'no'):
                #print("cola_raza:",raza)
                #print("cola_tamaño:",tamaño)
                #print("cola_edad:",edad)
                #print("cola_sexo:",sexo)
                break
    elif opcion == 2:
            while len(raza)>0 and len(tamaño)>0 and len(edad)>0 and len(sexo)>0:
                p={"Raza":raza.popleft(),"Tamaño":tamaño.popleft(),"Edad":edad.popleft(),"Sexo":sexo.popleft()}
                perros.append(p)
            print("Perros ingresados:",perros)
            print("***************************************************")
    elif opcion == 3:
        print("Adios...")
        break
    else: print("ERROR: Comando desconocido")