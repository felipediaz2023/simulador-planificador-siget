

import time

class Proceso:
    def __init__(self, nombre, tiempo_irrupcion, prioridad, tamaño_datos):
        self.nombre = nombre
        self.tiempo_irrupcion = tiempo_irrupcion
        self.prioridad = prioridad
        self.tamaño_datos = tamaño_datos
        self.estado = "Nuevo"

    def mostrar(self):
        print(f"{self.nombre} | Estado: {self.estado} | Tiempo restante: {self.tiempo_irrupcion}")


# PROCESOS DEL SIGET
procesos = [
    Proceso("P1 - Sensores de tráfico", 5, 2, 100),
    Proceso("P2 - Emergencia accidente", 3, 1, 50),
    Proceso("P3 - Actualizar mapa", 7, 3, 200)
]


print("\nSIMULACIÓN FIFO\n")

cola = procesos.copy()

for proceso in cola:

    proceso.estado = "Listo"
    proceso.mostrar()

    proceso.estado = "En ejecución"
    print(f"\nEjecutando {proceso.nombre}")

    while proceso.tiempo_irrupcion > 0:
        proceso.tiempo_irrupcion -= 1
        proceso.mostrar()
        time.sleep(1)

    proceso.estado = "Terminado"
    proceso.mostrar()

print("\nTodos los procesos terminaron (FIFO)")


# ROUND ROBIN@

print("\nSIMULACIÓN ROUND ROBIN\n")

procesos_rr = [
    Proceso("P1 - Sensores de tráfico", 5, 2, 100),
    Proceso("P2 - Emergencia accidente", 3, 1, 50),
    Proceso("P3 - Actualizar mapa", 7, 3, 200)
]

quantum = 2

cola = procesos_rr.copy()

while cola:

    proceso = cola.pop(0)

    proceso.estado = "En ejecución"
    print(f"\nEjecutando {proceso.nombre}")

    tiempo = min(quantum, proceso.tiempo_irrupcion)

    for i in range(tiempo):
        proceso.tiempo_irrupcion -= 1
        proceso.mostrar()
        time.sleep(1)

    if proceso.tiempo_irrupcion > 0:
        proceso.estado = "Listo"
        cola.append(proceso)
    else:
        proceso.estado = "Terminado"
        proceso.mostrar()

print("\nTodos los procesos terminaron (Round Robin)")
