class parqueadero:
    def __init__(self, numero_placa, puesto, fecha_ingreso, hora_ingreso, hora_salida, estado):
        self.numero_placa = numero_placa
        self.hora_ingreso = hora_ingreso
        self.hora_salida = hora_salida
        self.fecha_ingreso = fecha_ingreso
        self.puesto = puesto
        self.estado = estado

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso
    
    def get_puesto(self):
        return self.__puesto
    
    def get_hora_ingreso(self):
        return self.__hora_ingreso
    
    def get_numero_placa(self):
        return self.__numero_placa
    
    def get_hora_salida(self):
        return self.__hora_salida
    
    def get_estado(self):
        return self.__estado
    
    def set_hora_salida(self, nueva_hora):
        self.__hora_salida = nueva_hora

    def set_puesto(self, nuevo_puesto):
        self.__puesto = nuevo_puesto

    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def calcular_tiempo(self):
        return self.__hora_ingreso - self.__hora_salida
    
    def calcular_valor(self):
        tarifa_por_hora = 2000
        tiempo = self.calcular_tiempo()
        return tiempo * tarifa_por_hora
    
    def mostrar_info(self):
        return (f"numero_placa: {self.numero_placa} - puesto {self.puesto} - fecha_ingreso {self.fecha_ingreso} - hora_ingreso {self.hora_ingreso} - hora_salida {self.hora_salida} - estado {self.estado}")