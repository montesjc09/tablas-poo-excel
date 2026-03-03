from Modelo_parqueadero import parqueadero
from usuario import Usuario
from Modelo_carro import carro

usuario1 = Usuario("1020345678", "Juan Garcia", "Administrador")
usuario2 = Usuario("1020345679", "Maria Lopez", "Cliente")
usuario3 = Usuario("1020345680", "Carlos Rodriguez", "Ciente")
usuario4 = Usuario("1020345681", "Ana Martinez", "cliente")

carro1 = carro("ABC123", "Sedan", "Negro")
carro2 = carro("XYZ789", "SUV", "Blanco")
carro3 = carro("KLM456", "Pickup", "Azul")
carro4 = carro("DEF321", "Hatchback", "Rojo")

registro1 = parqueadero("ABC123", "A-01", "2026-02-16", "08:30", None, "entrada")
registro2 = parqueadero("XYZ789", "B-05", "2026-02-16","9:15", None, "entrada" )
registro3 = parqueadero("KLM456", "C-12", "2026-02-16", "10:00", "11:45", "Salida" )
registro4 = parqueadero("DEF321", "A-03", "2026-02-16", "11:20", None, "entrada" )


print("\n" + "="*120)
print("SISTEMA DE PARQUEADERO")
print("="*120)

print(f"{'CEDULA':<12}{'NOMBRE':<18}{'TIPO':<15}{'PLACA':<10}{'MARCA':<12}{'COLOR':<10}{'PUESTO':<8}{'FECHA':<12}{'ENTRADA':<10}{'SALIDA':<10}{'ESTADO':<10}")

print("-"*120)

print(f"{usuario1.cedula:<12}{usuario1.nombre:<18}{usuario1.tipo_usuario:<15}{carro1.placa:<10}{carro1.marca:<12}{carro1.color:<10}{registro1.puesto:<8}{registro1.fecha_ingreso:<12}{registro1.hora_ingreso:<10}{str(registro1.hora_salida):<10}{registro1.estado:<10}")
print(f"{usuario2.cedula:<12}{usuario2.nombre:<18}{usuario2.tipo_usuario:<15}{carro2.placa:<10}{carro2.marca:<12}{carro2.color:<10}{registro2.puesto:<8}{registro2.fecha_ingreso:<12}{registro2.hora_ingreso:<10}{str(registro2.hora_salida):<10}{registro2.estado:<10}")
print(f"{usuario3.cedula:<12}{usuario3.nombre:<18}{usuario3.tipo_usuario:<15}{carro3.placa:<10}{carro3.marca:<12}{carro3.color:<10}{registro3.puesto:<8}{registro3.fecha_ingreso:<12}{registro3.hora_ingreso:<10}{str(registro3.hora_salida):<10}{registro3.estado:<10}")
print(f"{usuario4.cedula:<12}{usuario4.nombre:<18}{usuario4.tipo_usuario:<15}{carro4.placa:<10}{carro4.marca:<12}{carro4.color:<10}{registro4.puesto:<8}{registro4.fecha_ingreso:<12}{registro4.hora_ingreso:<10}{str(registro4.hora_salida):<10}{registro4.estado:<10}")

print("="*120)