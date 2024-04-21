from algoritmos.algoritmo import Algoritmo


class Prioridad(Algoritmo):
    def __init__(self, procesos: list, nombre: str, descripcion: str):
        super().__init__(procesos, nombre, descripcion)

    def _procesar(self):
        self.procesos.sort(key=lambda x: x.prioridad)

        ultima_prioridad = 0
        final = []
        temp = []

        for proceso in self.procesos:
            if proceso.prioridad != ultima_prioridad:
                final += temp
                temp.clear()

            temp.append(proceso)
            temp.sort(key=lambda x: x.llegada)

        final += temp
        self.procesos = final
