#Interfaz grafica
from inicioDeSesion import inicioDeSesion
import tkinter as tk
import tkinter.messagebox as messagebox

# Menú principal
def menuPrincipal():
    # Limpiar la ventana
    for widget in ventana.winfo_children():
        widget.destroy()
    
    # Título
    titulo = tk.Label(ventana, text="Bienvenido al Sistema", font=("Arial", 24, "bold"))
    titulo.pack(pady=70)
    
    # Botón de inicio de sesión como paciente
    boton_paciente = tk.Button(ventana, text="Iniciar sesión como Paciente", font=("Arial", 16), width=30, command=lambda: mostrar_formulario("Paciente"))
    boton_paciente.pack(pady=20)
    
    # Botón de inicio de sesión como administrador
    boton_admin = tk.Button(ventana, text="Iniciar sesión como Administrador", font=("Arial", 16), width=30, command=lambda: mostrar_formulario("Administrador"))
    boton_admin.pack(pady=20)

def mostrar_formulario(tipoUsuario):
    # Limpiar la ventana
    for widget in ventana.winfo_children():
        widget.destroy()
    
    # Título del formulario
    titulo_formulario = tk.Label(ventana, text=f"Iniciar sesión como {tipoUsuario}", font=("Arial", 24, "bold"))
    titulo_formulario.pack(pady=50)
    
    # Para ingresar el nombre
    lbl_nombre = tk.Label(ventana, text="Nombre:", font=("Arial", 16))
    lbl_nombre.pack(pady=10)
    ingresar_nombre = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_nombre.pack(pady=5)
    
    # Para ingresar el correo electrónicp
    lbl_correo = tk.Label(ventana, text="Correo Electrónico:", font=("Arial", 16))
    lbl_correo.pack(pady=10)
    ingresar_correo = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_correo.pack(pady=5)
    
    ingresar_contrasena = None
    # Si es administrador, agregar espacio para la contraseña
    if tipoUsuario == "Administrador":
        lbl_contrasena = tk.Label(ventana, text="Contraseña:", font=("Arial", 16))
        lbl_contrasena.pack(pady=10)
        ingresar_contrasena = tk.Entry(ventana, font=("Arial", 14), width=30, show="*")
        ingresar_contrasena.pack(pady=5)
    
    def enviar_datos():
        nombre = ingresar_nombre.get()
        correo = ingresar_correo.get()
        contrasena = ingresar_contrasena.get() if ingresar_contrasena else None
        exito, mensaje = inicioDeSesion(tipoUsuario, nombre, correo, contrasena)
        
        print(f"Validación: {exito}, Mensaje: {mensaje}") #guiarse en la terminal

        if exito:
            if tipoUsuario == "Paciente":
                print("Abriendo interfaz de paciente...")  
                interfazPaciente()
            elif tipoUsuario == "Administrador":
                print("Abriendo interfaz de administrador...")  
                interfazAdmin()
        else:
            # Mostrar error
            lbl_resultado = tk.Label(ventana, text=mensaje, font=("Arial", 14), fg="red")
            lbl_resultado.pack(pady=10)
    
    boton_enviar = tk.Button(ventana, text="Enviar", font=("Arial", 16), width=20, command=enviar_datos)
    boton_enviar.pack(pady=20)

    # Botón para colver al menú principal
    boton_regresar = tk.Button(ventana, text="Regresar", font=("Arial", 16), width=20, command=menuPrincipal)
    boton_regresar.pack(pady=10)

def interfazAdmin():
    for widget in ventana.winfo_children():
        widget.destroy()
    
    titulo_formulario = tk.Label(ventana, text="Por favor, ingrese sus datos para continuar", font=("Arial", 24, "bold"))
    titulo_formulario.pack(pady=50)

