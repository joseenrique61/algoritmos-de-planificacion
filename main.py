from proceso import Proceso
from algoritmos.fifo import FIFO
from algoritmos.sjf import SJF
from algoritmos.prioridad import Prioridad
from algoritmos.round_robin import RoundRobin


def crear_procesos():
    return [
        Proceso("A", 3, 2, 2),
        Proceso("B", 1, 4, 3),
        Proceso("C", 3, 0, 1),
        Proceso("D", 4, 1, 3),
        Proceso("E", 2, 3, 4)
    ]


algoritmos = [
    FIFO(crear_procesos(), "FIFO", "Se ordenan según el orden de llegada."),
    SJF(crear_procesos(), "SJF", "Se ordenan según la ráfaga de la CPU a medida \n"
                                 "que van llegando. Si un proceso tiene menor ráfaga que otro pero \n"
                                 "aún no llega, se atiende primero el otro."),
    Prioridad(crear_procesos(), "Prioridad", "Usa la prioridad para organizar los procesos. \n"
                                             "Si dos tienen la misma prioridad, usa FIFO para organizarlos."),
    RoundRobin(crear_procesos(), "Round Robin", "Organiza los procesos y los ejecuta usando FIFO.\n"
                                                " Si algún proceso se pasa de cierta cantidad preestablecida de\n"
                                                " tiempo, el resto de su ejecución se vuelve a añadir \n"
                                                "a la cola de procesos.", 3),
]

for algoritmo in algoritmos:
    algoritmo.organizar()

print("\nTiempo promedio de espera de cada algoritmo:")
for algoritmo in algoritmos:
    print(f"{algoritmo.nombre}: {algoritmo.promedio_espera} ut")

mejor_proceso = sorted(algoritmos, key=lambda x: x.promedio_espera)[0]
print(f"\nMejor tiempo de espera:\n{mejor_proceso.nombre}: {mejor_proceso.promedio_espera} ut")
