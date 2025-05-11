#Inicio de sesión
from tkinter import messagebox
def inicioDeSesion(tipo_usuario, nombre, correo, contrasena=None):
    if not nombre.strip():
        messagebox.showerror("Error", "El nombre no puede estar vacío.")
        return False
    if "@" not in correo or "." not in correo:
        messagebox.showerror("Error", "El correo electrónico no es válido.")
        return False
    if tipo_usuario == "Administrador" and contrasena != "lafi69":
        messagebox.showerror("Error", "La contraseña es incorrecta.")
        return False
    return True, "Inicio de sesión exitoso."
