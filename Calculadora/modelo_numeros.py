class numero:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def get_numero1(self):
        return self.numero1
    
    def get_numero2(self):
        return self.numero2
    
    def set_numero1(self, numero1):
        self.numero1 = numero1
        
    def set_numero2(self, numero2):
        self.numero2 = numero2
        
    def mostrar_info(self):
        print("numero 1:", self.numero1)
        print("numero 2:", self.numero2)