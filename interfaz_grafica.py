import tkinter as tk
import funciones_interfaz
from tkinter import ttk
import tkinter.messagebox as messagebox

# ventana principal---------------------------------------------------------------------
ventana = tk.Tk()
ventana.title("Sistema de Inicio de Sesión")
ventana.geometry("1200x720") 
ventana.config(cursor='@imagenes/cursorJeringa.cur')
# Iniciar partículas
canvas_fondo = funciones_interfaz.iniciar_particulas(ventana)
# Enviar el canvas al fondo
ventana.lower(canvas_fondo)


#estilos---------------------------------------------------------------------------------
style = ttk.Style()
style.theme_use("clam")  # clam, alt, default, classic

style.configure("boton_salir.TButton", 
                font=("Arial", 12), 
                padding=6,
                foreground="black", 
                background="red")
style.map("boton_salir.TButton",
          background=[("active", "dark red")])

style.configure("estilo_principal.TButton",
                font=("Arial", 16),
                foreground="black", 
                background="#E0F7FA",
                borderwidth=1,
                focusthickness=3,
                focuscolor="none",
                padding=(13,9))
style.map("estilo_principal.TButton",
          background=[("active", "#B2EBF2")],          
          relief=[("pressed", "sunken"), ("!pressed", "raised")])

style.configure("botones_chicos.TButton",
                font=("Arial", 16),
                foreground="black", 
                background="#E0F7FA",
                borderwidth=1,
                focusthickness=3,
                focuscolor="none",
                padding=(9,6))
style.map("botones_chicos.TButton",
          background=[("active", "#B2EBF2")],      
          relief=[("pressed", "sunken"), ("!pressed", "raised")])
#----------------------------------------------------------------------------------------

# Menú principal-------------------------------------------------------------------------
def menuPrincipal():
    # Limpiar la ventana
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)
    
    # Título
    titulo = tk.Label(ventana, text="Bienvenido al Sistema", font=("Arial", 24, "bold"))
    titulo.pack(pady=70)
    
    # Botón de inicio de sesión como paciente
    boton_paciente = ttk.Button(ventana, text="Iniciar sesión como Paciente", style="estilo_principal.TButton", command=lambda: mostrar_formulario("Paciente"), width=30)
    boton_paciente.pack(pady=20)
    
    # Botón de inicio de sesión como administrador
    boton_admin = ttk.Button(ventana, text="Iniciar sesión como Administrador", style="estilo_principal.TButton", command=lambda: mostrar_formulario("Administrador"), width=30)
    boton_admin.pack(pady=20)

    boton_salir = ttk.Button(ventana, text="Salir", style="boton_salir.TButton", command=ventana.destroy)
    boton_salir.place(x=1050, y=650)

    tk.Button(ventana, command=funciones_interfaz.cumbion, bg=ventana['bg'], activebackground=ventana['bg'], bd=0, highlightthickness=0).place(relx=1.0, x=0, y=0, anchor="ne", width=20, height=20)



#Inicio de sesión----------------------------------------------------------------------------------------------------------
def mostrar_formulario(tipoUsuario):
    # Limpiar la ventana
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)

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
        exito, mensaje = funciones_interfaz.inicioDeSesion(tipoUsuario, nombre, correo, contrasena)
        
        print(f"Validación: {exito}, Mensaje: {mensaje}") #guiarse en la terminal

        if exito:
            if tipoUsuario == "Paciente":
                print("Abriendo interfaz de paciente...")  
                interfazPaciente(nombre)
            elif tipoUsuario == "Administrador":
                print("Abriendo interfaz de administrador...")  
                interfazAdmin(nombre)
        else:
            # Mostrar error
            lbl_resultado = tk.Label(ventana, text=mensaje, font=("Arial", 14), fg="red")
            lbl_resultado.pack(pady=10)
    
    boton_enviar = ttk.Button(ventana, text="Enviar", style="botones_chicos.TButton", width=10, command=enviar_datos)
    boton_enviar.pack(pady=20)

    # Botón para colver al menú principal
    boton_regresar = ttk.Button(ventana, text="Regresar", style="botones_chicos.TButton", width=10, command=menuPrincipal)
    boton_regresar.pack(pady=10)

