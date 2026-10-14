import customtkinter as ctk
ventana = ctk.CTk()
ventana.geometry("700x700")

def verificar():
    if campo_usuario.get() == "admin" and campo_clave.get() == "321":
        mensaje.configure(text="Bienvenido")
    else:
        mensaje.configure(text="Usuario o contraseña incorrectos")

texto_usuario = ctk.CTkLabel(ventana, text="Usuario:")
texto_usuario.pack()
campo_usuario = ctk.CTkEntry(ventana)
campo_usuario.pack()

texto_clave = ctk.CTkLabel(ventana, text="Contraseña:")
texto_clave.pack()
campo_clave = ctk.CTkEntry(ventana, show="*")
campo_clave.pack()

boton = ctk.CTkButton(ventana, text="Ingresar", command=verificar)
boton.pack()

mensaje = ctk.CTkLabel(ventana, text="")
mensaje.pack()

ventana.mainloop()