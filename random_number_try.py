import random
from queue import Queue

f = open('D:/UMG/Semestre 7/Progra3/Tareas/Random/Random.txt', 'w')
datos = Queue()

for i in range(1000000):
    datos.put(random.randint(-10000000, 10000000))
    datos.put(' ')
    imprimir = str(datos.get())
    f.write(imprimir)
f.close()

f = open ('D:/UMG/Semestre 7/Progra3/Tareas/Random/Random.txt','r')
lectura = input("¿Desea leer el archivo creado? Y/N ")
if(lectura == "Y"):
        numbers = f.read()
        print(numbers)
f.close()