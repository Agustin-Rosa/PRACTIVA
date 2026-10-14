import customtkinter as ctk
ventana = ctk.CTk()
ventana.geometry("700x700")

def limpiar():
    for elemento in ventana.winfo_children():
        elemento.destroy()

def pantalla_uno():
    limpiar()
    texto = ctk.CTkLabel(ventana, text="Soy la pantalla 1")
    texto.pack()
    boton1 = ctk.CTkButton(ventana, text="pasar a pantalla 2", command=pantalla_dos)
    boton1.pack()

def pantalla_dos():
    limpiar()
    texto = ctk.CTkLabel(ventana, text="Soy la pantalla 2")
    texto.pack()
    boton1 = ctk.CTkButton(ventana, text="volver", command=pantalla_uno)
    boton1.pack()

pantalla_uno()

ventana.mainloop()