#Interfaz del admin-----------------------------------------------------------------------------------------------------------
def interfazAdmin(nombre):
    #Limpiar la ventana
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)
    
    # Título centrado que ocupa dos columnas
    titulo = tk.Label(ventana, text=f"Bienvenido, {nombre}", font=("Arial", 24, "bold"))
    titulo.pack(pady=50)
    
    boton_citas_registradas = ttk.Button(ventana, text="Citas registradas", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_citas_registradas.pack(pady=20)
    
    boton_horarios = ttk.Button(ventana, text="Horarios", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_horarios.pack(pady=20)

    boton_registro_medico = ttk.Button(ventana, text="Registro médico", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_registro_medico.pack(pady=20)

    boton_estadisticas = ttk.Button(ventana, text="Estadísticas", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_estadisticas.pack(pady=20)

    boton_historial_citas = ttk.Button(ventana, text="Historial de citas", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_historial_citas.pack(pady=20)
    
    # Botón para volver al menú principal
    boton_regresar = ttk.Button(ventana, text="Regresar", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_regresar.pack(pady=50)

###def interfazAdmin_avanzada():
    #funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)
    #boton_salir = ttk.Button(ventana, text="Salir", style="boton_salir.TButton", command=ventana.destroy)
    #boton_salir.place(x=1050, y=650)

def interfaz_admin_avanzada():
    #Limpiar la ventana
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)
    
    # Configurar el layout en dos columnas:
    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=3)
    ventana.rowconfigure(0, weight=1)
    
    # Crear el frame izquierdo para los botones (1/4 del ancho)
    frame_izquierdo = tk.Frame(ventana, bg="#E0E0E0")
    frame_izquierdo.grid(row=0, column=0, sticky="nsew")
    
    # Crear el frame derecho para el contenido (3/4 del ancho)
    frame_derecho = tk.Frame(ventana, bg="#FFFFFF")
    frame_derecho.grid(row=0, column=1, sticky="nsew")
    
    # Agregar botones al frame izquierdo
    

    boton_citas_registradas = ttk.Button(frame_izquierdo, text="Citas registradas", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_citas_registradas.pack(pady=20)
    
    boton_horarios = ttk.Button(frame_izquierdo, text="Horarios", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_horarios.pack(pady=20)

    boton_registro_medico = ttk.Button(frame_izquierdo, text="Registro médico", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_registro_medico.pack(pady=20)

    boton_estadisticas = ttk.Button(frame_izquierdo, text="Estadísticas", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_estadisticas.pack(pady=20)

    boton_historial_citas = ttk.Button(frame_izquierdo, text="Historial de citas", style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_historial_citas.pack(pady=20)
    
    boton_cerrar_sesion = ttk.Button(frame_izquierdo, text="Cerrar sesión", style="estilo_principal.TButton", width=20, command=menuPrincipal)
    boton_cerrar_sesion.pack(pady=90)

    # Agregar contenido al frame derecho
    etiqueta = tk.Label(frame_derecho, text="....", font=("Arial", 24, "bold"), bg="#FFFFFF")
    etiqueta.pack(pady=30)


#Inferfaz del paciente----------------------------------------------------------------------------------------
def interfazPaciente(nombre):
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)
    
    titulo_formulario = tk.Label(ventana, text=f"Bienvenido, {nombre}", font=("Arial", 24, "bold"))
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
    boton_guarda_continuar = ttk.Button(frame_botones, text="Guarda y continuar", style="estilo_principal.TButton", width=20, command=guarda_continuar)
    boton_guarda_continuar.pack(side="left", padx=20)

    # Botón para volver al menú principal
    boton_regresar = ttk.Button(frame_botones, text="Regresar", style="estilo_principal.TButton", width=20, command=menuPrincipal)
    boton_regresar.pack(side="left", padx=20)

#Interfaz de doctores-----------------------------------------------------------------------------------------------------
def interfaz_lista_medicos():
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)
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
        {"nombre": "Dra. Meredith Grey", "especialidad": "Cirugía general", "precio": "3000", "foto": "imagenes/meredith_grey.png"},
        {"nombre": "Dr. Derek Shepherd", "especialidad": "Neurocirugía", "precio": "5000", "foto": "imagenes/derek_shepard.png"},
        {"nombre": "Dr. Gregory House", "especialidad": "Diagnostico", "precio": "6000", "foto": "imagenes/gregory_house.png"},
        {"nombre": "Dra. Cristina Yang", "especialidad": "Cirugía cardiotorácica", "precio": "4000", "foto": "imagenes/cristina_yang.png"},
        {"nombre": "Dr. Shaun Murphy", "especialidad": "Cirugía general", "precio": "2000", "foto": "imagenes/shaun_murphy.png"},
        {"nombre": "Dra. Addison Montgomery", "especialidad": "Obstetricia / Neonatal", "precio": "4000", "foto": "imagenes/addison_montgomery.png"},
        {"nombre": "Dr. Richard Webber", "especialidad": "Cirugía general", "precio": "3500", "foto": "imagenes/richard_webber.png"},
        {"nombre": "Dr. Jackson Avery", "especialidad": "Cirugía plastica / Otorrino", "precio": "3500", "foto": "imagenes/jackson_every.png"},
        {"nombre": "Dra. Miranda Bailey", "especialidad": "Cirugía general", "precio": "2500", "foto": "imagenes/miranda_bailey.png"},
        {"nombre": "Dr. Alex Karev", "especialidad": "Cirugía pediátrica", "precio": "2500", "foto": "imagenes/alex_karev.png"},
        {"nombre": "Dr. James Wilson", "especialidad": "Oncología", "precio": "2500", "foto": "imagenes/james_wilson.png"},
        {"nombre": "Dra. Jo Wilson", "especialidad": "Cirugía general", "precio": "1200", "foto": "imagenes/jo_wilson.png"},
    ]
    
    # Asociar la lista a la ventana principal
    ventana.imagenes_cargadas = []
    
    #botones para ordenar lalista
    ttk.Button(frame_contenedor, text="Ordenar por nombre", style="estilo_principal.TButton", width=20).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(frame_contenedor, text="Ordenar por especialidad", style="estilo_principal.TButton", width=20).grid(row=0, column=2, padx=5, pady=5)
    ttk.Button(frame_contenedor, text="Ordenar por precio", style="estilo_principal.TButton", width=20).grid(row=0, column=3, padx=5, pady=5)
    # Encabezados dentro del frame_contenedor para que coincidan con los datos
    tk.Label(frame_contenedor, text="Foto", font=("Arial", 14, "bold"), width=12).grid(row=1, column=0, padx=5, pady=5)
    tk.Label(frame_contenedor, text="Nombre", font=("Arial", 14, "bold"), width=20).grid(row=1, column=1, padx=5, pady=5)
    tk.Label(frame_contenedor, text="Especialidad", font=("Arial", 14, "bold"), width=20).grid(row=1, column=2, padx=5, pady=5)
    tk.Label(frame_contenedor, text="Precio (MXN)", font=("Arial", 14, "bold"), width=10).grid(row=1, column=3, padx=5, pady=5)
    tk.Label(frame_contenedor, text="Acción", font=("Arial", 14, "bold"), width=12).grid(row=1, column=4, padx=5, pady=5)
    boton_salir = ttk.Button(ventana, text="Salir", style="boton_salir.TButton", command=ventana.destroy)
    boton_salir.place(x=1050, y=30)

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


# Mostrar al iniciar (Menu pricipal)-------------------------------------------------------------------------------
menuPrincipal()
# Ejecutar ventana
ventana.mainloop()
