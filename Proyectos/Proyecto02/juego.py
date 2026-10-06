'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 12, Proyecto #2: Buscaminas

Fecha de entrega: 22/05/2026

'''
# Archivo: juego.py
# Descripción: Lógica principal del juego Buscaminas
#              Maneja las matrices, minas, pistas y reglas
import random

class Tablero:
    """
    Clase que representa el tablero del juego Buscaminas.
    Utiliza dos matrices:
    - logica: almacena el estado real del tablero (-1=mina, 0=vacío, 1-8=número)
    - visual: almacena lo que ve el jugador (?=oculto, V=visible, F=bandera)
    """

    def __init__(self, filas, columnas, minas):
        # Dimensiones del tablero
        self.filas = filas
        self.columnas = columnas
        self.minas = minas

        # Matriz logica estado real del tablero (inicia en ceros)
        self.logica = [[0]*columnas for _ in range(filas)]

        # Matriz visual lo que ve el jugador (inicia oculto)
        self.visual = [['?']*columnas for _ in range(filas)]

        # Control del primer click las minas se generan después del primer click
        self.primerClic = True

        # Contador de banderas colocadas
        self.banderasColocadas = 0

        # Estado del juego
        self.juegoActivo = True
        self.ganado = False

    # Generación aleatoria del tablero
    def colocarMinas(self, filaEvitar, columnaEvitar):
        """
        Coloca las minas aleatoriamente en el tablero.
        Evita colocar minas en la celda del primer clic
        y sus 8 vecinas, garantizando un area segura inicial.
        """
        # Construir el conjunto de celdas a evitar
        celdasEvitar = set()
        totalCeldas = self.filas * self.columnas

        if totalCeldas - 9 >= self.minas:
            for desplazamientoFila in [-1, 0, 1]:
                for desplazamientoColumna in [-1, 0, 1]:
                    filaVecina = filaEvitar + desplazamientoFila
                    columnaVecina = columnaEvitar + desplazamientoColumna
                    if 0 <= filaVecina < self.filas and 0 <= columnaVecina < self.columnas:
                        celdasEvitar.add((filaVecina, columnaVecina))
        else:
            celdasEvitar.add((filaEvitar, columnaEvitar))

        # Colocar minas en posiciones aleatorias validas
        minasColocadas = 0
        while minasColocadas < self.minas:
            minasFilas = random.randint(0, self.filas - 1)
            minasColumnas = random.randint(0, self.columnas - 1)
            if self.logica[minasFilas][minasColumnas] != -1 and (minasFilas, minasColumnas) not in celdasEvitar:
                self.logica[minasFilas][minasColumnas] = -1
                minasColocadas = minasColocadas + 1

    def calcularPistasNumericas(self):
        """
        Calcula los numeros de pista para cada celda que no es mina.
        Cada numero indica cuantas minas hay en las 8 celdas vecinas.
        """
        for celdaFilas in range(self.filas):
            for celdaColumnas in range(self.columnas):
                # Saltar celdas que son mina
                if self.logica[celdaFilas][celdaColumnas] == -1:
                    continue

                # Contar minas en las 8 celdas vecinas
                minasVecinas = 0
                for desplazamientoFila in [-1, 0, 1]:
                    for desplazamientoColumna in [-1, 0, 1]:
                        filaVecina = celdaFilas + desplazamientoFila
                        columnaVecina = celdaColumnas + desplazamientoColumna
                        if 0 <= filaVecina < self.filas and 0 <= columnaVecina < self.columnas:
                            if self.logica[filaVecina][columnaVecina] == -1:
                                minasVecinas = minasVecinas + 1

                # Guardar el conteo en la matriz logica
                self.logica[celdaFilas][celdaColumnas] = minasVecinas

    # Logica de click del jugador
    def revelar(self, fila, columna):
        """
        Maneja el clic izquierdo del jugador en una celda.
        En el primer clic genera el tablero garantizando área segura.
        Detecta victoria o derrota según la celda seleccionada.
        """
        # En el primer clic se generan las minas y las pistas
        if self.primerClic:
            self.colocarMinas(fila, columna)
            self.calcularPistasNumericas()
            self.primerClic = False

        # No hacer nada si el juego terminó
        if not self.juegoActivo:
            return

        # No hacer nada si la celda ya fue revelada
        if self.visual[fila][columna] != '?':
            return

        # Si es mina, derrota
        if self.logica[fila][columna] == -1:
            self.visual[fila][columna] = 'V'
            self.juegoActivo = False
            return

        # Si es celda segura, expandir y verificar victoria
        self.expandir(fila, columna)
        self.verificarVictoria()

    def expandir(self, fila, columna):
        """
        Expansión automática recursiva.
        Cuando una celda vacía (valor 0) es revelada,
        se revelan automáticamente todas sus celdas vecinas.
        La recursión se detiene cuando encuentra bordes,
        celdas ya reveladas o celdas con número.
        """
        cola = [(fila, columna)]
        visitadas = set()
        
        while cola:
            filaActual, columnaActual = cola.pop()
            
            if (filaActual, columnaActual) in visitadas:
                continue
            if filaActual < 0 or filaActual >= self.filas or columnaActual < 0 or columnaActual >= self.columnas:
                continue
            if self.visual[filaActual][columnaActual] != '?':
                continue
            
            visitadas.add((filaActual, columnaActual))
            self.visual[filaActual][columnaActual] = 'V'
            
            if self.logica[filaActual][columnaActual] == 0:
                for desplazamientoFila in [-1, 0, 1]:
                    for desplazamientoColumna in [-1, 0, 1]:
                        vecina = (filaActual + desplazamientoFila, columnaActual + desplazamientoColumna)
                        if vecina not in visitadas:
                            cola.append(vecina)

    # Verificación de victoria
    def verificarVictoria(self):
        """
        Verifica si el jugador ganó la partida.
        La victoria ocurre cuando todas las celdas sin mina
        han sido reveladas.
        """
        for fila in range(self.filas):
            for columna in range(self.columnas):
                # Si hay una celda oculta sin mina, el juego continúa
                if self.visual[fila][columna] == '?' and self.logica[fila][columna] != -1:
                    return
        # Si no quedan celdas ocultas sin mina victoria
        self.ganado = True
        self.juegoActivo = False

    # Manejo de banderas
    def ponerBanderas(self, fila, columna):
        """
        Alterna una bandera en la celda indicada.
        Solo se puede poner bandera en celdas ocultas.
        El número de banderas está limitado al total de minas.
        """
        # Poner bandera si la celda está oculta y hay banderas disponibles
        if self.visual[fila][columna] == '?' and self.banderasColocadas < self.minas:
            self.visual[fila][columna] = 'F'
            self.banderasColocadas = self.banderasColocadas + 1

        # Quitar bandera si ya tiene una
        elif self.visual[fila][columna] == 'F':
            self.visual[fila][columna] = '?'
            self.banderasColocadas = self.banderasColocadas - 1
