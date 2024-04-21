from algoritmos.algoritmo import Algoritmo


class SJF(Algoritmo):
    def __init__(self, procesos: list, nombre: str, descripcion: str):
        super().__init__(procesos, nombre, descripcion)

    def _procesar(self):
        ordenado_rafaga = sorted(self.procesos, key=lambda x: x.rafaga)
        final = []
        ultima_atencion = 0

        while len(ordenado_rafaga) > 0:
            for proceso in ordenado_rafaga:
                if proceso.llegada <= ultima_atencion:
                    siguiente = proceso
                    ordenado_rafaga.remove(proceso)
                    break

            siguiente.atencion = ultima_atencion
            ultima_atencion += siguiente.rafaga
            final.append(siguiente)

        self.procesos = final
