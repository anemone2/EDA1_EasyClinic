import tkinter as tk
import funciones_interfaz
from tkinter import ttk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import idioma_esp as lenguaje # Importa español como predeterminado

textos = lenguaje.textos

# ventana principal---------------------------------------------------------------------
ventana = tk.Tk()
ventana.title("Sistema de Inicio de Sesión")
ventana.geometry("1200x720") 
ventana.config(cursor='@imagenes/cursorJeringa.cur')
# Iniciar partículas
condicion_modo_oscuro = True
canvas_fondo = funciones_interfaz.iniciar_particulas(ventana, condicion_modo_oscuro)
# Enviar el canvas al fondo
ventana.lower(canvas_fondo)


def alternar_modo_oscuro():
    global condicion_modo_oscuro, canvas_fondo
    # Cambiar el estado de la variable
    condicion_modo_oscuro = not condicion_modo_oscuro
    # Eliminar el canvas anterior
    canvas_fondo.destroy()
    # Reiniciar las partículas con el nuevo modo
    canvas_fondo = funciones_interfaz.iniciar_particulas(ventana, condicion_modo_oscuro)
    ventana.lower(canvas_fondo)

    # Cambiar el fondo de la ventana
    if condicion_modo_oscuro:
        color_fondo = "black"
        color_letra = "white"
        color_boton = "#333333"
        color_boton_activo = "#444444"
    else:
        color_fondo = "#121212"
        color_letra = "black"
        color_boton = "#E0F7FA"
        color_boton_activo = "#B2EBF2"

    ventana.config(bg=color_fondo)

    #Actualizar los estilos
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("boton_salir.TButton", 
                    font=("Arial", 12), 
                    padding=6,
                    foreground=color_letra, 
                    background="red")
    style.map("boton_salir.TButton",
              background=[("active", "dark red")])

    style.configure("estilo_principal.TButton",
                    font=("Arial", 16),
                    foreground=color_letra, 
                    background=color_boton,
                    borderwidth=1,
                    focusthickness=3,
                    focuscolor="none",
                    padding=(13,9))
    style.map("estilo_principal.TButton",
              background=[("active", color_boton_activo)],
              relief=[("pressed", "sunken"), ("!pressed", "raised")])

    style.configure("botones_chicos.TButton",
                    font=("Arial", 16),
                    foreground=color_letra, 
                    background=color_boton,
                    borderwidth=1,
                    focusthickness=3,
                    focuscolor="none",
                    padding=(9,6))
    style.map("botones_chicos.TButton",
              background=[("active", color_boton_activo)],
              relief=[("pressed", "sunken"), ("!pressed", "raised")])

    menuPrincipal()

# Menú principal-------------------------------------------------------------------------
def menuPrincipal():
    # Limpiar la ventana
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)
    
    # Título
    titulo = tk.Label(ventana, text=textos["bienvenida"], font=("Arial", 24, "bold"))
    titulo.pack(pady=70)
    
    # Botón de inicio de sesión como paciente
    boton_paciente = ttk.Button(ventana, text=textos["inicio_sesion_paciente"], style="estilo_principal.TButton", command=lambda: mostrar_formulario("Paciente"), width=30)
    boton_paciente.pack(pady=20)
    
    # Botón de inicio de sesión como administrador
    boton_admin = ttk.Button(ventana, text=textos["inicio_sesion_administrados"], style="estilo_principal.TButton", command=lambda: mostrar_formulario("Administrador"), width=30)
    boton_admin.pack(pady=20)
    
    #Boton para cambiar idioma
    boton_cambiar_idioma = ttk.Button(ventana, text=textos["cambiar_idioma"], style="botones_chicos.TButton", command=mostrar_opciones_idioma)
    boton_cambiar_idioma.place(x=50, y=200)
    boton_salir = ttk.Button(ventana, text=textos["salir"], style="boton_salir.TButton", command=ventana.destroy)
    boton_salir.place(x=1050, y=650)

    ventana.imagen_modo = tk.PhotoImage(file="imagenes/imagen_modo.png").subsample(10, 10)
    boton_imagen = tk.Button(
        ventana,
        image=ventana.imagen_modo,
        command=alternar_modo_oscuro,
        borderwidth=0,
        highlightthickness=0,
        bg=ventana["bg"],
        activebackground=ventana["bg"]
    )
    boton_imagen.place(x=1050, y=20)

