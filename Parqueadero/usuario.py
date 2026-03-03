class Usuario:
    def __init__(self, cedula, nombre, tipo_usuario):
        self.cedula = cedula
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario

    def get_cedula(self):
        return self.__cedula
    
    def get_nombre(self):
        return self.__nombre
    
    def get_tipo_usuario(self):
        return self.__tipo_usuario
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_tipo_usuario(self, nuevo_tipo):
        self.__tipo_usuario = nuevo_tipo
        
    def set_cedula(self, nueva_cedula):
        self.__cedula = nueva_cedula

    def mostrar_informacion(self):
        return f"Cedula: {self.cedula} - Nombre: {self.nombre} - Tipo: {self.tipo_usuario}"