from datetime import date
from tabulate import tabulate

class calculadora:
    
    historial = []
    
    def __init__(self, usuario, numeros, tipo_operacion):
        self.__usuario = usuario
        self.__numeros = numeros
        self.__tipo_operacion = tipo_operacion 
        self.__resultado = None
        self.__fecha_uso = date.today()
        
    def calcular(self):
        n1 = self.__numeros.get_numero1()
        n2 = self.__numeros.get_numero2()
        
        if self.__tipo_operacion == "suma":
            self.__resultado = n1 + n2
        elif self.__tipo_operacion == "resta":
            self.__resultado = n1 - n2
        elif self.__tipo_operacion == "multiplicacion":
            self.__resultado = n1 * n2 
        elif self.__tipo_operacion == "division":
            if n2 != 0:
                self.__resultado = n1 / n2
            else:
                self.__resultado = "error: division por cero"
        else:
            self.__resultado = "operacion no valida"
            
        calculadora.historial.append([self.__usuario.nombre, self.__usuario.cedula, n1, n2, self.__tipo_operacion, self.__resultado, self.__fecha_uso])
    
    def mostrar_registro(self):
       
       encabezados = ["nombre", "cedula", "Numero1", "Numero2", "operacion", "Resultado", "Fecha"]
       
       print(tabulate(calculadora.historial, headers= encabezados, tablefmt="grid"))