#Cambio de idioma----------------------------------------------------------------------------------------------------------
def cambiar_idioma(idioma): #la variable que entra sera el idioma al que se va a cambiar
    global textos
    if idioma == "ingles":
        import idioma_ingles as lenguaje #se importa el .py con el diccionario de palabras en ese idioma y se le llama con el alia lenguaje
    elif idioma == "frances":
        import idioma_frances as lenguaje
    elif idioma == "portugues":
        import idioma_portugues as lenguaje
    elif idioma == "aleman":
        import idioma_aleman as lenguaje
    elif idioma == "italiano":
        import idioma_italiano as lenguaje
    elif idioma == "chino":
        import idioma_chino as lenguaje
    elif idioma == "japones":
        import idioma_japones as lenguaje
    else:
        import idioma_esp as lenguaje #si no es ninguno de los idiomas anteriores se importa el espaniol
    textos = lenguaje.textos #se guarda en la variable global textos el diccionario de el idioma seleccionado
    menuPrincipal() #se vuelve a llamar al menu para actualizar el idioma
    
def mostrar_opciones_idioma():
    # Si ya se abrió antes, se borra para no duplicar
    if hasattr(ventana, "frame_opciones_idioma"):
        ventana.frame_opciones_idioma.destroy()

    #Crea el marco que contiene los botones de idiomas
    ventana.frame_opciones_idioma = tk.Frame(ventana, bg="white", bd=1, relief="solid")
    ventana.frame_opciones_idioma.place(x=50, y=250)

    #Crea un botón por idioma, uno a uno
    btn_esp = ttk.Button(ventana.frame_opciones_idioma, text=textos["espaniol"], style="botones_chicos.TButton", command=lambda: cambiar_idioma("esp"))
    btn_esp.pack(fill="x", padx=5, pady=2)

    btn_ing = ttk.Button(ventana.frame_opciones_idioma, text=textos["ingles"], style="botones_chicos.TButton", command=lambda: cambiar_idioma("ingles"))
    btn_ing.pack(fill="x", padx=5, pady=2)

    btn_fra = ttk.Button(ventana.frame_opciones_idioma, text=textos["frances"], style="botones_chicos.TButton", command=lambda: cambiar_idioma("frances"))
    btn_fra.pack(fill="x", padx=5, pady=2)

    btn_por = ttk.Button(ventana.frame_opciones_idioma, text=textos["portugues"], style="botones_chicos.TButton", command=lambda: cambiar_idioma("portugues"))
    btn_por.pack(fill="x", padx=5, pady=2)

    btn_ale = ttk.Button(ventana.frame_opciones_idioma, text=textos["aleman"], style="botones_chicos.TButton", command=lambda: cambiar_idioma("aleman"))
    btn_ale.pack(fill="x", padx=5, pady=2)

    btn_ita = ttk.Button(ventana.frame_opciones_idioma, text=textos["italiano"], style="botones_chicos.TButton", command=lambda: cambiar_idioma("italiano"))
    btn_ita.pack(fill="x", padx=5, pady=2)

    btn_chi = ttk.Button(ventana.frame_opciones_idioma, text=textos["chino"], style="botones_chicos.TButton", command=lambda: cambiar_idioma("chino"))
    btn_chi.pack(fill="x", padx=5, pady=2)

    btn_jap = ttk.Button(ventana.frame_opciones_idioma, text=textos["japones"], style="botones_chicos.TButton", command=lambda: cambiar_idioma("japones"))
    btn_jap.pack(fill="x", padx=5, pady=2)

