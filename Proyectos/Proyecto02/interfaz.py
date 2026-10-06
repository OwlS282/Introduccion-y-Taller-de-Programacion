'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 12, Proyecto #2: Buscaminas

Fecha de entrega: 22/05/2026

'''
# Archivo: interfaz.py
# Descripción: Interfaz gráfica del juego Buscaminas
#              Maneja todas las ventanas y la interacción
#              con el usuario mediante Tkinter

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import os

from juego import Tablero
from puntajes import archiPuntajes

# Ruta base del proyecto para ubicar imagenes y archivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Ventana Principal, Menu de inicio del programa
class ventanaPrincipal:
    """
    Ventana de inicio del programa. Muestra el menu principal
    con opciones para iniciar partida, ver puntajes o salir.
    """

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("1200x800")
        self.ventana.resizable(False, False)
        self.ventana.title("Buscaminas - Menú Principal")

        # Cargar imagen de fondo
        imagen = Image.open(os.path.join(BASE_DIR, "MenuPrincipal.png"))
        imagen = imagen.resize((1200, 800))
        self.imagenFondo = ImageTk.PhotoImage(imagen)

        # Cargar logo del TEC
        logoImagen = Image.open(os.path.join(BASE_DIR, "LogoTEC.png"))
        logoImagen = logoImagen.resize((200, 200))
        self.logoTEC = ImageTk.PhotoImage(logoImagen)

        # Crear canvas para superponer imagen, logo y texto
        self.canvas = tk.Canvas(self.ventana, width=1200, height=800, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        # Colocar imagen de fondo, logo y textos en el canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagenFondo)
        self.canvas.create_image(950, 625, anchor="nw", image=self.logoTEC)
        self.canvas.create_text(600, 240, text="BUSCAMINAS", font=("Arial", 36, "bold"), fill="#FFFFFF")
        self.canvas.create_text(35, 710, text="Owel Jafet Gutiérrez Ortiz", font=("Arial", 16, "bold"), fill="#FFFFFF", anchor="nw")
        self.canvas.create_text(35, 740, text="2026800869", font=("Arial", 16, "bold"), fill="#FFFFFF", anchor="nw")

        # Boton de Nueva Partida
        botonNuevaPartida = tk.Button(
            self.ventana, text="Nueva Partida",
            bg="#002855", fg="#FFFFFF",
            font=("Arial", 16, "bold"),
            width=25, height=2,
            relief="flat", cursor="hand2",
            command=self.nuevaPartida
        )
        botonNuevaPartida.place(relx=0.5, rely=0.45, anchor="center")

        # Boton de Ver Puntajes
        botonVerPuntaje = tk.Button(
            self.ventana, text="Ver Puntajes",
            bg="#002855", fg="#FFFFFF",
            font=("Arial", 16, "bold"),
            width=25, height=2,
            relief="flat", cursor="hand2",
            command=self.verPuntaje
        )
        botonVerPuntaje.place(relx=0.5, rely=0.55, anchor="center")

        # Boton de Salir
        botonSalir = tk.Button(
            self.ventana, text="Salir",
            bg="#002855", fg="#FFFFFF",
            font=("Arial", 16, "bold"),
            width=25, height=2,
            relief="flat", cursor="hand2",
            command=self.salir
        )
        botonSalir.place(relx=0.5, rely=0.65, anchor="center")

    def nuevaPartida(self):
        # Abrir ventana de seleccion de dificultad
        ventanaSeleccionDificultad(self.ventana)

    def verPuntaje(self):
        # Abrir ventana de puntajes
        ventanaPuntajes(self.ventana)

    def salir(self):
        # Cerrar el programa
        self.ventana.destroy()


# Ventana Seleccion de Dificultad
class ventanaSeleccionDificultad:
    """
    Ventana para elegir el nivel de dificultad de la partida.
    Incluye niveles predefinidos y opción personalizada.
    """

    def __init__(self, ventana):
        self.ventanaPrincipal = ventana
        self.ventanaSeleccionDificultad = tk.Toplevel(ventana)
        self.ventanaSeleccionDificultad.title("Buscaminas - Seleccionar Dificultad")
        self.ventanaSeleccionDificultad.geometry("1200x800")
        self.ventanaSeleccionDificultad.resizable(False, False)

        # Cargar imagen de fondo
        imagen = Image.open(os.path.join(BASE_DIR, "SeleccionDificultad.png"))
        imagen = imagen.resize((1200, 800))
        self.imagenFondo = ImageTk.PhotoImage(imagen)

        # Cargar logo del TEC
        logoImagen = Image.open(os.path.join(BASE_DIR, "LogoTEC.png"))
        logoImagen = logoImagen.resize((200, 200))
        self.logoTEC = ImageTk.PhotoImage(logoImagen)

        # Crear canvas para superponer imagen, logo y texto
        self.canvas = tk.Canvas(self.ventanaSeleccionDificultad, width=1200, height=800, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        # Colocar imagen de fondo, logo y textos en el canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagenFondo)
        self.canvas.create_image(950, 625, anchor="nw", image=self.logoTEC)
        self.canvas.create_text(600, 160, text="SELECCIONAR DIFICULTAD", font=("Arial", 36, "bold"), fill="#FFFFFF")
        self.canvas.create_text(35, 710, text="Owel Jafet Gutiérrez Ortiz", font=("Arial", 16, "bold"), fill="#FFFFFF", anchor="nw")
        self.canvas.create_text(35, 740, text="2026800869", font=("Arial", 16, "bold"), fill="#FFFFFF", anchor="nw")

        # Boton de Dificultad Facil (8x8, 10 minas)
        botonFacil = tk.Button(
            self.ventanaSeleccionDificultad, text="Fácil",
            bg="#002855", fg="#FFFFFF",
            font=("Arial", 16, "bold"),
            width=25, height=2,
            relief="flat", cursor="hand2",
            command=lambda: self.elegirDificultad(8, 8, 10, "facil")
        )
        botonFacil.place(relx=0.5, rely=0.35, anchor="center")

        # Boton de Dificultad Medio (10x10, 15 minas)
        botonMedio = tk.Button(
            self.ventanaSeleccionDificultad, text="Medio",
            bg="#002855", fg="#FFFFFF",
            font=("Arial", 16, "bold"),
            width=25, height=2,
            relief="flat", cursor="hand2",
            command=lambda: self.elegirDificultad(10, 10, 15, "medio")
        )
        botonMedio.place(relx=0.5, rely=0.45, anchor="center")

        # Boton de Dificultad Dificil (12x12, 25 minas)
        botonDificil = tk.Button(
            self.ventanaSeleccionDificultad, text="Difícil",
            bg="#002855", fg="#FFFFFF",
            font=("Arial", 16, "bold"),
            width=25, height=2,
            relief="flat", cursor="hand2",
            command=lambda: self.elegirDificultad(12, 12, 25, "dificil")
        )
        botonDificil.place(relx=0.5, rely=0.55, anchor="center")

        # Boton de Dificultad Experto (15x15, 40 minas)
        botonExperto = tk.Button(
            self.ventanaSeleccionDificultad, text="Experto",
            bg="#002855", fg="#FFFFFF",
            font=("Arial", 16, "bold"),
            width=25, height=2,
            relief="flat", cursor="hand2",
            command=lambda: self.elegirDificultad(15, 15, 40, "experto")
        )
        botonExperto.place(relx=0.5, rely=0.65, anchor="center")

        # Boton de Dificultad Personalizado
        botonPersonalizado = tk.Button(
            self.ventanaSeleccionDificultad, text="Personalizado",
            bg="#002855", fg="#FFFFFF",
            font=("Arial", 16, "bold"),
            width=25, height=2,
            relief="flat", cursor="hand2",
            command=self.nivelPersonalizado
        )
        botonPersonalizado.place(relx=0.5, rely=0.75, anchor="center")

    def elegirDificultad(self, filas, columnas, minas, nivel):
        # Abrir tablero con la dificultad seleccionada y cerrar esta ventana
        ventanaTablero(self.ventanaPrincipal, filas, columnas, minas, nivel)
        self.ventanaSeleccionDificultad.destroy()

    def nivelPersonalizado(self):
        # Abrir ventana de configuracion personalizada
        self.ventanaSeleccionDificultadCustom = tk.Toplevel(self.ventanaSeleccionDificultad)
        self.ventanaSeleccionDificultadCustom.title("Buscaminas - Nivel Personalizado")
        self.ventanaSeleccionDificultadCustom.geometry("400x500")
        self.ventanaSeleccionDificultadCustom.resizable(False, False)
        self.ventanaSeleccionDificultadCustom.configure(bg="#002855")

        # Titulo
        tk.Label(
            self.ventanaSeleccionDificultadCustom,
            text="NIVEL PERSONALIZADO",
            font=("Arial", 20, "bold"),
            bg="#002855", fg="#FFFFFF"
        ).pack(pady=30)

        # Campo de Filas
        tk.Label(self.ventanaSeleccionDificultadCustom, text="Filas:", font=("Arial", 14, "bold"), bg="#002855", fg="#FFFFFF").pack()
        self.campoFilas = tk.Entry(self.ventanaSeleccionDificultadCustom, font=("Arial", 14), width=10, justify="center")
        self.campoFilas.pack(pady=10)

        # Campo de Columnas
        tk.Label(self.ventanaSeleccionDificultadCustom, text="Columnas:", font=("Arial", 14, "bold"), bg="#002855", fg="#FFFFFF").pack()
        self.campoColumnas = tk.Entry(self.ventanaSeleccionDificultadCustom, font=("Arial", 14), width=10, justify="center")
        self.campoColumnas.pack(pady=10)

        # Campo de Minas
        tk.Label(self.ventanaSeleccionDificultadCustom, text="Minas:", font=("Arial", 14, "bold"), bg="#002855", fg="#FFFFFF").pack()
        self.campoMinas = tk.Entry(self.ventanaSeleccionDificultadCustom, font=("Arial", 14), width=10, justify="center")
        self.campoMinas.pack(pady=10)

        # Boton de Jugar
        tk.Button(
            self.ventanaSeleccionDificultadCustom,
            text="Jugar",
            bg="#FFFFFF", fg="#002855",
            font=("Arial", 14, "bold"),
            width=15, height=2,
            relief="flat", cursor="hand2",
            command=self.iniciarPersonalizado
        ).pack(pady=30)

    def iniciarPersonalizado(self):
        # Leer y validar los valores ingresados por el usuario
        try:
            filas = int(self.campoFilas.get())
            columnas = int(self.campoColumnas.get())
            minas = int(self.campoMinas.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa solo numeros enteros", parent=self.ventanaSeleccionDificultadCustom)
            return

        # Validar dimensiones minimas (4x4)
        if filas < 4 or columnas < 4:
            messagebox.showerror("Error", "El tamaño mínimo permitido es de 4 filas y 4 columnas", parent=self.ventanaSeleccionDificultadCustom)
            return

        # Validar cantidad minima de minas
        if minas < 1:
            messagebox.showerror("Error", "Debe haber al menos 1 mina", parent=self.ventanaSeleccionDificultadCustom)
            return

        # Validar dimensiones maximas (25x25)
        if filas > 25 or columnas > 25:
            messagebox.showerror("Error", "El tamaño máximo permitido es de 25x25", parent=self.ventanaSeleccionDificultadCustom)
            return
        
        # Validar, sacamos la cantidad de minas posibles dependiendo de las dimensiones
        if filas == 4 and columnas == 4:
            minasMaximasPosibles = (filas * columnas) - 2
        else: 
            minasMaximasPosibles = (filas * columnas) - 10
        
        if minasMaximasPosibles <= 0:
            minasMaximasPosibles = (filas * columnas) - 2

        # Validar si el usuario superó el límite dinámico
        if minas > minasMaximasPosibles:
            messagebox.showerror("Error", f"Hay demasiadas minas para ese tablero, el máximo de minas permitido es {minasMaximasPosibles}", parent=self.ventanaSeleccionDificultadCustom)
            return

        # Abrir tablero con valores personalizados y cerrar ventanas
        ventanaTablero(self.ventanaPrincipal, filas, columnas, minas, "custom")
        self.ventanaSeleccionDificultadCustom.destroy()
        self.ventanaSeleccionDificultad.destroy()


# Ventana del Tablero de Juego principal
class ventanaTablero:
    """
    Ventana principal del juego. Muestra el tablero de botones,
    el temporizador, el contador de banderas y maneja toda
    la interacción del jugador durante la partida.
    """

    def __init__(self, ventana, filas, columnas, minas, nivel):
        self.ventanaTablero = tk.Toplevel(ventana)
        self.ventanaTablero.title("Buscaminas - Juego")
        self.ventanaTablero.geometry("1200x800")
        self.ventanaTablero.resizable(False, False)
        self.ventanaTablero.configure(bg="#002855")
        self.ventanaTablero.config(cursor="target")

        # Cargar imagenes de bomba y bandera
        imagenBomba = Image.open(os.path.join(BASE_DIR, "Bomba.png"))
        imagenBomba = imagenBomba.resize((20, 20), Image.NEAREST)
        self.fotoBomba = ImageTk.PhotoImage(imagenBomba)

        imagenBandera = Image.open(os.path.join(BASE_DIR, "Bandera.png"))
        imagenBandera = imagenBandera.resize((20, 20), Image.NEAREST)
        self.fotoBandera = ImageTk.PhotoImage(imagenBandera)

        # Inicializar logica del juego
        self.tablero = Tablero(filas, columnas, minas)
        self.botones = []
        self.segundos = 0

        # Atributos para reinicio
        self.ventanaPadre = ventana
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.nivel = nivel

        # Gestor de puntajes
        self.gestorPuntajes = archiPuntajes()

        # Frame de informacion superior
        self.frameInfo = tk.Frame(self.ventanaTablero, bg="#ffffff", pady=10)
        self.frameInfo.pack(fill="x")

        # Fila 1 Titulo y temporizador
        frameFila1 = tk.Frame(self.frameInfo, bg="#ffffff")
        frameFila1.pack(fill="x", padx=20)
        tk.Label(frameFila1, text="BUSCAMINAS", font=("Arial", 18, "bold"), bg="#ffffff", fg="#002855").pack(side="left")
        self.labelTimer = tk.Label(frameFila1, text="0 s", font=("Arial", 18, "bold"), bg="#ffffff", fg="#002855")
        self.labelTimer.pack(side="right")

        # Fila 2 Nivel y contador de banderas
        frameFila2 = tk.Frame(self.frameInfo, bg="#ffffff")
        frameFila2.pack(fill="x", padx=20)
        tk.Label(frameFila2, text=f"Nivel: {nivel.capitalize()}", font=("Arial", 14), bg="#ffffff", fg="#002855").pack(side="left")
        self.labelMinas = tk.Label(frameFila2, text=f"Banderas 0 / {minas}", font=("Arial", 14), bg="#ffffff", fg="#002855")
        self.labelMinas.pack(side="right")

        # Iniciar temporizador
        self.actualizarTimer()

        # Frame del tablero
        self.frameTablero = tk.Frame(self.ventanaTablero, bg="#002855")
        self.frameTablero.place(relx=0.5, rely=0.55, anchor="center")

        # Crear matriz de botones
        for celdaFilas in range(filas):
            filaBotones = []
            for celdaColumnas in range(columnas):
                boton = tk.Button(
                    self.frameTablero, text=" ",
                    width=3, height=1,
                    bg="LightSteelBlue2"
                )
                boton.grid(row=celdaFilas, column=celdaColumnas)
                boton.config(command=lambda fila=celdaFilas, columna=celdaColumnas: self.clickCelda(fila, columna))
                boton.bind("<Button-3>", lambda evento, f=celdaFilas, c=celdaColumnas: self.clickDerecho(f, c))
                filaBotones.append(boton)
            self.botones.append(filaBotones)

        #ver bombas
        for celdaFilas in range(filas):
            for celdaColumnas in range(columnas):
                if self.tablero.logica[celdaFilas][celdaColumnas] == -1:
                    self.botones[celdaFilas][celdaColumnas].config(bg='red')

    # Manejo de clicks del jugador
    def clickCelda(self, fila, columna):
        """
        Maneja el clic izquierdo revelar celda.
        """
        self.tablero.revelar(fila, columna)
        self.actualizarTablero()

        for celdaFilas in range(self.tablero.filas):
            for celdaColumnas in range(self.tablero.columnas):
                if self.tablero.logica[celdaFilas][celdaColumnas] == -1:
                    if self.tablero.visual[celdaFilas][celdaColumnas] == '?':
                        self.botones[celdaFilas][celdaColumnas].config(bg='red')

        # Victoria
        if self.tablero.ganado == True:
            self.bloquearTablero()
            messagebox.showinfo("Resultado", f"¡Ganaste! Tiempo: {self.segundos} segundos", parent=self.ventanaTablero)
            nombre = self.validarNombre()
            if nombre is not None:
                self.gestorPuntajes.guardarPuntajes(self.nivel, nombre, self.segundos)
            respuesta = messagebox.askquestion("Fin", "¿Querés jugar de nuevo con la misma dificultad?", parent=self.ventanaTablero)
            if respuesta == 'yes':
                self.reiniciar()
            else:
                self.ventanaTablero.destroy()

        # Derrota
        if self.tablero.juegoActivo == False and self.tablero.ganado == False:
            self.bloquearTablero()
            # Revelar todas las minas
            for celdaFilas in range(self.tablero.filas):
                for celdaColumnas in range(self.tablero.columnas):
                    boton = self.botones[celdaFilas][celdaColumnas]
                    if self.tablero.logica[celdaFilas][celdaColumnas] == -1:
                        boton.config(image=self.fotoBomba, text='', compound='center', width=25, height=20, bg="firebrick2")
                        boton.config(state='disabled')
            messagebox.showinfo("Resultado", f"¡Perdiste! Tiempo: {self.segundos} segundos", parent=self.ventanaTablero)
            respuesta = messagebox.askquestion("Fin", "¿Querés jugar de nuevo con la misma dificultad?", parent=self.ventanaTablero)
            if respuesta == 'yes':
                self.reiniciar()
            else:
                self.ventanaTablero.destroy()

    def clickDerecho(self, fila, columna):
        """
        Maneja el clic derecho de poner o quitar bandera.
        """
        if not self.tablero.juegoActivo:
            return

        self.tablero.ponerBanderas(fila, columna)

        # Actualizar contador de banderas
        banderasRestantes = self.tablero.minas - self.tablero.banderasColocadas
        self.labelMinas.config(text=f"Banderas: {banderasRestantes}/{self.tablero.minas}")

        # Actualizar visual del boton
        estadoCelda = self.tablero.visual[fila][columna]
        if estadoCelda == 'F':
            self.botones[fila][columna].config(image=self.fotoBandera, text='', compound='center', width=24, height=20, bg="gold2")
        if estadoCelda == '?':
            self.botones[fila][columna].config(image='', text=' ', width=3, height=1, bg="LightSteelBlue2")

    # Actualizacion de la interfaz
    def actualizarTablero(self):
        """
        Recorre la matriz visual y actualiza cada botón según su estado.
        """
        for celdaFilas in range(self.tablero.filas):
            for celdaColumnas in range(self.tablero.columnas):
                estadoCelda = self.tablero.visual[celdaFilas][celdaColumnas]
                boton = self.botones[celdaFilas][celdaColumnas]

                if estadoCelda == 'V':
                    valorCelda = self.tablero.logica[celdaFilas][celdaColumnas]

                    # Mina revelada
                    if valorCelda == -1:
                        boton.config(image=self.fotoBomba, text='', compound='center', width=25, height=20)

                    # Celda vacia
                    elif valorCelda == 0:
                        boton.config(text=' ', bg="wheat3")

                    # Celda con numero y sus colores
                    else:
                        colores = {
                            1: "#0000FF",  # azul
                            2: "#008000",  # verde
                            3: "#FF0000",  # rojo
                            4: "#000080",  # azul oscuro
                            5: "#800000",  # rojo oscuro
                            6: "#008080",  # teal
                            7: "#000000",  # negro
                            8: "#808080"   # gris
                        }
                        color = colores.get(valorCelda, "#000000")
                        boton.config(text=valorCelda, fg=color, bg="wheat2", disabledforeground=color)

                    boton.config(state='disabled')

                # Bandera colocada
                if estadoCelda == 'F':
                    boton.config(image=self.fotoBandera, text='', compound='center', width=25, height=20)

    def actualizarTimer(self):
        """
        Actualiza el temporizador cada segundo mientras el juego este activo.
        """
        if self.tablero.juegoActivo == True:
            self.segundos = self.segundos + 1
            self.labelTimer.config(text=f"{self.segundos}s")
            self.ventanaTablero.after(1000, self.actualizarTimer)

    def bloquearTablero(self):
        """
        Deshabilita todos los botones del tablero al terminar la partida.
        """
        for celdaFilas in range(self.tablero.filas):
            for celdaColumnas in range(self.tablero.columnas):
                self.botones[celdaFilas][celdaColumnas].config(state='disabled')

    # Validación de nombre y reinicio
    def validarNombre(self):
        """
        Solicita el nombre del jugador en un loop hasta que
        ingrese un nombre válido o cancele el diálogo.
        """
        while True:
            nombre = simpledialog.askstring("Registre su Nombre", "Ingrese un Nombre")
            if nombre == None:
                return None
            if nombre.strip() == "":
                messagebox.showerror("Error", "El nombre no puede estar vacío")
                continue
            return nombre

    def reiniciar(self):
        """
        Cierra el tablero actual y abre uno nuevo con la misma dificultad.
        """
        self.ventanaTablero.destroy()
        ventanaTablero(self.ventanaPadre, self.filas, self.columnas, self.minas, self.nivel)


# Ventana de Puntajes
class ventanaPuntajes:
    """
    Ventana que muestra los mejores puntajes por nivel
    organizados en pestañas usando ttk.Notebook.
    """

    def __init__(self, ventana):
        self.ventanaPuntajes = tk.Toplevel(ventana)
        self.ventanaPuntajes.title("Buscaminas - Puntajes")
        self.ventanaPuntajes.geometry("600x500")
        self.ventanaPuntajes.resizable(False, False)
        self.ventanaPuntajes.configure(bg="#002855")
        self.gestorPuntajes = archiPuntajes()

        # Título
        tk.Label(
            self.ventanaPuntajes,
            text="MEJORES PUNTAJES",
            font=("Arial", 24, "bold"),
            bg="#002855", fg="#FFFFFF"
        ).pack(pady=20)

        self.mostrarPuntajes()

    def mostrarPuntajes(self):
        """
        Crea las pestañas de puntajes por nivel y muestra los datos.
        """

        # Estilo de las pestañas
        style = ttk.Style()
        style.configure("TNotebook.Tab",
            font=("Arial", 12, "bold"),
            padding=[20, 10],
            foreground="#002855"
        )

        # Notebook con pestañas por nivel
        notebook = ttk.Notebook(self.ventanaPuntajes)
        notebook.pack(fill="both", expand=True, padx=20, pady=20)

        for nivel in ["facil", "medio", "dificil", "experto", "custom"]:

            # Frame de cada pestaña
            frameNivel = tk.Frame(notebook, bg="#002855")
            notebook.add(frameNivel, text=nivel.upper())

            # Configurar columnas para centrado
            frameNivel.columnconfigure(0, weight=1)
            frameNivel.columnconfigure(1, weight=1)
            frameNivel.columnconfigure(2, weight=1)

            # Encabezados de la tabla
            tk.Label(frameNivel, text="#", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#002855", width=5).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
            tk.Label(frameNivel, text="Nombre", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#002855", width=20).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
            tk.Label(frameNivel, text="Tiempo", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#002855", width=10).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

            # Obtener puntajes del nivel
            lista = self.gestorPuntajes.obtenerPuntajes(nivel)

            if len(lista) == 0:
                # Sin puntajes registrados
                tk.Label(frameNivel, text="Sin puntajes", font=("Arial", 12), bg="#002855", fg="#FFFFFF").grid(row=1, column=0, columnspan=3, pady=10)
            else:
                # Mostrar cada puntaje en su fila
                for posicion, puntaje in enumerate(lista):
                    tk.Label(frameNivel, text=posicion+1, font=("Arial", 12), bg="#002855", fg="#FFFFFF", width=5).grid(row=posicion+1, column=0, padx=5, pady=3)
                    tk.Label(frameNivel, text=puntaje['nombre'], font=("Arial", 12), bg="#002855", fg="#FFFFFF", width=20).grid(row=posicion+1, column=1, padx=5, pady=3)
                    tk.Label(frameNivel, text=f"{puntaje['tiempo']}s", font=("Arial", 12), bg="#002855", fg="#FFFFFF", width=10).grid(row=posicion+1, column=2, padx=5, pady=3)


# Punto de entrada del programa
if __name__ == "__main__":
    ventana = tk.Tk()
    app = ventanaPrincipal(ventana)
    ventana.mainloop()