def interfazPaciente():
    for widget in ventana.winfo_children():
        widget.destroy()
    
    titulo_formulario = tk.Label(ventana, text="Por favor, ingrese sus datos para continuar", font=("Arial", 24, "bold"))
    titulo_formulario.pack(pady=50)

    # Para ingresar el nombre
    lbl_nombre = tk.Label(ventana, text="Nombre:", font=("Arial", 16))
    lbl_nombre.pack(pady=10)
    ingresar_nombre = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_nombre.pack(pady=5)

    # Para ingresar la edad
    lbl_edad = tk.Label(ventana, text="Edad:", font=("Arial", 16))
    lbl_edad.pack(pady=10)
    ingresar_edad = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_edad.pack(pady=5)
    
    # Para ingresar el Sexo
    lbl_sexo = tk.Label(ventana, text="Sexo (m o f):", font=("Arial", 16))
    lbl_sexo.pack(pady=10)
    ingresar_sexo = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_sexo.pack(pady=5)
    
    # Para ingresar el peso
    lbl_peso = tk.Label(ventana, text="Peso[kg]:", font=("Arial", 16))
    lbl_peso.pack(pady=10)
    ingresar_peso = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_peso.pack(pady=5)
    
    # Para ingresar el motivo de la cita
    lbl_motivo = tk.Label(ventana, text="Motivo de la cita:", font=("Arial", 16))
    lbl_motivo.pack(pady=10)
    ingresar_motivo = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_motivo.pack(pady=5)
    
    # Para guardar los datos del paciente y luego pasar a la lista de médicos
    def guarda_continuar():
        #guarda los datos en las variables
        nombre = ingresar_nombre.get()
        edad = ingresar_edad.get()
        sexo = ingresar_sexo.get()
        peso = ingresar_peso.get()
        motivo = ingresar_motivo.get()
        
        # Validaciones básicas de cada dato
        if not nombre.strip():
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return
        if not edad.isdigit() or int(edad) <= 0:
            messagebox.showerror("Error", "La edad debe ser un número positivo.")
            return
        if not peso.replace(".", "", 1).isdigit() or float(peso) <= 0:
            messagebox.showerror("Error", "El peso debe ser un número positivo.")
            return
        if sexo.lower() not in ["m", "f"]:
            messagebox.showerror("Error", "El sexo debe ser M o F.")
            return
        if not motivo.strip():
            messagebox.showerror("Error", "El motivo de la cita no puede estar vacío.")
            return

        # Si pasa todas las validaciones, guarda los datos
        paciente = {
            "nombre": nombre,
            "edad": edad,
            "sexo": sexo,
            "peso": peso,
            "motivo": motivo
        }
        #pasa a la interfaz de la lista de medicos
        interfaz_lista_medicos()
    
    #Para crear un frame y que los botones aparezcan uno alado del otro
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=20, anchor="center")
    
    # Para Guardar los datos y pasar a la lista de medicos
    boton_guarda_continuar = tk.Button(frame_botones, text="Guarda y continuar", font=("Arial", 16), width=20, command=guarda_continuar)
    boton_guarda_continuar.pack(side="left", padx=20)

    # Botón para volver al menú principal
    boton_regresar = tk.Button(frame_botones, text="Regresar", font=("Arial", 16), width=20, command=menuPrincipal)
    boton_regresar.pack(side="left", padx=20)