#Inicio de sesión----------------------------------------------------------------------------------------------------------
def mostrar_formulario(tipoUsuario):
    # Limpiar la ventana
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)

    # Título del formulario
    titulo_formulario = tk.Label(ventana, text=f"{textos["iniciar_sesion_como"]} {tipoUsuario}", font=("Arial", 24, "bold"))
    titulo_formulario.pack(pady=50)
    
    # Para ingresar el nombre
    lbl_nombre = tk.Label(ventana, text=textos["nombre"], font=("Arial", 16))
    lbl_nombre.pack(pady=10)
    ingresar_nombre = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_nombre.pack(pady=5)
    
    # Para ingresar el correo electrónicp
    lbl_correo = tk.Label(ventana, text=textos["correo_electronico"], font=("Arial", 16))
    lbl_correo.pack(pady=10)
    ingresar_correo = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_correo.pack(pady=5)
    
    ingresar_contrasena = None
    # Si es administrador, agregar espacio para la contraseña
    if tipoUsuario == "Administrador":
        lbl_contrasena = tk.Label(ventana, text=textos["contrasena"], font=("Arial", 16))
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
    
    boton_enviar = ttk.Button(ventana, text=textos["enviar"], style="botones_chicos.TButton", width=10, command=enviar_datos)
    boton_enviar.pack(pady=20)

    # Botón para colver al menú principal
    boton_regresar = ttk.Button(ventana, text=textos["regresar"], style="botones_chicos.TButton", width=10, command=menuPrincipal)
    boton_regresar.pack(pady=10)

