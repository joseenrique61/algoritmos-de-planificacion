from algoritmos.algoritmo import Algoritmo
from proceso import Proceso


class RoundRobin(Algoritmo):
    def __init__(self, procesos: list, nombre: str, descripcion: str, quantum: int):
        super().__init__(procesos, nombre, descripcion)
        self.quantum = quantum

    def _procesar(self):
        self.procesos.sort(key=lambda x: x.llegada)

        for proceso in self.procesos:
            if proceso.rafaga > self.quantum:
                self.procesos.append(Proceso(proceso.nombre, proceso.rafaga - self.quantum, proceso.llegada, proceso.prioridad))
                proceso.rafaga = self.quantum
