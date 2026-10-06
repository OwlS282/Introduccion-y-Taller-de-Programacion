'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 19, Proyecto #3: SiembraTEC

Fecha de entrega: 29/06/2026

'''
import time

class Producto:
    """
    Clase base que representa un producto de la granja.
    Contiene los atributos y métodos comunes a todos los productos.
    """

    def __init__(self, nombre, precio, tiempoProduccion, ganancia):
        """
        Inicializa un producto con sus atributos base.

        Args:
            nombre (str): Nombre del producto.
            precio (int): Costo en monedas para comprarlo.
            tiempoProduccion (int): Segundos necesarios para producir.
            ganancia (int): Monedas que genera al cosechar.
        """
        self._nombre = nombre
        self._precio = precio
        self._ganancia = ganancia
        self._tiempoProduccion = tiempoProduccion
        self._horaInicio = None

    def getNombre(self):
        """Retorna el nombre del producto."""
        return self._nombre

    def getPrecio(self):
        """Retorna el precio del producto en monedas."""
        return self._precio

    def getGanancia(self):
        """Retorna la ganancia del producto al cosechar."""
        return self._ganancia

    def getTiempoProduccion(self):
        """Retorna el tiempo de producción en segundos."""
        return self._tiempoProduccion

    def getHoraInicio(self):
        """Retorna el timestamp Unix de cuando fue colocado, o None si no ha sido colocado."""
        return self._horaInicio

    def colocar(self):
        """Registra la hora actual como inicio del ciclo de producción."""
        self._horaInicio = time.time()

    def estaListo(self):
        """
        Verifica si el producto ha completado su ciclo de producción.

        Returns:
            bool: True si está listo para cosechar, False en caso contrario.
        """
        if self._horaInicio is None:
            return False
        tiempoPasado = time.time() - self._horaInicio
        if tiempoPasado >= self._tiempoProduccion:
            return True
        return False


class Plantacion(Producto):
    """
    Subclase de Producto que representa cultivos agrícolas.
    Las plantaciones NO reinician su ciclo al ser cosechadas — deben recomprarse.
    """

    def reiniciarCiclo(self):
        """Retorna False porque las plantaciones no reinician su ciclo al cosechar."""
        return False


class Trigo(Plantacion):
    """Plantación de trigo. Precio: 20, Tiempo: 30s, Ganancia: 35."""
    def __init__(self):
        super().__init__("Trigo", 20, 30, 35)

class Maiz(Plantacion):
    """Plantación de maíz. Precio: 35, Tiempo: 60s, Ganancia: 60."""
    def __init__(self):
        super().__init__("Maiz", 35, 60, 60)

class Zanahoria(Plantacion):
    """Plantación de zanahoria. Precio: 50, Tiempo: 90s, Ganancia: 90."""
    def __init__(self):
        super().__init__("Zanahoria", 50, 90, 90)

class Tomate(Plantacion):
    """Plantación de tomate. Precio: 75, Tiempo: 120s, Ganancia: 130."""
    def __init__(self):
        super().__init__("Tomate", 75, 120, 130)

class Papa(Plantacion):
    """Plantación de papa. Precio: 100, Tiempo: 180s, Ganancia: 180."""
    def __init__(self):
        super().__init__("Papa", 100, 180, 180)


class Animal(Producto):
    """
    Subclase de Producto que representa animales de la granja.
    Los animales SÍ reinician su ciclo automáticamente al ser cosechados.
    """

    def reiniciarCiclo(self):
        """Retorna True porque los animales reinician su ciclo automáticamente."""
        return True


class Gallina(Animal):
    """Animal gallina. Precio: 150, Tiempo: 120s, Ganancia: 250."""
    def __init__(self):
        super().__init__("Gallina", 150, 120, 250)

class Pato(Animal):
    """Animal pato. Precio: 250, Tiempo: 180s, Ganancia: 400."""
    def __init__(self):
        super().__init__("Pato", 250, 180, 400)

class Oveja(Animal):
    """Animal oveja. Precio: 400, Tiempo: 300s, Ganancia: 650."""
    def __init__(self):
        super().__init__("Oveja", 400, 300, 650)

class Cerdo(Animal):
    """Animal cerdo. Precio: 700, Tiempo: 420s, Ganancia: 1100."""
    def __init__(self):
        super().__init__("Cerdo", 700, 420, 1100)

class Vaca(Animal):
    """Animal vaca. Precio: 1000, Tiempo: 600s, Ganancia: 1700."""
    def __init__(self):
        super().__init__("Vaca", 1000, 600, 1700)


class VacaEspecial(Vaca):
    """
    Vaca especial única llamada Lana.
    Solo puede existir una instancia en toda la partida.
    Se distingue por su sombrero vaquero rosado.
    """

    def __init__(self):
        """Inicializa a Lana con precio 0 y la marca como única."""
        Producto.__init__(self, "Lana", 0, 600, 1700)
        self._esUnica = True

    def getEsUnica(self):
        """Retorna True indicando que Lana es un objeto único."""
        return self._esUnica


class Arbol(Producto):
    """
    Subclase de Producto que representa árboles frutales.
    Los árboles SÍ reinician su ciclo automáticamente al ser cosechados.
    """

    def reiniciarCiclo(self):
        """Retorna True porque los árboles reinician su ciclo automáticamente."""
        return True


class Manzano(Arbol):
    """Árbol manzano. Precio: 120, Tiempo: 180s, Ganancia: 200."""
    def __init__(self):
        super().__init__("Manzano", 120, 180, 200)

class Naranjo(Arbol):
    """Árbol naranjo. Precio: 180, Tiempo: 240s, Ganancia: 320."""
    def __init__(self):
        super().__init__("Naranjo", 180, 240, 320)

class Limonero(Arbol):
    """Árbol limonero. Precio: 250, Tiempo: 300s, Ganancia: 450."""
    def __init__(self):
        super().__init__("Limonero", 250, 300, 450)

class Cacaotero(Arbol):
    """Árbol cacaotero. Precio: 500, Tiempo: 480s, Ganancia: 850."""
    def __init__(self):
        super().__init__("Cacaotero", 500, 480, 850)

class Cafetal(Arbol):
    """Árbol cafetal. Precio: 800, Tiempo: 600s, Ganancia: 1400."""
    def __init__(self):
        super().__init__("Cafetal", 800, 600, 1400)


class Decorativo(Producto):
    """
    Subclase de Producto que representa elementos decorativos.
    Los decorativos no generan producción ni monedas.
    """

    def reiniciarCiclo(self):
        """Retorna False porque los decorativos no producen nada."""
        return False

    def estaListo(self):
        """Retorna False porque los decorativos nunca están listos para cosechar."""
        return False


class Cerca(Decorativo):
    """
    Elemento decorativo cerca. Soporta rotación en múltiplos de 90 grados.
    Precio: 50 monedas.
    """

    def __init__(self, rotacion=0):
        """
        Inicializa la cerca con una rotación opcional.

        Args:
            rotacion (int): Ángulo inicial de rotación (0, 90, 180 o 270).
        """
        super().__init__("Cerca", 50, 0, 0)
        self.rotacion = rotacion

    def getRotacion(self):
        """Retorna el ángulo de rotación actual de la cerca."""
        return self.rotacion

    def rotar(self):
        """Rota la cerca 90 grados en sentido horario."""
        self.rotacion = (self.rotacion + 90) % 360


class Banco(Decorativo):
    """
    Elemento decorativo banco. Soporta rotación en múltiplos de 90 grados.
    Precio: 100 monedas.
    """

    def __init__(self, rotacion=0):
        """
        Inicializa el banco con una rotación opcional.

        Args:
            rotacion (int): Ángulo inicial de rotación (0, 90, 180 o 270).
        """
        super().__init__("Banco", 100, 0, 0)
        self.rotacion = rotacion

    def getRotacion(self):
        """Retorna el ángulo de rotación actual del banco."""
        return self.rotacion

    def rotar(self):
        """Rota el banco 90 grados en sentido horario."""
        self.rotacion = (self.rotacion + 90) % 360


class Fuente(Decorativo):
    """Elemento decorativo fuente. Precio: 250 monedas."""
    def __init__(self):
        super().__init__("Fuente", 250, 0, 0)


class Estatua(Decorativo):
    """Elemento decorativo estatua. Precio: 500 monedas."""
    def __init__(self):
        super().__init__("Estatua", 500, 0, 0)


class Molino(Decorativo):
    """Elemento decorativo molino. Precio: 1000 monedas."""
    def __init__(self):
        super().__init__("Molino", 1000, 0, 0)