import tkinter as tk
from tkinter import ttk
from datetime import datetime

historial = []

def guardar():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    tipo_usuario = combo_tipo_usuario.get()
    placa = entry_placa.get()
    tipo = entry_tipo.get()
    color = entry_color.get()
    puesto = combo_puesto.get()
    estado = combo_estado.get()

    fecha = datetime.now().strftime("%Y-%m-%d")

    hora_entrada = entry_hora_entrada.get()
    hora_salida = entry_hora_salida.get()

    datos = (cedula, nombre, placa, tipo_usuario, tipo, color, puesto, fecha, hora_entrada, hora_salida, estado)
    
    historial.append(datos)

    tabla.insert("", tk.END, values=datos)

    limpiar()

def limpiar():
    entry_cedula.delete(0, tk.END)
    entry_nombre.delete(0, tk.END) 
    entry_tipo_usuario.delete(0, tk.END) 
    entry_placa.delete(0, tk.END) 
    entry_tipo.delete(0, tk.END)
    entry_color.delete(0, tk.END)
    entry_puesto.delete(0, tk.END)
    entry_hora_entrada.delete(0, tk.END)
    entry_hora_salida.delete(0, tk.END)
    entry_estado.delete(0, tk.END)

def imprimir_historial():
    print("\n  historial de parqueadero: \n")
    for registro in historial:
        print(registro)

ventana = tk.Tk()
ventana.title(" Sistema de Parqueadero")
ventana.geometry("1200x600")
ventana.configure(bg="#2138aa")

style = ttk.Style()
style.theme_use("clam")

titulo = tk.Label(ventana, text= "Sistema de parqueadero", font=("arial", 20, "bold"), bg="#2c3e50", fg="white")
titulo.pack(pady=10)

frame = tk.Frame(ventana, bg= "#34495e")
frame.pack(pady=10, padx=20, fill="x")

tk.Label(frame, text= "Cedula:", bg="#34495e", fg="white").grid(row=0, column=0)
entry_cedula = tk.Entry(frame)
entry_cedula.grid(row=0, column=1)

tk.Label(frame, text= "Nombre:", bg="#34495e", fg="white").grid(row=1, column=0)
entry_nombre = tk.Entry(frame)
entry_nombre.grid(row=1, column=1)

tk.Label(frame, text= "Tipo de usuario:", bg="#34495e", fg="white").grid(row=2, column=0)
combo_tipo_usuario = ttk.Combobox(frame, values=["Administrador", "Cliente"])
entry_tipo_usuario = combo_tipo_usuario
combo_tipo_usuario.grid(row=2, column=1)

tk.Label(frame, text= "placa:", bg="#34495e", fg="white").grid(row=0, column=2)
entry_placa = tk.Entry(frame)
entry_placa.grid(row=0, column=3)

tk.Label(frame, text= "tipo Carro:", bg="#34495e", fg="white").grid(row=1, column=2)
entry_tipo = tk.Entry(frame)
entry_tipo.grid(row=1, column=3)

tk.Label(frame, text= "color:", bg="#34495e", fg="white").grid(row=2, column=2)
entry_color = tk.Entry(frame)
entry_color.grid(row=2, column=3)

puestos = ["A-01", "A-02", "B-01", "B-02", "C-01", "C-02", "D-01", "D-02", "E-01", "E-02"]

tk.Label(frame, text= "Puesto:", bg="#34495e", fg="white").grid(row=0, column=4)
combo_puesto = ttk.Combobox(frame, values=puestos)
entry_puesto = combo_puesto
combo_puesto.grid(row=0, column=5)

tk.Label(frame, text= "Hora entrada:", bg="#34495e", fg= "white").grid(row=1, column=4)
entry_hora_entrada = tk.Entry(frame)
entry_hora_entrada.grid(row=1, column=5)

tk.Label(frame, text= "Hora salida:", bg="#34495e", fg="white").grid(row=2, column=4)
entry_hora_salida = tk.Entry(frame)
entry_hora_salida.grid(row=2, column=5)

tk.Label(frame, text="Estado:", bg="#34495e", fg="white").grid(row=3, column=0)
combo_estado = ttk.Combobox(frame, values=["Entrada", "Salida"])
entry_estado = combo_estado
combo_estado.grid(row=3, column=1)

btn_guardar = tk.Button(frame, text= "Guardar", bg="#27ae60", fg="white", width=15, command=guardar)
btn_guardar.grid(row=3, column=2, pady=10)

btn_imprimir = tk.Button(frame, text= "Imprimir historial", bg="#e74c3c", fg="white", width=18, command=imprimir_historial)
btn_imprimir.grid(row=3, column=3)

columnas = ("cedula","nombre","placa", "tipo Usuario", "tipo carro", "color", "puesto", "fecha", "hora entrada", "hora salida", "estado")

tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

tabla.pack(fill="both", expand=True, padx=20, pady=20)

ventana.mainloop()