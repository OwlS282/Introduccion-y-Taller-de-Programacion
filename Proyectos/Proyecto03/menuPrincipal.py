'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 19, Proyecto #3: SiembraTEC

Fecha de entrega: 29/06/2026

'''

import tkinter as tk
import tkinter.simpledialog as sd
import tkinter.messagebox as mb
import os

from jugador import Jugador
from terreno import Terreno
from guardado import cargarPartida
from ventanaJuego import VentanaJuego
from ventanaEstadisticas import VentanaEstadisticas
from PIL import Image, ImageTk

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class MenuPrincipal:
    """
    Ventana principal del juego SiembraTEC.
    Muestra el menú con opciones para iniciar una nueva partida,
    continuar una guardada, ver estadísticas o salir del juego.
    """

    def __init__(self):
        """
        Inicializa la ventana del menú principal con imagen de fondo,
        título del juego y botones de navegación con estilo retro.
        """
        self.ventana = tk.Tk()
        self.ventana.title("SiembraTEC")
        self.ventana.resizable(False, False)

        imagen = Image.open("fondo_menu.png").resize((800, 600))
        self.fondo = ImageTk.PhotoImage(imagen)

        self.canvas = tk.Canvas(self.ventana, width=800, height=600)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.fondo)

        self.canvas.create_text(400, 100, text="SiembraTEC",
            font=("Press Start 2P", 30, "bold"), fill="white")

        self.crearBoton("Nuevo Juego", 250, self.nuevoJuego)
        self.crearBoton("Continuar Partida", 320, self.continuarPartida)
        self.crearBoton("Estadísticas", 390, self.estadisticas)
        self.crearBoton("Salir", 460, self.salir)

        self.ventana.mainloop()

    def crearBoton(self, texto, y, comando):
        """
        Crea un botón con estilo retro sobre el canvas del menú.

        Args:
            texto (str): Texto que muestra el botón.
            y (int): Posición vertical del botón en el canvas.
            comando (function): Función que ejecuta el botón al ser presionado.
        """
        boton = tk.Button(self.ventana, text=texto, command=comando,
            font=("Press Start 2P", 10), bg="#8B6914", fg="white",
            width=20, relief="raised", bd=3)
        self.canvas.create_window(400, y, window=boton)

    def nuevoJuego(self):
        """
        Inicia una nueva partida solicitando el nombre del jugador.
        Si ya existe una partida guardada, pide confirmación para borrarla.
        Valida que el nombre sea válido antes de crear el jugador.
        """
        if os.path.exists("partida.json"):
            confirmacion = mb.askokcancel(
                "¡Atención!",
                "Ya tienes una partida guardada.\n¿Deseas borrarla y crear una nueva?"
            )
            if not confirmacion:
                return

        while True:
            nombre = sd.askstring("Nombre", "¿Cómo te llamas?")

            if nombre is None:
                return
            if not nombre.strip():
                mb.showerror("Error", "El nombre no puede estar vacío")
                continue
            if len(nombre) < 3:
                mb.showerror("Error", "El nombre debe tener al menos 3 caracteres")
                continue
            if not nombre.replace(" ", "").isalpha():
                mb.showerror("Error", "El nombre solo puede contener letras")
                continue
            break

        jugador = Jugador(nombre)
        terreno = Terreno(0)
        jugador.agregarTerreno(terreno)

        self.ventana.withdraw()
        VentanaJuego(jugador, self.ventana)

    def continuarPartida(self):
        """
        Carga y continúa una partida guardada previamente.
        Muestra error si no existe archivo de guardado.
        """
        if not os.path.exists("partida.json"):
            mb.showerror("Error", "No hay partida guardada")
            return
        jugador = cargarPartida()

        self.ventana.withdraw()
        VentanaJuego(jugador, self.ventana)

    def estadisticas(self):
        """
        Abre la ventana de estadísticas de la partida guardada.
        Evita abrir múltiples instancias de la misma ventana.
        Muestra error si no existe archivo de guardado.
        """
        if hasattr(self, 'statsAbierto') and self.statsAbierto:
            return
        if not os.path.exists("partida.json"):
            mb.showerror("Error", "No hay partida guardada")
            return
        self.statsAbierto = True
        jugador = cargarPartida()
        ventana = VentanaEstadisticas(self.ventana, jugador)
        ventana.ventana.protocol("WM_DELETE_WINDOW", lambda: self.cerrarVentana('statsAbierto', ventana))

    def cerrarVentana(self, atributo, ventana):
        """
        Cierra una ventana secundaria y marca su flag como cerrada.

        Args:
            atributo (str): Nombre del atributo booleano a poner en False.
            ventana: Objeto ventana con atributo .ventana de Tkinter.
        """
        setattr(self, atributo, False)
        ventana.ventana.destroy()

    def salir(self):
        """Cierra completamente la aplicación."""
        self.ventana.destroy()