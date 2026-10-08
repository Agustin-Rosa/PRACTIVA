import customtkinter as ctk
ventana = ctk.CTk()
ventana.geometry("700x700")

def limpiar():
    for elemento in ventana.winfo_children():
        elemento.destroy()

ventana.mainloop()