import random
from queue import Queue

TipoArch = input("¿Desea generar el archivo con colas(C) o pilas(P)? C/P ") 

f = open('D:/UMG/Semestre 7/Progra3/Tareas/Random/Random2.txt', 'w')

if TipoArch == "C":
    print("Creando archivo con colas...")
    datos = Queue()
    for i in range(1000000):
        datos.put(random.randint(-10000000, 10000000))
        datos.put(' ')
        imprimir = str(datos.get())
        f.write(imprimir)
f.close()

if TipoArch == "P":
    print("Creando archivo con pilas...")
    pilas = [0]
    for i in range(1000000):
        pilas.append(random.randint(-10000000, 10000000))
        pilas.append(' ')
        imprimir = str(pilas)
        f.write(imprimir)
f.close()

f = open ('D:/UMG/Semestre 7/Progra3/Tareas/Random/Random2.txt','r')
lectura = input("¿Desea leer el archivo creado? Y/N ")
if(lectura == "Y"):
        numbers = f.read()
        print(numbers)
f.close()