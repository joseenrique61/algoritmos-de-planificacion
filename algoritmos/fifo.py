from algoritmos.algoritmo import Algoritmo


class FIFO(Algoritmo):
    def __init__(self, procesos: list, nombre: str, descripcion: str):
        super().__init__(procesos, nombre, descripcion)

    def _procesar(self):
        self.procesos.sort(key=lambda x: x.llegada)