def interfaz_lista_medicos():
    for widget in ventana.winfo_children():
        widget.destroy()
    titulo_formulario = tk.Label(ventana, text="Lista de médicos", font=("Arial", 20, "bold"))
    titulo_formulario.pack(pady=20)
    busqueda = tk.Label(ventana, text="Busqueda de medicos", font=("Arial", 20, "bold"))
    busqueda.pack(pady=10)
    buscar_medico = tk.Entry(ventana, font=("Arial", 14), width=30)
    buscar_medico.pack(pady=10)

    
    #area scroleable
    canvas = tk.Canvas(ventana)
    scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)

    # Frame interno que contendrá los médicos
    frame_contenedor = tk.Frame(canvas)

    # Permite que el scroll se actualice automáticamente cuando cambia el tamaño del contenido
    frame_contenedor.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Incrustamos el frame dentro del canvas
    canvas.create_window((0, 0), window=frame_contenedor, anchor="n")

    # Configurar el canvas para que use el scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Empaquetamos
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    #lista De medicos
    medicos = [
        {"nombre": "Dra. Meredith Grey", "especialidad": "Cirugía general", "precio": "3000", "foto": "meredith_grey.png"},
        {"nombre": "Dr. Derek Shepherd", "especialidad": "Neurocirugía", "precio": "5000", "foto": "derek_shepard.png"},
        {"nombre": "Dr. Gregory House", "especialidad": "Diagnostico", "precio": "6000", "foto": "gregory_house.png"},
        {"nombre": "Dra. Cristina Yang", "especialidad": "Cirugía cardiotorácica", "precio": "4000", "foto": "cristina_yang.png"},
        {"nombre": "Dr. Shaun Murphy", "especialidad": "Cirugía general", "precio": "2000", "foto": "shaun_murphy.png"},
        {"nombre": "Dra. Addison Montgomery", "especialidad": "Obstetricia / Neonatal", "precio": "4000", "foto": "addison_montgomery.png"},
        {"nombre": "Dr. Richard Webber", "especialidad": "Cirugía general", "precio": "3500", "foto": "richard_webber.png"},
        {"nombre": "Dr. Jackson Avery", "especialidad": "Cirugía plastica / Otorrino", "precio": "3500", "foto": "jackson_every.png"},
        {"nombre": "Dra. Miranda Bailey", "especialidad": "Cirugía general", "precio": "2500", "foto": "miranda_bailey.png"},
        {"nombre": "Dr. Alex Karev", "especialidad": "Cirugía pediátrica", "precio": "2500", "foto": "alex_karev.png"},
        {"nombre": "Dr. James Wilson", "especialidad": "Oncología", "precio": "2500", "foto": "james_wilson.png"},
        {"nombre": "Dra. Jo Wilson", "especialidad": "Cirugía general", "precio": "1200", "foto": "jo_wilson.png"},
    ]
    
    # Asociar la lista a la ventana principal
    ventana.imagenes_cargadas = []
    
    #botones para ordenar lalista
    tk.Button(frame_contenedor, text="Ordenar por nombre", font=("Arial", 16), width=20).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame_contenedor, text="Ordenar por especialidad", font=("Arial", 16), width=20).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(frame_contenedor, text="Ordenar por precio", font=("Arial", 16), width=20).grid(row=0, column=3, padx=5, pady=5)
    # Encabezados dentro del frame_contenedor para que coincidan con los datos
    tk.Label(frame_contenedor, text="Foto", font=("Arial", 14, "bold"), width=12).grid(row=1, column=0, padx=5, pady=5)
    tk.Label(frame_contenedor, text="Nombre", font=("Arial", 14, "bold"), width=20).grid(row=1, column=1, padx=5, pady=5)
    tk.Label(frame_contenedor, text="Especialidad", font=("Arial", 14, "bold"), width=20).grid(row=1, column=2, padx=5, pady=5)
    tk.Label(frame_contenedor, text="Precio (MXN)", font=("Arial", 14, "bold"), width=10).grid(row=1, column=3, padx=5, pady=5)
    tk.Label(frame_contenedor, text="Acción", font=("Arial", 14, "bold"), width=12).grid(row=1, column=4, padx=5, pady=5)

    #mostrar lista de medicos
    for i, medico in enumerate(medicos, start = 2):
        try:
            img = tk.PhotoImage(file=medico["foto"]).subsample(7, 7)  # Reduce tamaño
        except:
            img = tk.PhotoImage(width=60, height=60)  # Imagen vacía si falla

        ventana.imagenes_cargadas.append(img)

        # Colocar datos en la fila i
        tk.Label(frame_contenedor, image=img, width=60, height=80).grid(row=i, column=0, padx=5, pady=5)
        tk.Label(frame_contenedor, text=medico["nombre"], font=("Arial", 12), width=20, anchor="w").grid(row=i, column=1)
        tk.Label(frame_contenedor, text=medico["especialidad"], font=("Arial", 12), width=20, anchor="w").grid(row=i, column=2)
        tk.Label(frame_contenedor, text=medico["precio"], font=("Arial", 12), width=10, anchor="w").grid(row=i, column=3)
        tk.Button(frame_contenedor, text="Seleccionar", command=lambda m=medico: agendar_cita(m)).grid(row=i, column=4, padx=10)

# ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Inicio de Sesión")
ventana.geometry("1200x720") 

# Mostrar al iniciar (Menu pricipal)
menuPrincipal()

# Ejecutar ventana
ventana.mainloop()
