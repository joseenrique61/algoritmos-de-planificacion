from abc import abstractmethod
from calculadorDeTiempos import calcular_tiempos


class Algoritmo:
    def __init__(self, procesos: list, nombre: str, descripcion: str):
        self.procesos = procesos
        self.nombre = nombre
        self.descripcion = descripcion
        self.promedio_espera = 0

    @calcular_tiempos
    def organizar(self):
        print(f"\n\n{self.nombre}")
        print(self.descripcion)

        self._procesar()

    @abstractmethod
    def _procesar(self):
        pass

