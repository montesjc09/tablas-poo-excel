class usuario:
    def __init__(self,nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        
    def get_nombre(self):
        return self.nombre
        
    def get_cedula(self):
        return self.cedula
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def set_cedula(self, nueva_cedula):
        self.id = nueva_cedula
        
    def mostrar_info(self):
        print(f"nombre: {self.nombre}, cedula: {self.cedula}")