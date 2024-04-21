class Proceso:
    def __init__(self, nombre: str, rafaga: int, llegada: int, prioridad: int):
        self.nombre = nombre
        self.rafaga = rafaga
        self.llegada = llegada
        self.prioridad = prioridad
        self.espera = 0
        self.retorno = 0
        self.atencion = 0
        self.repetido = False

    def calcular_espera_retorno(self, atencion: list = None, quantum: int = 0, ultima_rafaga=0, force_repetir=False):
        if self.repetido and not force_repetir:
            return

        if isinstance(atencion, list):
            self.retorno = atencion[-1] + ultima_rafaga

            self.espera = atencion[0] - self.llegada

            for i in range(1, len(atencion)):
                self.espera += atencion[i] - (atencion[i - 1] + quantum)
        else:
            self.espera = self.atencion - self.llegada
            self.retorno = self.atencion + self.rafaga

        self.repetido = True
