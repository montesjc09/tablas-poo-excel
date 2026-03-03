class carro:
    def __init__(self,placa, marca, color):
        self.placa = placa
        self.marca = marca
        self.color = color

    def get_placa(self):
        return self.__placa
    
    def get_marca(self):
        return self.__marca
    
    def get_color(self):
        return self.__color
    
    def set_color(self, nuevo_color):
        self.__color = nuevo_color

    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

    def mostrar_info(self):
        return f" placa: {self.placa} - marca: {self.marca} - color: {self.color}"