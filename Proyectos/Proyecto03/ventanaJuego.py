'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 19, Proyecto #3: SiembraTEC

Fecha de entrega: 29/06/2026

'''

import tkinter as tk
import tkinter.messagebox as mb
import time
import os

from ventanaTienda import VentanaTienda
from guardado import guardarPartida
from terreno import Terreno
from PIL import Image, ImageTk
from productos import Plantacion, Arbol
from ventanaInventario import VentanaInventario

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class VentanaJuego:
    """
    Ventana principal del juego SiembraTEC.
    Muestra el terreno de la granja con su grid de 15x15 celdas,
    el panel de información del jugador y los controles del juego.
    """

    def __init__(self, jugador, ventanaPadre):
        """
        Inicializa la ventana de juego.

        Args:
            jugador (Jugador): El objeto jugador con toda la información de la partida.
            ventanaPadre (tk.Tk): La ventana padre (menú principal).
        """
        self.jugador = jugador
        self.ventana = tk.Toplevel(ventanaPadre)
        self.ventana.title("SiembraTEC - Granja")
        self.ventana.geometry("1006x780")
        self.ventana.resizable(False, False)
        self.ventanaPadre = ventanaPadre

        self.frameTerreno = tk.Frame(self.ventana)
        self.frameTerreno.pack(side="left")

        self.framePanel = tk.Frame(self.ventana)
        self.framePanel.pack(side="right")

        self.terrenoActual = 0
        self.productoSeleccionado = None

        self.cargarImagenes()
        self.crearGrid()
        self.crearPanel()
        self.actualizarGrid()
        self.actualizarAutomatico()
        self.ventana.mainloop()

    def cargarImagenes(self):
        """
        Carga y precalcula todas las imágenes de los productos combinadas
        con sus fondos correspondientes (tierra o pasto).
        También carga la imagen de exclamación para productos listos.
        """
        self.imagenesRaw = {}
        tamaño = (48, 48)

        fondoTierra = Image.open("fondo_tierra.png").resize(tamaño).convert("RGBA")
        fondoPasto = Image.open("fondo_pasto.png").resize(tamaño).convert("RGBA")
        self.exclamacion = Image.open("exclamacion.png").resize((20, 20)).convert("RGBA")

        def combinar(fondo, archivo):
            """Combina un sprite con su fondo retornando una imagen PIL."""
            sprite = Image.open(archivo).resize(tamaño).convert("RGBA")
            resultado = fondo.copy()
            resultado.paste(sprite, (0, 0), sprite)
            return resultado

        for nombre in ["trigo", "maiz", "zanahoria", "tomate", "papa"]:
            self.imagenesRaw[nombre.capitalize()] = [
                combinar(fondoTierra, f"{nombre}_{numero}.png") for numero in range(1, 5)
            ]

        for nombre in ["gallina", "pato", "oveja", "cerdo", "vaca"]:
            self.imagenesRaw[nombre.capitalize()] = [
                combinar(fondoTierra, f"{nombre}_{numero}.png") for numero in range(1, 4)
            ]

        self.imagenesRaw["Lana"] = [
            combinar(fondoTierra, f"lvh_{numero}.png") for numero in range(1, 4)
        ]

        for nombre in ["manzano", "naranjo", "limonero", "cacaotero", "cafetal"]:
            self.imagenesRaw[nombre.capitalize()] = [
                combinar(fondoTierra, f"{nombre}_{numero}.png") for numero in range(1, 4)
            ]

        for nombre in ["banco", "estatua", "fuente", "molino"]:
            self.imagenesRaw[nombre.capitalize()] = [
                combinar(fondoPasto, f"{nombre}_1.png")
            ]

        self.imagenesRaw["Cerca"] = [combinar(fondoPasto, "cerca_1.png")]
        self.imagenesRaw["Banco"] = [combinar(fondoPasto, "banco_1.png")]

        self.imagenes = {}
        for nombre, frames in self.imagenesRaw.items():
            self.imagenes[nombre] = [ImageTk.PhotoImage(f) for f in frames]
        self.imagenes["pasto"] = [ImageTk.PhotoImage(fondoPasto)]
        self.frameActual = {}

    def combinarImagenes(self, nombreFondo, imagenSprite):
        """
        Combina una imagen de fondo con un sprite.

        Args:
            nombreFondo (str): Nombre del archivo de fondo sin extensión.
            imagenSprite (Image): Imagen PIL del sprite a superponer.

        Returns:
            ImageTk.PhotoImage: Imagen combinada lista para Tkinter.
        """
        fondo = Image.open(f"{nombreFondo}.png").resize((48, 48)).convert("RGBA")
        sprite = imagenSprite.convert("RGBA")
        fondo.paste(sprite, (0, 0), sprite)
        return ImageTk.PhotoImage(fondo)

    def agregarExclamacion(self, imagenRaw):
        """
        Superpone el signo de exclamación sobre una imagen PIL
        para indicar que el producto está listo para cosechar.

        Args:
            imagenRaw (Image): Imagen PIL base del producto.

        Returns:
            ImageTk.PhotoImage: Imagen con el signo de exclamación superpuesto.
        """
        resultado = imagenRaw.copy()
        resultado.paste(self.exclamacion, (28, 0), self.exclamacion)
        return ImageTk.PhotoImage(resultado)

    def crearGrid(self):
        """
        Crea el grid de botones de 15x15 que representa el terreno.
        Cada botón responde al clic izquierdo (colocar/cosechar)
        y al clic derecho (vender).
        """
        self.botonesCeldas = []

        for fila in range(15):
            filaBotones = []
            for columna in range(15):
                boton = tk.Button(
                    self.frameTerreno, width=48, height=48, bd=1, padx=0, pady=0,
                    command=lambda fila=fila, columna=columna: self.clickCelda(fila, columna)
                )
                boton.bind("<Button-3>", lambda evento, fila=fila, columna=columna: self.clickDerecho(fila, columna))
                boton.grid(row=fila, column=columna)
                filaBotones.append(boton)
            self.botonesCeldas.append(filaBotones)

        for fila in range(15):
            self.frameTerreno.rowconfigure(fila, minsize=48)
        for columna in range(15):
            self.frameTerreno.columnconfigure(columna, minsize=48)

    def crearPanel(self):
        """
        Crea el panel lateral de información del jugador con estilo retro.
        Incluye etiquetas de nombre, monedas, terrenos, producciones listas,
        tiempo jugado y botones de acción.
        """
        self.framePanel.destroy()
        self.ventana.update()
        altura = self.ventana.winfo_height()
        self.framePanel = tk.Canvas(
            self.ventana, width=220, height=altura,
            bg="#5C3317", highlightbackground="#DAA520", highlightthickness=3
        )
        self.framePanel.pack(side="right")

        fuente = ("Press Start 2P", 7)
        estilo = {"bg": "#5C3317", "fg": "#FFD700", "font": fuente}

        self.framePanel.create_text(110, 20, text="SiembraTEC", fill="#FFD700", font=("Press Start 2P", 8))
        self.framePanel.create_line(10, 35, 210, 35, fill="#DAA520", width=2)

        self.panelNombre = tk.StringVar()
        self.panelNombre.set(f"{self.jugador.getNombre()}")
        self.framePanel.create_window(110, 55, window=tk.Label(self.framePanel, textvariable=self.panelNombre, **estilo))

        self.panelMonedas = tk.StringVar()
        self.panelMonedas.set(f"{self.jugador.getMonedas()}")
        self.framePanel.create_window(110, 90, window=tk.Label(self.framePanel, textvariable=self.panelMonedas, **estilo))

        self.panelCantidadTerrenos = tk.StringVar()
        self.panelCantidadTerrenos.set(f"{self.jugador.getCantidadTerrenos()} terrenos")
        self.framePanel.create_window(110, 125, window=tk.Label(self.framePanel, textvariable=self.panelCantidadTerrenos, **estilo))

        self.panelProduccionesListas = tk.StringVar()
        self.panelProduccionesListas.set("Listos: 0")
        self.framePanel.create_window(110, 160, window=tk.Label(self.framePanel, textvariable=self.panelProduccionesListas, **estilo))

        self.panelTiempoTotalJuego = tk.StringVar()
        self.panelTiempoTotalJuego.set("0 seg")
        self.framePanel.create_window(110, 195, window=tk.Label(self.framePanel, textvariable=self.panelTiempoTotalJuego, **estilo))

        self.framePanel.create_line(10, 220, 210, 220, fill="#DAA520", width=2)

        estiloBoton = {"bg": "#8B6914", "fg": "#FFD700", "font": ("Press Start 2P", 7), "width": 14, "relief": "raised", "bd": 2}
        self.framePanel.create_window(110, 255, window=tk.Button(self.framePanel, text="Inventario", command=self.abrirInventario, **estiloBoton))
        self.framePanel.create_window(110, 305, window=tk.Button(self.framePanel, text="Tienda", command=self.abrirTienda, **estiloBoton))
        self.framePanel.create_window(110, 355, window=tk.Button(self.framePanel, text="Guardar", command=self.guardar, **estiloBoton))

        self.framePanel.create_line(10, 385, 210, 385, fill="#DAA520", width=2)

        self.framePanel.create_window(110, 420, window=tk.Button(self.framePanel, text="<< Anterior", command=self.terrenoAnterior, **estiloBoton))
        self.framePanel.create_window(110, 470, window=tk.Button(self.framePanel, text="Siguiente >>", command=self.terrenoSiguiente, **estiloBoton))
        self.framePanel.create_window(110, 520, window=tk.Button(self.framePanel, text="+ Terreno", command=self.comprarTerreno, **estiloBoton))

        self.framePanel.create_line(10, 555, 210, 555, fill="#DAA520", width=2)
        self.framePanel.create_window(110, 585, window=tk.Button(self.framePanel, text="Menu", command=self.volverMenu, **estiloBoton))
        self.framePanel.create_window(110, 630, window=tk.Button(self.framePanel, text="Salir", command=self.salirJuego, **estiloBoton))

    def clickCelda(self, fila, columna):
        """
        Maneja el clic izquierdo en una celda del terreno.
        Si hay un producto seleccionado lo coloca en la celda,
        si la celda tiene un decorativo rotable lo rota,
        si tiene un producto listo lo cosecha.

        Args:
            fila (int): Índice de la fila de la celda clickeada.
            columna (int): Índice de la columna de la celda clickeada.
        """
        terreno = self.jugador.getTerrenos()[self.terrenoActual]

        if self.productoSeleccionado is not None and terreno.celdaDisponible(fila, columna):
            terreno.agregarElemento(fila, columna, self.productoSeleccionado)
            self.productoSeleccionado = None
            self.actualizarPanel()
            self.actualizarGrid()

        elif not terreno.celdaDisponible(fila, columna):
            producto = terreno.getMatriz()[fila][columna]

            if hasattr(producto, 'rotar'):
                producto.rotar()
                self.actualizarGrid()
                return

            if producto.estaListo():
                self.jugador._monedas += producto.getGanancia()
                self.jugador._totalMonedasGeneradas += producto.getGanancia()
                if producto.reiniciarCiclo():
                    producto.colocar()
                else:
                    terreno.quitarElemento(fila, columna)
                self.actualizarPanel()
                self.actualizarGrid()
            else:
                if producto.getTiempoProduccion() == 0:
                    mb.showinfo("Info", f"{producto.getNombre()} es un objeto decorativo")
                else:
                    tiempoRestante = producto.getTiempoProduccion() - (time.time() - producto.getHoraInicio())
                    mb.showinfo("Info", f"{producto.getNombre()} listo en {int(tiempoRestante)} segundos")

    def clickDerecho(self, fila, columna):
        """
        Maneja el clic derecho en una celda del terreno.
        Ofrece vender el producto colocado en esa celda al 50% de su precio.

        Args:
            fila (int): Índice de la fila de la celda clickeada.
            columna (int): Índice de la columna de la celda clickeada.
        """
        terreno = self.jugador.getTerrenos()[self.terrenoActual]

        if terreno.celdaDisponible(fila, columna):
            return

        producto = terreno.getMatriz()[fila][columna]
        devolucion = int(producto.getPrecio() * 0.50)

        confirmacion = mb.askokcancel(
            "Vender",
            f"¿Quieres vender {producto.getNombre()}?\nRecibirás {devolucion} monedas"
        )
        if confirmacion:
            self.jugador._monedas += devolucion
            terreno.quitarElemento(fila, columna)
            self.actualizarPanel()
            self.actualizarGrid()

    def actualizarGrid(self):
        """
        Actualiza visualmente todas las celdas del grid según el estado
        actual del terreno. Aplica sprites, rotaciones y el indicador
        de exclamación para productos listos.
        """
        terreno = self.jugador.getTerrenos()[self.terrenoActual]
        for fila in range(15):
            for columna in range(15):
                celda = terreno.getMatriz()[fila][columna]
                boton = self.botonesCeldas[fila][columna]
                if celda is None:
                    imagen = self.imagenes["pasto"][0]
                    boton.config(image=imagen, text="", width=48, height=48)
                    boton.image = imagen
                else:
                    nombre = celda.getNombre()
                    if nombre in self.imagenes:
                        if isinstance(celda, (Plantacion, Arbol)):
                            frameIndex = self.obtenerFrameCultivo(celda, len(self.imagenes[nombre]))
                        else:
                            clave = f"{fila},{columna}"
                            if clave not in self.frameActual:
                                self.frameActual[clave] = 0
                            frameIndex = self.frameActual[clave] % len(self.imagenes[nombre])

                        imagenPIL = self.imagenesRaw[nombre][frameIndex]
                        if hasattr(celda, 'getRotacion') and celda.getRotacion() != 0:
                            imagenPIL = imagenPIL.rotate(-celda.getRotacion())
                        imagen = ImageTk.PhotoImage(imagenPIL)
                        boton.config(image=imagen, text="", width=48, height=48)
                        boton.image = imagen

                        if celda.estaListo():
                            imagenConExclamacion = self.agregarExclamacion(imagenPIL)
                            boton.config(image=imagenConExclamacion, bg="SystemButtonFace", relief="raised")
                            boton.image = imagenConExclamacion
                        else:
                            boton.config(bg="SystemButtonFace", relief="raised")
                    else:
                        boton.config(image="", text=nombre[:4])

    def obtenerFrameCultivo(self, producto, totalFrames):
        """
        Calcula el índice del frame a mostrar para un cultivo o árbol
        según el porcentaje de tiempo de producción transcurrido.

        Args:
            producto (Producto): El producto cuyo frame se calcula.
            totalFrames (int): Cantidad total de frames disponibles.

        Returns:
            int: Índice del frame correspondiente al progreso actual.
        """
        if producto.getHoraInicio() is None:
            return 0
        tiempoPasado = time.time() - producto.getHoraInicio()
        tiempoTotal = producto.getTiempoProduccion()
        porcentaje = min(tiempoPasado / tiempoTotal, 1.0)
        frameIndex = int(porcentaje * totalFrames)
        return min(frameIndex, totalFrames - 1)

    def actualizarAutomatico(self):
        """
        Actualiza automáticamente el panel y el grid cada 500ms.
        También avanza los frames de animación de los animales.
        """
        for clave in list(self.frameActual.keys()):
            self.frameActual[clave] += 1

        self.actualizarPanel()
        self.actualizarGrid()
        self.ventana.after(500, self.actualizarAutomatico)

    def seleccionarProducto(self, producto):
        """
        Establece el producto seleccionado para colocar en el terreno.

        Args:
            producto (Producto): El producto a colocar.
        """
        self.productoSeleccionado = producto

    def abrirTienda(self):
        """Abre la ventana de tienda si no está ya abierta."""
        if hasattr(self, 'tiendaAbierta') and self.tiendaAbierta:
            return
        self.tiendaAbierta = True
        ventana = VentanaTienda(self.ventana, self.jugador, self.seleccionarProducto)
        ventana.ventana.protocol("WM_DELETE_WINDOW", lambda: self.cerrarVentana('tiendaAbierta', ventana))

    def cerrarVentana(self, atributo, ventana):
        """
        Cierra una ventana secundaria y marca su flag como cerrada.

        Args:
            atributo (str): Nombre del atributo booleano a poner en False.
            ventana: Objeto ventana con atributo .ventana de Tkinter.
        """
        setattr(self, atributo, False)
        ventana.ventana.destroy()

    def abrirInventario(self):
        """Abre la ventana de inventario si no está ya abierta."""
        if hasattr(self, 'inventarioAbierto') and self.inventarioAbierto:
            return
        self.inventarioAbierto = True
        ventana = VentanaInventario(self.ventana, self.jugador, self.seleccionarProducto, self.cerrarInventario)
        ventana.ventana.protocol("WM_DELETE_WINDOW", lambda: self.cerrarVentana('inventarioAbierto', ventana))

    def cerrarInventario(self):
        """Marca el inventario como cerrado para permitir reabrirlo."""
        self.inventarioAbierto = False

    def guardar(self):
        """Guarda la partida actual en el archivo JSON y notifica al jugador."""
        guardarPartida(self.jugador)
        mb.showinfo("Guardado", "¡Partida guardada exitosamente!")

    def terrenoAnterior(self):
        """Navega al terreno anterior si existe."""
        if self.terrenoActual > 0:
            self.terrenoActual -= 1
            self.actualizarGrid()

    def terrenoSiguiente(self):
        """Navega al terreno siguiente si existe."""
        if self.terrenoActual < len(self.jugador.getTerrenos()) - 1:
            self.terrenoActual += 1
            self.actualizarGrid()

    def volverMenu(self):
        """Cierra la ventana de juego y vuelve al menú principal."""
        confirmacion = mb.askokcancel("Volver", "¿Volver al menú? Los cambios no guardados se perderán")
        if confirmacion:
            self.ventana.destroy()
            self.ventanaPadre.deiconify()

    def salirJuego(self):
        """Cierra completamente el juego."""
        confirmacion = mb.askokcancel("Salir", "¿Salir del juego?")
        if confirmacion:
            self.ventanaPadre.destroy()

    def comprarTerreno(self):
        """
        Permite al jugador comprar un nuevo terreno por 20,000 monedas
        previa confirmación. Valida que tenga monedas suficientes.
        """
        confirmacion = mb.askokcancel("Comprar terreno", "¿Comprar un nuevo terreno por 20,000 monedas?")
        if not confirmacion:
            return
        if self.jugador.getMonedas() < 20000:
            mb.showerror("Error", "¡Monedas insuficientes!")
            return

        self.jugador._monedas -= 20000
        nuevoID = len(self.jugador.getTerrenos())
        nuevoTerreno = Terreno(nuevoID)
        self.jugador.agregarTerreno(nuevoTerreno)
        self.actualizarPanel()
        mb.showinfo("¡Nuevo terreno!", f"Terreno {nuevoID + 1} adquirido")

    def actualizarPanel(self):
        """
        Actualiza todas las etiquetas del panel lateral con los datos
        actuales del jugador: monedas, terrenos, producciones listas y tiempo.
        """
        totalListas = 0
        for terreno in self.jugador.getTerrenos():
            for fila in terreno.getMatriz():
                for celda in fila:
                    if celda is not None and celda.estaListo():
                        totalListas += 1
        self.panelProduccionesListas.set(f"Producciones listas: {totalListas}")
        self.panelMonedas.set(f"Monedas: {self.jugador.getMonedas()}")
        self.panelCantidadTerrenos.set(f"Terrenos: {self.jugador.getCantidadTerrenos()}")
        self.panelTiempoTotalJuego.set(f"Tiempo jugado: {int(self.jugador.getTiempoJugado())} seg")