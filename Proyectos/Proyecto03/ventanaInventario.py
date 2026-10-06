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


class VentanaInventario:
    """
    Ventana del inventario del juego SiembraTEC.
    Muestra los productos comprados pendientes de colocar en el terreno
    y permite colocarlos o venderlos al 50% de su precio.
    """

    def __init__(self, ventanaPadre, jugador, alColocar, alCerrar=None):
        """
        Inicializa la ventana de inventario.

        Args:
            ventanaPadre (tk.Toplevel): La ventana padre del juego.
            jugador (Jugador): El objeto jugador actual.
            alColocar (function): Función callback que se llama al colocar un producto.
            alCerrar (function): Función callback que se llama al cerrar el inventario.
        """
        self.alCerrar = alCerrar
        self.jugador = jugador
        self.alColocar = alColocar
        self.ventana = tk.Toplevel(ventanaPadre)
        self.ventana.title("Inventario")
        self.ventana.geometry("500x500")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#5C3317")

        self.crearInventario()

    def crearInventario(self):
        """
        Construye la interfaz del inventario con lista de productos,
        botones de colocar y vender, y área de scroll.
        """
        tk.Label(self.ventana, text="Inventario",
            font=("Press Start 2P", 12), bg="#5C3317", fg="#FFD700").pack(pady=10)

        tk.Canvas(self.ventana, height=2, bg="#DAA520").pack(fill="x", padx=10)

        frameContenedor = tk.Frame(self.ventana, bg="#5C3317")
        frameContenedor.pack(fill="both", expand=True, padx=10, pady=5)

        scrollbar = tk.Scrollbar(frameContenedor)
        scrollbar.pack(side="right", fill="y")

        canvas = tk.Canvas(frameContenedor, bg="#5C3317",
            yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=canvas.yview)

        frameProductos = tk.Frame(canvas, bg="#5C3317")
        canvas.create_window((0, 0), window=frameProductos, anchor="nw")
        frameProductos.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        if len(self.jugador.getInventario()) == 0:
            tk.Label(frameProductos,
                text="No tienes productos en el inventario",
                font=("Press Start 2P", 8), bg="#5C3317", fg="#FFD700").pack(pady=20)
            return

        estiloHeader = {"bg": "#8B6914", "fg": "#FFD700", "font": ("Press Start 2P", 6)}
        tk.Label(frameProductos, text="Producto", width=12, **estiloHeader).grid(row=0, column=0, padx=2, pady=2)
        tk.Label(frameProductos, text="Precio", width=8, **estiloHeader).grid(row=0, column=1, padx=2, pady=2)
        tk.Label(frameProductos, text="Colocar", width=8, **estiloHeader).grid(row=0, column=2, padx=2, pady=2)
        tk.Label(frameProductos, text="Vender", width=8, **estiloHeader).grid(row=0, column=3, padx=2, pady=2)

        estiloFila = {"bg": "#5C3317", "fg": "#FFD700", "font": ("Press Start 2P", 6)}
        estiloBoton = {"font": ("Press Start 2P", 6), "bg": "#8B6914", "fg": "#FFD700", "relief": "raised", "bd": 2}

        for indice, producto in enumerate(self.jugador.getInventario()):
            fila = indice + 1
            tk.Label(frameProductos, text=producto.getNombre(), width=12, **estiloFila).grid(row=fila, column=0, padx=2, pady=4)
            tk.Label(frameProductos, text=str(producto.getPrecio()), width=8, **estiloFila).grid(row=fila, column=1, padx=2, pady=4)
            tk.Button(frameProductos, text="Colocar", width=8,
                command=lambda p=producto: self.colocar(p), **estiloBoton).grid(row=fila, column=2, padx=2, pady=4)
            tk.Button(frameProductos, text="Vender", width=8,
                command=lambda p=producto: self.vender(p), **estiloBoton).grid(row=fila, column=3, padx=2, pady=4)

        tk.Canvas(self.ventana, height=2, bg="#DAA520").pack(fill="x", padx=10)
        tk.Label(self.ventana, text=f"{self.jugador.getMonedas()} monedas",
            font=("Press Start 2P", 7), bg="#5C3317", fg="#FFD700").pack(pady=5)

    def colocar(self, producto):
        """
        Coloca un producto del inventario en el terreno.
        Elimina el producto del inventario y cierra la ventana.

        Args:
            producto (Producto): El producto a colocar en el terreno.
        """
        self.jugador.getInventario().remove(producto)
        self.alColocar(producto)
        if self.alCerrar:
            self.alCerrar()
        self.ventana.destroy()

    def vender(self, producto):
        """
        Vende un producto del inventario al 50% de su precio original.
        Solicita confirmación antes de proceder.

        Args:
            producto (Producto): El producto a vender.
        """
        devolucion = int(producto.getPrecio() * 0.50)
        confirmacion = mb.askokcancel(
            "Vender",
            f"¿Vender {producto.getNombre()}?\nRecibirás {devolucion} monedas (50%)"
        )
        if confirmacion:
            self.jugador._monedas += devolucion
            self.jugador.getInventario().remove(producto)
            if self.alCerrar:
                self.alCerrar()
            self.ventana.destroy()