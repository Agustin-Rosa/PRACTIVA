import customtkinter as ctk
ventana = ctk.CTk()
ventana.title("Mi primer ventana")
ventana.geometry("700x700")
texto = ctk.CTkLabel(ventana, text="Hola, soy un texto")
texto.pack() 



def cambiar():
    texto.configure(text="¡Me apretaste!")

boton1= ctk.CTkButton(ventana,text="apretame pibe", command=cambiar)
boton1.pack()


ventana.mainloop()