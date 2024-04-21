def calcular_tiempos(procesar):
    def funcion(self):
        procesar(self)

        calcular_atencion(self)
        imprimir_procesos(self)

        suma_esperas = 0
        suma_retornos = 0

        espera_retorno_round_robin(self)
        print("\nTiempos de procesos:")
        for proceso in sorted(self.procesos, key=lambda x: x.nombre):
            proceso.calcular_espera_retorno()

            suma_esperas += proceso.espera
            suma_retornos += proceso.retorno

            print(f"\nProceso: {proceso.nombre}")
            print(f"Espera: {proceso.espera}")
            print(f"Retorno: {proceso.retorno}")

        self.promedio_espera = float(suma_esperas) / float(len(self.procesos))
        promedio_retorno = float(suma_retornos) / float(len(self.procesos))

        print(f"\nTiempo promedio de espera: {self.promedio_espera} ut")
        print(f"Tiempos de retorno: {promedio_retorno} ut")

    def calcular_atencion(self):
        ultima_atencion = 0
        for proceso in self.procesos:
            proceso.atencion = ultima_atencion
            ultima_atencion += proceso.rafaga

    def espera_retorno_round_robin(self):
        cuenta_procesos = {}

        for proceso in self.procesos:
            if cuenta_procesos.get(proceso.nombre) is None:
                cuenta_procesos[proceso.nombre] = 0
            cuenta_procesos[proceso.nombre] += 1

        temp = []
        for nombre, cant in cuenta_procesos.items():
            if cant == 1:
                continue

            temp1 = []
            for proceso in self.procesos:
                if proceso.nombre == nombre:
                    temp1.append(proceso)
            temp.append(temp1)

        for lista in temp:
            atenciones = [lista[0].atencion]

            for i in range(1, len(lista)):
                atenciones.append(lista[i].atencion)
                self.procesos.remove(lista[i])

            lista[0].calcular_espera_retorno(atencion=atenciones, quantum=self.quantum, ultima_rafaga=lista[-1].rafaga, force_repetir=True)
            self.procesos.remove(lista[0])
            self.procesos.append(lista[0])

    def imprimir_procesos(self):
        string = "\nCadena de ejecución:\n"
        for proceso in self.procesos:
            string += f"{proceso.atencion}  {proceso.nombre}  "
        string += f"{self.procesos[-1].atencion + self.procesos[-1].rafaga}"

        print(string)

    return funcion