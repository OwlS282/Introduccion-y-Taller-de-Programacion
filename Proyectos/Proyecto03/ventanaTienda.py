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

from productos import *


class VentanaTienda:
    """
    Ventana de la tienda del juego SiembraTEC.
    Permite al jugador comprar productos organizados por categorías
    con scroll y estilo retro.
    """

    def __init__(self, ventanaPadre, jugador, alComprar):
        """
        Inicializa la ventana de tienda.

        Args:
            ventanaPadre (tk.Toplevel): La ventana padre del juego.
            jugador (Jugador): El objeto jugador actual.
            alComprar (function): Función callback que se llama al adoptar a Lana.
        """
        self.jugador = jugador
        self.alComprar = alComprar
        self.ventana = tk.Toplevel(ventanaPadre)
        self.ventana.title("Tienda")
        self.ventana.geometry("500x600")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#5C3317")

        self.categoriaActual = tk.StringVar(value="Plantaciones")
        self.crearTienda()

    def crearTienda(self):
        """
        Construye la interfaz completa de la tienda con pestañas por categoría,
        área de scroll para los productos y etiqueta de monedas disponibles.
        """
        tk.Label(self.ventana, text="Tienda", font=("Press Start 2P", 12),
            bg="#5C3317", fg="#FFD700").pack(pady=10)

        framePestañas = tk.Frame(self.ventana, bg="#5C3317")
        framePestañas.pack(fill="x", padx=10)

        categorias = ["Plantaciones", "Animales", "Árboles", "Decorativos", "Especial"]
        for categoria in categorias:
            tk.Button(framePestañas, text=categoria,
                font=("Press Start 2P", 6),
                bg="#8B6914", fg="#FFD700",
                relief="raised", bd=2,
                command=lambda c=categoria: self.mostrarCategoria(c)
            ).pack(side="left", padx=2, pady=5)

        tk.Canvas(self.ventana, height=2, bg="#DAA520").pack(fill="x", padx=10)

        frameContenedor = tk.Frame(self.ventana, bg="#5C3317")
        frameContenedor.pack(fill="both", expand=True, padx=10, pady=5)

        scrollbar = tk.Scrollbar(frameContenedor)
        scrollbar.pack(side="right", fill="y")

        self.canvas = tk.Canvas(frameContenedor, bg="#5C3317",
            yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.canvas.yview)

        self.frameProductos = tk.Frame(self.canvas, bg="#5C3317")
        self.canvas.create_window((0, 0), window=self.frameProductos, anchor="nw")
        self.frameProductos.bind("<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.labelMonedas = tk.Label(self.ventana,
            text=f"{self.jugador.getMonedas()} monedas",
            font=("Press Start 2P", 7), bg="#5C3317", fg="#FFD700")
        self.labelMonedas.pack(pady=5)

        self.mostrarCategoria("Plantaciones")

    def mostrarCategoria(self, categoria):
        """
        Muestra los productos de una categoría específica en el área de scroll.
        Limpia los productos anteriores antes de mostrar los nuevos.

        Args:
            categoria (str): Nombre de la categoría a mostrar.
        """
        for widget in self.frameProductos.winfo_children():
            widget.destroy()

        categorias = {
            "Plantaciones": [Trigo, Maiz, Zanahoria, Tomate, Papa],
            "Animales": [Gallina, Pato, Oveja, Cerdo, Vaca],
            "Árboles": [Manzano, Naranjo, Limonero, Cacaotero, Cafetal],
            "Decorativos": [Cerca, Banco, Fuente, Estatua, Molino],
            "Especial": []
        }

        productos = categorias[categoria]

        estiloHeader = {"bg": "#8B6914", "fg": "#FFD700", "font": ("Press Start 2P", 6)}
        tk.Label(self.frameProductos, text="Producto", width=12, **estiloHeader).grid(row=0, column=0, padx=2, pady=2)
        tk.Label(self.frameProductos, text="Precio", width=8, **estiloHeader).grid(row=0, column=1, padx=2, pady=2)
        tk.Label(self.frameProductos, text="Tiempo", width=8, **estiloHeader).grid(row=0, column=2, padx=2, pady=2)
        tk.Label(self.frameProductos, text="Ganancia", width=8, **estiloHeader).grid(row=0, column=3, padx=2, pady=2)
        tk.Label(self.frameProductos, text="", width=8, **estiloHeader).grid(row=0, column=4, padx=2, pady=2)

        estiloFila = {"bg": "#5C3317", "fg": "#FFD700", "font": ("Press Start 2P", 6)}

        if categoria == "Especial":
            if self.jugador.getLVHDisponible():
                tk.Label(self.frameProductos, text="Lana", width=12, **estiloFila).grid(row=1, column=0, padx=2, pady=4)
                tk.Label(self.frameProductos, text="Gratis", width=8, **estiloFila).grid(row=1, column=1, padx=2, pady=4)
                tk.Label(self.frameProductos, text="Única", width=8, **estiloFila).grid(row=1, column=2, padx=2, pady=4)
                tk.Label(self.frameProductos, text="♡", width=8, **estiloFila).grid(row=1, column=3, padx=2, pady=4)
                tk.Button(self.frameProductos, text="Adoptar",
                    font=("Press Start 2P", 6), bg="#8B6914", fg="#FFD700",
                    command=self.adoptarLVH).grid(row=1, column=4, padx=2, pady=4)
            else:
                tk.Label(self.frameProductos, text="Lana ya fue adoptada ♡",
                    **estiloFila).grid(row=1, column=0, columnspan=5, pady=10)
            return

        for indice, ClaseProducto in enumerate(productos):
            productoTemp = ClaseProducto()
            fila = indice + 1
            tk.Label(self.frameProductos, text=productoTemp.getNombre(), width=12, **estiloFila).grid(row=fila, column=0, padx=2, pady=4)
            tk.Label(self.frameProductos, text=str(productoTemp.getPrecio()), width=8, **estiloFila).grid(row=fila, column=1, padx=2, pady=4)
            tk.Label(self.frameProductos, text=f"{productoTemp.getTiempoProduccion()}s", width=8, **estiloFila).grid(row=fila, column=2, padx=2, pady=4)
            tk.Label(self.frameProductos, text=str(productoTemp.getGanancia()), width=8, **estiloFila).grid(row=fila, column=3, padx=2, pady=4)
            tk.Button(self.frameProductos, text="Comprar",
                font=("Press Start 2P", 6), bg="#8B6914", fg="#FFD700",
                command=lambda cls=ClaseProducto: self.comprar(cls)
            ).grid(row=fila, column=4, padx=2, pady=4)

    def comprar(self, claseProducto):
        """
        Maneja la compra de un producto previa confirmación del jugador.
        Descuenta las monedas y agrega el producto al inventario.

        Args:
            claseProducto (class): La clase del producto a comprar.
        """
        productoNuevo = claseProducto()
        confirmacion = mb.askokcancel(
            "Confirmar compra",
            f"¿Comprar {productoNuevo.getNombre()} por {productoNuevo.getPrecio()} monedas?"
        )
        if not confirmacion:
            return
        if self.jugador.comprarProductos(productoNuevo):
            self.labelMonedas.config(text=f"{self.jugador.getMonedas()} monedas")
            mb.showinfo("¡Comprado!", f"{productoNuevo.getNombre()} agregado al inventario")
        else:
            mb.showerror("Error", "No tienes suficientes monedas")

    def adoptarLVH(self):
        """
        Maneja la adopción de Lana, la vaca especial única e irremplazable.
        Una vez adoptada no puede volver a aparecer en la tienda.
        """
        confirmacion = mb.askokcancel("Adoptar", "¿Quieres adoptar a Lana? Es única e irremplazable ♡")
        if not confirmacion:
            return
        lana = VacaEspecial()
        if self.jugador.comprarProductos(lana):
            self.jugador._LVHDisponible = False
            self.alComprar(lana)
            mb.showinfo("¡Lana ha llegado!", "Lana ha llegado a la granja ♡")
            self.ventana.destroy()
        else:
            mb.showerror("Error", "No tienes suficientes monedas")