'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 19, Proyecto #3: SiembraTEC

Fecha de entrega: 29/06/2026

'''

import tkinter as tk


class VentanaEstadisticas:
    """
    Ventana de estadísticas del juego SiembraTEC.
    Muestra información general de la partida incluyendo monedas,
    tiempo jugado, productos comprados y cantidad por tipo.
    """

    def __init__(self, ventanaPadre, jugador):
        """
        Inicializa la ventana de estadísticas.

        Args:
            ventanaPadre (tk.Tk): La ventana padre (menú principal).
            jugador (Jugador): El objeto jugador con la información de la partida.
        """
        self.jugador = jugador
        self.ventana = tk.Toplevel(ventanaPadre)
        self.ventana.title("Estadísticas")
        self.ventana.geometry("450x550")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#5C3317")

        self.crearEstadisticas()

    def crearEstadisticas(self):
        """
        Construye la interfaz de estadísticas con datos generales del jugador
        y una lista scrollable de productos comprados por tipo.
        """
        fuente = ("Press Start 2P", 7)
        estilo = {"bg": "#5C3317", "fg": "#FFD700", "font": fuente}

        tk.Label(self.ventana, text="Estadísticas",
            font=("Press Start 2P", 12), bg="#5C3317", fg="#FFD700").pack(pady=15)

        tk.Canvas(self.ventana, height=2, bg="#DAA520").pack(fill="x", padx=10)

        frame = tk.Frame(self.ventana, bg="#5C3317")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        datos = [
            ("Jugador", self.jugador.getNombre()),
            ("Monedas actuales", str(self.jugador.getMonedas())),
            ("Total generado", str(self.jugador.getTotalMonedasGeneradas())),
            ("Productos comprados", str(self.jugador.getTotalProductosComprados())),
            ("Terrenos", str(self.jugador.getCantidadTerrenos())),
            ("Tiempo total", f"{int(self.jugador.getTiempoTotal())} seg"),
        ]

        for indice, (etiqueta, valor) in enumerate(datos):
            tk.Label(frame, text=etiqueta, anchor="w", width=22, **estilo).grid(row=indice, column=0, padx=5, pady=6, sticky="w")
            tk.Label(frame, text=valor, anchor="e", width=12, **estilo).grid(row=indice, column=1, padx=5, pady=6, sticky="e")

        tk.Canvas(self.ventana, height=2, bg="#DAA520").pack(fill="x", padx=10)

        tk.Label(self.ventana, text="Productos por tipo",
            font=("Press Start 2P", 8), bg="#5C3317", fg="#FFD700").pack(pady=8)

        frameContenedor = tk.Frame(self.ventana, bg="#5C3317")
        frameContenedor.pack(fill="both", expand=True, padx=10)

        scrollbar = tk.Scrollbar(frameContenedor)
        scrollbar.pack(side="right", fill="y")

        canvas = tk.Canvas(frameContenedor, bg="#5C3317", height=150,
            yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=canvas.yview)

        frameTipos = tk.Frame(canvas, bg="#5C3317")
        canvas.create_window((0, 0), window=frameTipos, anchor="nw")
        frameTipos.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        if len(self.jugador.getCantidadPorTipo()) == 0:
            tk.Label(frameTipos, text="Sin productos aún",
                font=("Press Start 2P", 7), bg="#5C3317", fg="#FFD700").pack(pady=5)
        else:
            for tipo, cantidad in self.jugador.getCantidadPorTipo().items():
                tk.Label(frameTipos, text=f"{tipo}: {cantidad}",
                    font=("Press Start 2P", 7), bg="#5C3317", fg="#FFD700").pack(anchor="w", padx=10, pady=2)