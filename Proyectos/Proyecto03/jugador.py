'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 19, Proyecto #3: SiembraTEC

Fecha de entrega: 29/06/2026

'''
import time

class Jugador:
    """
    Clase que representa al jugador del juego SiembraTEC.
    Gestiona las monedas, terrenos, inventario y estadísticas del jugador.
    """

    def __init__(self, nombre):
        """
        Inicializa un jugador con valores por defecto.

        Args:
            nombre (str): Nombre del jugador.
        """
        self._nombre = nombre
        self._monedas = 100
        self._terrenos = []
        self._tiempoInicio = time.time()
        self._totalMonedasGeneradas = 0
        self._totalProductosComprados = 0
        self._cantidadPorTipo = {}
        self._cantidadTerrenos = 0
        self._tiempoAcumulado = 0
        self._LVHDisponible = True
        self._inventario = []

    def getTiempoJugado(self):
        """Retorna los segundos transcurridos en la sesión actual."""
        return time.time() - self._tiempoInicio

    def getNombre(self):
        """Retorna el nombre del jugador."""
        return self._nombre

    def getMonedas(self):
        """Retorna la cantidad de monedas disponibles del jugador."""
        return self._monedas

    def getTerrenos(self):
        """Retorna la lista de terrenos del jugador."""
        return self._terrenos

    def getTiempoInicio(self):
        """Retorna el timestamp Unix del inicio de la sesión actual."""
        return self._tiempoInicio

    def getTotalMonedasGeneradas(self):
        """Retorna el total de monedas generadas por cosechas en todas las sesiones."""
        return self._totalMonedasGeneradas

    def getTotalProductosComprados(self):
        """Retorna el total de productos comprados en todas las sesiones."""
        return self._totalProductosComprados

    def getCantidadPorTipo(self):
        """Retorna un diccionario con la cantidad de productos comprados por tipo."""
        return self._cantidadPorTipo

    def getCantidadTerrenos(self):
        """Retorna la cantidad de terrenos adquiridos por el jugador."""
        return self._cantidadTerrenos

    def getTiempoAcumulado(self):
        """Retorna el tiempo total jugado acumulado en sesiones anteriores."""
        return self._tiempoAcumulado

    def getTiempoTotal(self):
        """Retorna el tiempo total jugado incluyendo la sesión actual."""
        return self._tiempoAcumulado + (time.time() - self._tiempoInicio)

    def getLVHDisponible(self):
        """Retorna True si Lana (la vaca especial) aún está disponible para adoptar."""
        return self._LVHDisponible

    def getInventario(self):
        """Retorna la lista de productos comprados pendientes de colocar."""
        return self._inventario

    def agregarTerreno(self, terreno):
        """
        Agrega un nuevo terreno a la lista del jugador.

        Args:
            terreno (Terreno): El terreno a agregar.
        """
        self._terrenos.append(terreno)
        self._cantidadTerrenos = len(self._terrenos)

    def comprarProductos(self, producto):
        """
        Intenta comprar un producto descontando su precio de las monedas del jugador.
        Si la compra es exitosa, agrega el producto al inventario y actualiza estadísticas.

        Args:
            producto (Producto): El producto a comprar.

        Returns:
            bool: True si la compra fue exitosa, False si no hay suficientes monedas.
        """
        if self._monedas < producto.getPrecio():
            return False

        self._monedas -= producto.getPrecio()
        self._totalProductosComprados += 1

        tipo = producto.getNombre()
        if tipo in self._cantidadPorTipo:
            self._cantidadPorTipo[tipo] += 1
        else:
            self._cantidadPorTipo[tipo] = 1

        self._inventario.append(producto)
        return True