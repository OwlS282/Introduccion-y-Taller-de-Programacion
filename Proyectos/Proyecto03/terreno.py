'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 19, Proyecto #3: SiembraTEC

Fecha de entrega: 29/06/2026

'''
class Terreno:
    """
    Clase que representa un terreno de la granja.
    Cada terreno contiene una matriz de 15x15 celdas donde
    el jugador puede colocar productos.
    """

    def __init__(self, id):
        """
        Inicializa un terreno vacío con una matriz de 15x15.

        Args:
            id (int): Identificador único del terreno.
        """
        self._id = id
        self._matriz = [[None for _ in range(15)] for _ in range(15)]

    def getID(self):
        """Retorna el identificador único del terreno."""
        return self._id

    def getMatriz(self):
        """Retorna la matriz 15x15 del terreno con todos sus elementos."""
        return self._matriz

    def agregarElemento(self, fila, columna, producto):
        """
        Coloca un producto en una celda específica del terreno.

        Args:
            fila (int): Índice de la fila (0-14).
            columna (int): Índice de la columna (0-14).
            producto (Producto): El producto a colocar.

        Returns:
            bool: True si se colocó exitosamente, False si la celda está ocupada.
        """
        if not self.celdaDisponible(fila, columna):
            return False
        self._matriz[fila][columna] = producto
        producto.colocar()
        return True

    def quitarElemento(self, fila, columna):
        """
        Elimina el producto de una celda específica del terreno.

        Args:
            fila (int): Índice de la fila (0-14).
            columna (int): Índice de la columna (0-14).
        """
        self._matriz[fila][columna] = None

    def celdaDisponible(self, fila, columna):
        """
        Verifica si una celda específica está vacía.

        Args:
            fila (int): Índice de la fila (0-14).
            columna (int): Índice de la columna (0-14).

        Returns:
            bool: True si la celda está vacía, False si está ocupada.
        """
        if self._matriz[fila][columna] is None:
            return True
        return False