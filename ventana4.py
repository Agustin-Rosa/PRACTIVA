import customtkinter as ctk
ventana = ctk.CTk()
ventana.geometry("700x700")

def verificar():
    if campo.get() == "321":
        mensaje.configure(text="Correcto")
    else:
        mensaje.configure(text="Incorrecto")

campo = ctk.CTkEntry(ventana)
campo.pack()

boton = ctk.CTkButton(ventana, text="Verificar", command=verificar)
boton.pack()

mensaje = ctk.CTkLabel(ventana, text="")
mensaje.pack()

ventana.mainloop()