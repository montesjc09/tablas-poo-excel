import tkinter as tk

registros = []

def calcular(operacion):
    n1 = float(num1.get())
    n2 = float(num2.get())

    if operacion == "suma":
        r = n1 + n2 
    elif operacion == "resta":
        r = n1 - n2
    elif operacion == "multi":
        r = n1 * n2 
    elif operacion == "divi":
        r = n1 / n2 

    resultado.config(text="resultado: " + str(r))

def guardar():
    id_usuario = cedula.get()
    nombre_usuario = nombre.get()
    res =resultado.cget("text")
   
    dato = "ID: " +  id_usuario + " - Nombre: " + nombre_usuario + "-" + res
    registros.append(dato)
    
    historial.config(text="\n".join(registros))

ventana = tk.Tk()
ventana.title("calculadora basica")
ventana.config(width=450, height=650)

frame1 = tk.LabelFrame(ventana, text="usuario")
frame1.pack(padx=10, pady=10)

tk.Label(frame1, text="cedula:").pack()
cedula = tk.Entry(frame1)
cedula.pack()

tk.Label(frame1, text="nombre:").pack()
nombre = tk.Entry(frame1)
nombre.pack()

frame2 = tk.LabelFrame(ventana, text="numeros")
frame2.pack(padx=10, pady=5)

tk.Label(frame2, text= "numero 1:").pack()
num1 = tk.Entry(frame2)
num1.pack()

tk.Label(frame2, text="numero 2:").pack()
num2 = tk.Entry(frame2)
num2.pack()

frame3 = tk.LabelFrame(ventana, text= "operaciones")
frame3.pack(padx=10, pady=10)

resultado = tk.Label(frame3, text= "resultado: ")
resultado.pack()

tk.Button(frame3, text= "suma", command=lambda: calcular("suma")).pack()
tk.Button(frame3, text= "resta", command=lambda: calcular("resta")).pack()
tk.Button(frame3, text= "multipliacion", command=lambda: calcular("multi")).pack()
tk.Button(frame3, text= "division", command=lambda: calcular("divi")).pack()

tk.Button(frame3, text="guardar", command=guardar).pack(pady=5)

frame4 = tk.LabelFrame(ventana, text="historial")
frame4.pack(padx=10, pady=10)

historial = tk.Label(frame4, text= "historial de operaciones: ", justify="left")
historial.pack()

ventana.mainloop()