#Interfaz del admin-----------------------------------------------------------------------------------------------------------
def interfazAdmin(nombre):
    #Limpiar la ventana
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)
    
    # Título centrado que ocupa dos columnas
    titulo = tk.Label(ventana, text=f"{textos["bienvenido"]} {nombre}", font=("Arial", 24, "bold"))
    titulo.pack(pady=50)
    
    boton_citas_registradas = ttk.Button(ventana, text=textos["citas_registradas"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_citas_registradas.pack(pady=20)
    
    boton_horarios = ttk.Button(ventana, text=textos["horarios"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_horarios.pack(pady=20)

    boton_registro_medico = ttk.Button(ventana, text=textos["registro_medico"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_registro_medico.pack(pady=20)

    boton_estadisticas = ttk.Button(ventana, text=textos["estadisticas"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_estadisticas.pack(pady=20)

    boton_historial_citas = ttk.Button(ventana, text=textos["historial_citas"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_historial_citas.pack(pady=20)
    
    # Botón para volver al menú principal
    boton_regresar = ttk.Button(ventana, text=textos["regresar"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
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
    
    boton_citas_registradas = ttk.Button(frame_izquierdo, text=textos["citas_registradas"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_citas_registradas.pack(pady=20)
    
    boton_horarios = ttk.Button(frame_izquierdo, text=textos["horarios"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_horarios.pack(pady=20)

    boton_registro_medico = ttk.Button(frame_izquierdo, text=textos["registro_medico"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_registro_medico.pack(pady=20)

    boton_estadisticas = ttk.Button(frame_izquierdo, text=textos["estadisticas"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_estadisticas.pack(pady=20)

    boton_historial_citas = ttk.Button(frame_izquierdo, text=textos["historial_citas"], style="estilo_principal.TButton", width=20, command=interfaz_admin_avanzada)
    boton_historial_citas.pack(pady=20)
    
    boton_cerrar_sesion = ttk.Button(frame_izquierdo, text=textos["cerrar_sesion"], style="estilo_principal.TButton", width=20, command=menuPrincipal)
    boton_cerrar_sesion.pack(pady=90)

    # Agregar contenido al frame derecho
    etiqueta = tk.Label(frame_derecho, text="....", font=("Arial", 24, "bold"), bg="#FFFFFF")
    etiqueta.pack(pady=30)


#Inferfaz del paciente----------------------------------------------------------------------------------------
def interfazPaciente(nombre):
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)
    
    titulo_formulario = tk.Label(ventana, text=f"{textos["bienvenido"]} {nombre}", font=("Arial", 24, "bold"))
    titulo_formulario.pack(pady=50)

    # Para ingresar la edad
    lbl_edad = tk.Label(ventana, text=textos["edad"], font=("Arial", 16))
    lbl_edad.pack(pady=10)
    ingresar_edad = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_edad.pack(pady=5)
    
    # Para ingresar el Sexo
    lbl_sexo = tk.Label(ventana, text=textos["sexo"], font=("Arial", 16))
    lbl_sexo.pack(pady=10)
    ingresar_sexo = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_sexo.pack(pady=5)
    
    # Para ingresar el peso
    lbl_peso = tk.Label(ventana, text=textos["peso"], font=("Arial", 16))
    lbl_peso.pack(pady=10)
    ingresar_peso = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_peso.pack(pady=5)
    
    # Para ingresar el motivo de la cita
    lbl_motivo = tk.Label(ventana, text=textos["motivo"], font=("Arial", 16))
    lbl_motivo.pack(pady=10)
    ingresar_motivo = tk.Entry(ventana, font=("Arial", 14), width=30)
    ingresar_motivo.pack(pady=5)
    
    # Para guardar los datos del paciente y luego pasar a la lista de médicos
    def guarda_continuar():
        #guarda los datos en las variables
        edad = ingresar_edad.get()
        sexo = ingresar_sexo.get()
        peso = ingresar_peso.get()
        motivo = ingresar_motivo.get()
        
        # Validaciones básicas de cada dato
        if not edad.isdigit() or int(edad) <= 0:
            messagebox.showerror(textos["error"], textos["error_edad"])
            return
        if not peso.replace(".", "", 1).isdigit() or float(peso) <= 0:
            messagebox.showerror(textos["error"], textos["error_peso"])
            return
        if sexo.lower() not in ["m", "f"]:
            messagebox.showerror(textos["error"], textos["error_sexo"])
            return
        if not motivo.strip():
            messagebox.showerror(textos["error"], textos["error_motivo"])
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
    boton_guarda_continuar = ttk.Button(frame_botones, text=textos["guarda_continuar"], style="estilo_principal.TButton", width=20, command=guarda_continuar)
    boton_guarda_continuar.pack(side="left", padx=20)

    # Botón para volver al menú principal
    boton_regresar = ttk.Button(frame_botones, text=textos["regresar"], style="estilo_principal.TButton", width=20, command=menuPrincipal)
    boton_regresar.pack(side="left", padx=20)

#Interfaz de doctores-----------------------------------------------------------------------------------------------------
def interfaz_lista_medicos():
    funciones_interfaz.limpiar_contenido(ventana, canvas_fondo)
    titulo_formulario = tk.Label(ventana, text=textos["lista_medicos"], font=("Arial", 20, "bold"))
    titulo_formulario.pack(pady=20)
    busqueda = tk.Label(ventana, text=textos["busqueda_medicos"], font=("Arial", 20, "bold"))
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
    ttk.Button(frame_contenedor, text=textos["ordenar_nombre"], style="estilo_principal.TButton", width=20).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(frame_contenedor, text=textos["ordenar_especialidad"], style="estilo_principal.TButton", width=20).grid(row=0, column=2, padx=5, pady=5)
    ttk.Button(frame_contenedor, text=textos["ordenar_precio"], style="estilo_principal.TButton", width=20).grid(row=0, column=3, padx=5, pady=5)
    # Encabezados dentro del frame_contenedor para que coincidan con los datos
    tk.Label(frame_contenedor, text=textos["foto"], font=("Arial", 14, "bold"), width=12).grid(row=1, column=0, padx=5, pady=5)
    tk.Label(frame_contenedor, text=textos["nombre"], font=("Arial", 14, "bold"), width=20).grid(row=1, column=1, padx=5, pady=5)
    tk.Label(frame_contenedor, text=textos["especialidad"], font=("Arial", 14, "bold"), width=20).grid(row=1, column=2, padx=5, pady=5)
    tk.Label(frame_contenedor, text=textos["precio"], font=("Arial", 14, "bold"), width=10).grid(row=1, column=3, padx=5, pady=5)
    tk.Label(frame_contenedor, text=textos["accion"], font=("Arial", 14, "bold"), width=12).grid(row=1, column=4, padx=5, pady=5)
    boton_salir = ttk.Button(ventana, text=textos["salir"], style="boton_salir.TButton", command=ventana.destroy)
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
        tk.Button(frame_contenedor, text=textos["seleccionar"], command=lambda m=medico: agendar_cita(m)).grid(row=i, column=4, padx=10)


# Mostrar al iniciar (Menu pricipal)-------------------------------------------------------------------------------
alternar_modo_oscuro()
# Ejecutar ventana
ventana.mainloop()
