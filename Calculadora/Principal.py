from modelo_usuario import usuario
from modelo_numeros import numero
from modelo_calculadora import calculadora

usuario1 = usuario("juan garcia lopez", "1020345678")
usuario2 = usuario("maria lopez perez", "1020345679")
usuario3 = usuario("carlos rodriguez sanchez", "1020345680")

numero1 = numero (50, 30)
calc1 = calculadora(usuario1, numero1, "suma")
calc1.calcular()
calc1.mostrar_registro()

calc2 = calculadora(usuario1, numero1, "resta")
calc2.calcular()
calc2.mostrar_registro()

calc3 = calculadora(usuario1, numero1, "multiplicacion")
calc3.calcular()
calc3.mostrar_registro()

numero2 = numero(150, 3)
calc4 = calculadora(usuario1, numero2, "division")
calc4.calcular()
calc4.mostrar_registro()

numero3 = numero(100, 5)
cal5 = calculadora(usuario2, numero3, "suma")
cal5.calcular()
cal5.mostrar_registro()

calc6 = calculadora(usuario2, numero3, "resta")
calc6.calcular()
calc6.mostrar_registro()

calc7 = calculadora(usuario2, numero3, "multiplicacion")
calc7.calcular()
calc7.mostrar_registro()

calc8 = calculadora(usuario2, numero3, "division")
calc8.calcular()
calc8.mostrar_registro()

numero4 = numero(200, 8)
calc9 = calculadora(usuario3, numero4, "suma")
calc9.calcular()
calc9.mostrar_registro()

calc10 = calculadora(usuario3, numero4,"resta")
calc10.calcular()
calc10.mostrar_registro()

numero5 = numero(75, 3)
calc11 = calculadora(usuario3, numero5, "division")
calc11.calcular()
calc11.mostrar_registro()