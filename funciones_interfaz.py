import tkinter as tk
import random

def iniciar_particulas(ventana): #Funsión diseñada para recibir una ventana como parametro
    #De esta forma es más facil integrarla al archivo principal de interfaz
    #Asigno dimensiones a variables
    ancho = ventana.winfo_width() if ventana.winfo_width() > 1 else 1200
    alto = ventana.winfo_height() if ventana.winfo_height() > 1 else 720
    canvas = tk.Canvas(ventana, width=ancho, height=alto, highlightthickness=0) #Se crea un canvas y se elimina su margen por defecto
    canvas.place(x=0, y=0) #Se posiciona en (0,0)
    particulas = []
    for _ in range(100): #Genera 100 particulas, "_" se usa cuando no se usará ese valor
        x = random.randint(0, ancho) #Genera coordenadas aleatorias
        y = random.randint(0, alto) #Genera coordenadas aleatorias
        size = random.randint(3, 8) #variable de tamaño, uso size por evitar caracteres especiales
        particula_id = canvas.create_oval(x, y, x+size, y+size, fill="#B2EBF2", outline="") #Caracteristicas del ovalo creado
        vx = random.uniform(-2, 2) #variable de velocidad
        vy = random.uniform(-2, 2) #variable de velocidad
        particulas.append({"id": particula_id, "vx": vx, "vy": vy}) #Guarda un diccionario de la particla en la lista "particulas"
    def actualizar_particulas():
        for p in particulas: #recorre toda la lista accediento al diccionario de cada particula hasta terminar la lista
            canvas.move(p["id"], p["vx"], p["vy"]) #indica el movimiento de las figuras, p[""] es la forma de accedes al dato del diccionario
            coords = canvas.coords(p["id"]) #obtiene las coordenadas "x, y, x+size, y+size"
            if coords[2] < 0: #Si salio por la izquierda
                canvas.move(p["id"], ancho, 0) #se mueve a la derecha
            elif coords[0] > ancho: #Si salio por la derecha
                canvas.move(p["id"], -ancho, 0) #Se mueve a la izquierda
            if coords[3] < 0: #Si salió por arriba
                canvas.move(p["id"], 0, alto) #se mueve a abajo
            elif coords[1] > alto: #Si salió por abajo
                canvas.move(p["id"], 0, -alto) #Se mueve a arriba
        ventana.after(50, actualizar_particulas)
    actualizar_particulas()
    return canvas #Regresa el canvas para ser utilizado

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

def limpiar_contenido(ventana, canvas_fondo):
    for widget in ventana.winfo_children():
        if widget != canvas_fondo:
            widget.destroy()
