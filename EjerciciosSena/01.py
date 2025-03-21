# 1.Una entidad otorga subsidios de vivienda a sus empleados siempre y cuando cumplan con ciertos criterios. 
# Si un empleado es de un estrato socio-económico menor al estrato  4 y tiene por lo menos 8 años de antigüedad 
# en la entidad, entonces el empleado tiene derecho a un subsidio de vivienda, de lo contrario, no. Teniendo en 
# cuenta las condiciones anteriores, cree en Javascript un programa que reciba por teclado el nombre del empleado, 
# luego, que reciba su estrato socio-económico (debe estar ubicado entre 1 y 6), después, que reciba por teclado 
# su antigüedad en años en la entidad y por último muestre si el empleado tiene derecho al subsidio o no, por ejemplo, 
# “Juan Pérez, usted no tiene derecho a subsidio de vivienda.

import tkinter as tk
from tkinter import messagebox

def enviar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    ciudad = entry_ciudad.get()
    profesion = entry_profesion.get()
    
    resumen = f"Nombre: {nombre}\nEdad: {edad}\nCiudad: {ciudad}\nProfesión: {profesion}"
    messagebox.showinfo("Datos ingresados", resumen)

    # Limpiar los campos de texto
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_ciudad.delete(0, tk.END)
    entry_profesion.delete(0, tk.END)

# Crear ventana
ventana = tk.Tk()
ventana.title("Formulario de preguntas")

# Etiquetas y campos
tk.Label(ventana, text="¿Cómo te llamas?").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="¿Cuántos años tienes?").grid(row=1, column=0, sticky="w")
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)

tk.Label(ventana, text="¿En qué ciudad vives?").grid(row=2, column=0, sticky="w")
entry_ciudad = tk.Entry(ventana)
entry_ciudad.grid(row=2, column=1)

tk.Label(ventana, text="¿Cuál es tu profesión?").grid(row=3, column=0, sticky="w")
entry_profesion = tk.Entry(ventana)
entry_profesion.grid(row=3, column=1)

# Botón para enviar
tk.Button(ventana, text="Enviar", command=enviar_datos).grid(row=4, columnspan=2, pady=10)

ventana.mainloop()


