import customtkinter as ctk
ventana = ctk.CTk()
ventana.geometry("700x700")

def leer():
    print(f"Hola, {campo.get()}")

campo = ctk.CTkEntry(ventana)
campo.pack()

boton = ctk.CTkButton(ventana, text="Leer", command=leer)
boton.pack()

ventana.mainloop()