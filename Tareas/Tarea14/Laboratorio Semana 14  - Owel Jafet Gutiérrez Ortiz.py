'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 15: Laboratorio (Semana 14): Matrices

Fecha de entrega: 07/06/2026

'''

#Ejercicio 01
'''
def sumaDigitos(numero):
    #retorna la suma en los digitos de un numero positivo entero
    if numero < 10:
        return numero
    
    return (numero % 10) + sumaDigitos(numero // 10)

def rotar90(matriz):
    #recibe una matriz cuadrada y retorna una nueva matriz rotada 90 grados a la derecha
    numero = len(matriz)
    
    #creamos la matriz de ceros del mismo tamaño
    resultado = [[0] * numero for _ in range(numero)]

    for fila in range(numero):
        for columna in range(numero):
            
            resultado[columna][numero - 1 - fila] = matriz[fila][columna]
    return resultado

def imprimirMatriz(matriz):
    #por cada fila en la matriz, imprimimos
    for fila in matriz:
        print(fila)

#Ejemplo Suma
numero = 5831
print(f"La suma de los digitos {numero} es {sumaDigitos(numero)}")
print("")


#Ejemplo Matriz
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Matriz Original: ")
imprimirMatriz(matriz)
print("Matriz Rotada 90° a la derecha: ")
imprimirMatriz(rotar90(matriz))
'''

#Ejercicio 02
'''
def sumaVecinos(matriz):

    # obtenemos el numero de filas y columnas de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])

    # creamos una matriz de ceros del mismo tamaño para guardar el resultado
    resultado = [[0] * columnas for _ in range(filas)]

    # definimos direcciones arriba, abajo, izquierda y derecha.
    direcciones = [(-1,0), (1,0), (0,-1), (0,1)]

    
    for fila in range(filas):
        for columna in range(columnas):
            total = 0

            #recorremos cada direccion posible
            for direccionFilas, direccionColumnas in direcciones:
                #calculamos la posicion del vecino sumando la dirrecion a la posicion actual
                direccionFilas, direccionColumnas = fila + direccionFilas, columna + direccionColumnas
                
                # verificamos que el vecino este dentro de los limites de l amtriz
                if 0 <= direccionFilas < filas and 0 <= direccionColumnas < columnas:
                    total = total + matriz[direccionFilas][direccionColumnas]
            
            #guardamos la suma de los vecinos en la posicion correspondiente        
            resultado [fila][columna] = total
    return resultado

def imprimirMatriz(matriz):
    #por cada fila en la matriz, imprimimos
    for fila in matriz:
        print(fila)

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Matriz Original: ")
imprimirMatriz(matriz)
print("Matriz Suma de Vecinos: ")
imprimirMatriz(sumaVecinos(matriz))
'''

#Ejercicio 03
'''
def caminoMaximo(matriz):

    filas = len(matriz)
    columnas = len(matriz[0]) #columnas del primer elemento

    # suma maxima para llegar a columna y fila
    sumaMaxima = [[0] * columnas for _ in range(filas)]
    sumaMaxima[0][0] = matriz[0][0]

    # Llenar primera fila, solo viene de la izquierda
    for fila in range(1, columnas):
        sumaMaxima[0][fila] = sumaMaxima[0][fila - 1] + matriz[0][fila]
 
    # Llenar primera columna, solo viene de arriba
    for columna in range(1, filas):
        sumaMaxima[columna][0] = sumaMaxima[columna - 1][0] + matriz[columna][0]
 
    # Llenar el resto, elige el maximo del entre arriba o el de la izquierda
    for columna in range(1, filas):
        for fila in range(1, columnas):
            sumaMaxima[columna][fila] = max(sumaMaxima[columna - 1][fila], sumaMaxima[columna][fila - 1]) + matriz[columna][fila]
    
    recorrido = []

    columna, fila = filas - 1, columnas - 1

    while columna > 0 or fila > 0:
        recorrido.append((columna, fila))

        if columna == 0:
            fila -= 1
        
        elif fila == 0:
            columna -= 1
        
        elif sumaMaxima[columna -1][fila] > sumaMaxima[columna][fila - 1]:
            columna -= 1

        else:
            fila -= 1

    recorrido.append((0, 0))
    recorrido.reverse()

    return sumaMaxima[filas - 1][columnas - 1], recorrido

def imprimirMatriz(matriz):
    #por cada fila en la matriz, imprimimos
    for fila in matriz:
        print(fila)

matriz = [[5, 1, 7],
          [2, 8, 3],
          [1, 4, 9]]
print("Matriz Original: ")
imprimirMatriz(matriz)
suma, recorrido = caminoMaximo(matriz)
print(f"Suma maxima: {suma}")
print(f"Recorrido (fila, columna): {recorrido}")
'''

#Ejercicio 04
'''
def matrizSimetrica(matriz):

    numero = len(matriz)

    for columna in range(numero):
        for fila in range(numero):
            if matriz[columna][fila] != matriz[fila][columna]:
                return False
            
    return True

def imprimirMatriz(matriz):
    #por cada fila en la matriz, imprimimos
    for fila in matriz:
        print(fila)

matriz = [[1, 2, 3],
          [2, 5, 6],
          [3, 6, 9]]
print("Matriz Original: ")
imprimirMatriz(matriz)
print(f"La matriz es simestrica?: {matrizSimetrica(matriz)}")
'''

#Ejercicio 05
'''
def buscarIslas(matriz):

    #total de columnas y filas
    filas = len(matriz)
    columnas = len(matriz[0])

    visitado = [fila[:] for fila in matriz] #Crea una copia independiente de la matriz
    islas = 0

    def recorrerIsla(fila, columna):
        #nos permite ver si ta fue revisada
        if fila < 0 or fila >= filas or columna < 0 or columna >= columnas or visitado[fila][columna] == 0:
            return
        
        #contador de ya contados
        visitado[fila][columna] = 0

        recorrerIsla(fila + 1, columna)  # abajo
        recorrerIsla(fila - 1, columna)  # arriba
        recorrerIsla(fila, columna + 1)  # derecha
        recorrerIsla(fila, columna - 1)  # izquierda
    
    for fila in range(filas):
        for columna in range(columnas):
            
            #detectamos una isla
            if visitado[fila][columna] == 1:
                recorrerIsla(fila, columna)
                islas += 1

    return islas

def imprimirMatriz(matriz):
    #por cada fila en la matriz, imprimimos
    for fila in matriz:
        print(fila)

matriz = [[1, 1, 0, 0],
          [1, 0, 0, 1],
          [0, 0, 1, 1],
          [0, 0, 0, 0]]
print("Matriz:")
imprimirMatriz(matriz)
print(f"Número de islas: {buscarIslas(matriz)}")
'''

#Ejercicio 06
'''
def espiralMatriz(matriz):
    resultado = []
    
    # si la matriz esta vacia retornamos
    if not matriz:
        return resultado
    
    arriba, abajo = 0, len(matriz) - 1
    izquierda, derecha = 0, len(matriz[0]) - 1

    while arriba <= abajo and izquierda <= derecha:

        #recorremos de izquierda a derecha
        for columna in range(izquierda, derecha + 1):
            resultado.append(matriz[arriba][columna])
        arriba += 1

        #recorremos de arriba a abajo
        for fila in range(arriba, abajo + 1):
            resultado.append(matriz[fila][derecha])
        derecha -= 1

        #recorremos de derecha a izquierda
        if arriba <= abajo:
            for columna in range(derecha, izquierda - 1, -1):
                resultado.append(matriz[abajo][columna])
            abajo -= 1

        #recorremos de abajo a arriba
        if izquierda <= derecha:
            for fila in range(abajo, arriba - 1, -1):
                resultado.append(matriz[fila][izquierda])
            izquierda += 1

    return resultado


def imprimirMatriz(matriz):
    #por cada fila en la matriz, imprimimos
    for fila in matriz:
        print(fila)

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Matriz:")
imprimirMatriz(matriz)

#convierte cada numero a str, luego lo unimos y lo imprimimos
print(f"Recorrido en espiral: {' '.join(map(str, espiralMatriz(matriz)))}")
'''

#Ejercicio 07
'''
def validacionSudoku(matriz):

    def sinRepetidos(numeros):
        # filtramos los ceros
        celdas = [numero for numero in numeros if numero != 0]
        # si tenemos repetidos el conjunto tendra menos elementos
        return len(celdas) == len(set(celdas))
    
    # validamos cada fila
    for fila in matriz:
        if not sinRepetidos(fila):
            return False
    
    #validamos cada columna
    for indiceColumna in range(9):
        columnaActual = [matriz[indiceFila][indiceColumna] for indiceFila  in range(9)]
        if not sinRepetidos(columnaActual):
            return False
        
    #validamos sub matrices de 3x3
    for filaBloque in range(3):
        for columnaBloque in range(3):
            bloque = []
            for filaInterna in range(3):
                for columnaInterna in range(3):
                    fila = filaBloque * 3 + filaInterna
                    columna = columnaBloque * 3 + columnaInterna
                    bloque.append(matriz[fila][columna])
            if not sinRepetidos(bloque):
                return False
            
    return True

def imprimirMatriz(matriz):
    #por cada fila en la matriz, imprimimos
    for fila in matriz:
        print(fila)

matriz = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]


print("Matriz:")
imprimirMatriz(matriz)

print(f"¿El Sudoku es valido? {validacionSudoku(matriz)}")
'''

#Ejercicio 08
'''
def recorridoFloodFill(matriz, filaInicial, columnaInicial, valorNuevo):

    totalFilas = len(matriz)
    totalColumnas = len(matriz[0])

    #copiar matriz
    resultado = [fila[:] for fila in matriz]

    # si el valor en la celda inicial
    valorOriginal = resultado[filaInicial][columnaInicial]

    #devolvemos la matriz si el valor es el mismo
    if valorOriginal == valorNuevo:
        return resultado
    
    def reemplazarCeldas(filaActual, columnaActual):
        #si estamos fuera del limite, detenemos el recorrido
        if filaActual < 0 or filaActual >= totalFilas or columnaActual < 0 or columnaActual >= totalColumnas:
            return
        
        #si la celda no tiene valor, detenemos el recorrido
        if matriz[filaActual][columnaActual] != valorOriginal:
            return
        
        #reemplazamos el valor de la celda actual
        matriz[filaActual][columnaActual] = valorNuevo

        #revisamos las 4 direcciones
        reemplazarCeldas(filaActual + 1, columnaActual) #abajo
        reemplazarCeldas(filaActual - 1, columnaActual) #arriba
        reemplazarCeldas(filaActual, columnaActual + 1) #derecha
        reemplazarCeldas(filaActual, columnaActual - 1) #izquierda
    
    reemplazarCeldas(filaInicial, columnaInicial)
    return matriz

def imprimirMatriz(matriz):
    #por cada fila en la matriz, imprimimos
    for fila in matriz:
        print(fila)

matriz = [
    
    [1, 1, 1],
    [1, 2, 2],
    [1, 1, 2]

    ]


print("Matriz Original:")
imprimirMatriz(matriz)

print("Flood Fill desde (0,0) reemplazando con 9:")
imprimirMatriz(recorridoFloodFill(matriz, 0, 0, 9))
'''

#Ejercicio 09
'''
def buscarPalabra(matriz, palabraBuscada):

    totalFilas = len(matriz)
    totalColumnas = len(matriz[0])

    # direcciones posibles: abajo, arriba, derecha, izquierda
    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def recorrerLetras(filaActual, columnaActual, indiceLetra, celdasVisitadas, direccionActual):
        # si encotramos todas las letras, la palabra existe
        if indiceLetra == len(palabraBuscada):
            return True

        #si estamos fuera de los limites detenemos el recorrido
        if filaActual < 0 or filaActual >= totalFilas or columnaActual < 0 or columnaActual >= totalColumnas:
            return False

        # si la celda ya fue visitada, la saltamos
        if (filaActual, columnaActual) in celdasVisitadas:
            return False
        
        # si la letra no coincide, detenemos el recorrido
        if matriz[filaActual][columnaActual] != palabraBuscada[indiceLetra]:
            return False

        # Marcamos la celda como visitada
        celdasVisitadas.add((filaActual, columnaActual))

        # si ya tenemos direccion, seguimos solo en esa direccion
        if direccionActual is not None:
            movimientoFila, movimientoColumna = direccionActual
            palabraEncontrada = recorrerLetras(filaActual + movimientoFila, columnaActual + movimientoColumna, indiceLetra + 1, celdasVisitadas, direccionActual)
        else:
            # primera letra, exploramos las 4 direcciones posibles
            palabraEncontrada = any(
                recorrerLetras(filaActual + movimientoFila, columnaActual + movimientoColumna, indiceLetra + 1, celdasVisitadas, (movimientoFila, movimientoColumna))
                for movimientoFila, movimientoColumna in direcciones
            )

        # desmarcamos la celda para otros posibles caminos
        celdasVisitadas.remove((filaActual, columnaActual))

        return palabraEncontrada

    # intentamos iniciar la busqueda desde cada celda de la matriz
    for fila in range(totalFilas):
        for columna in range(totalColumnas):
            if recorrerLetras(fila, columna, 0, set(), None):
                return True

    return False

def imprimirMatriz(matriz):
    # por cada fila en la matriz, imprimimos
    for fila in matriz:
        print(fila)

matriz = [
        ['C', 'A', 'S', 'A'],
        ['X', 'Z', 'S', 'O'],
        ['Q', 'W', 'L', 'L']
          ]

print("Matriz:")
imprimirMatriz(matriz)
print(f"Buscar 'SOL': {buscarPalabra(matriz, 'SOL')}")
print(f"Buscar 'CAS': {buscarPalabra(matriz, 'CAS')}")
'''

#Ejercicio 10
'''
def comprimirMatriz(matriz):

    #guardamos el resultado
    resultado = []
    
    #aplanar matriz
    elementos = []
    for fila in matriz:
        for valor in fila:
            elementos.append(valor)

    # retornamos matriz vacia
    if not elementos:
        return resultado
    
    elementoActual = elementos [0]
    contadorRepeticiones = 1

    # recorremos desde segundo elemento
    for indice in range(1, len(elementos)):
        if elementos[indice] == elementoActual:
            contadorRepeticiones += 1
        else:
            # si es diferente, guardamos el grupo actual y empezamos uno nuevo
            resultado.append((elementoActual, contadorRepeticiones))
            elementoActual = elementos[indice]
            contadorRepeticiones = 1
    
    #agregamos el ultimo grupo
    resultado.append((elementoActual, contadorRepeticiones))

    return resultado

def imprimirMatriz(matriz):
    # por cada fila en la matriz, imprimimos su contenido
    for fila in matriz:
        print(fila)

matriz = [[1, 1, 1],
          [2, 2, 3]]

print("Matriz Original:")
imprimirMatriz(matriz)
print(f"Matriz Comprimida: {comprimirMatriz(matriz)}")
'''

#Ejercicio 11
'''
def transponerMatriz(matriz):

    totalFilas = len(matriz)
    totalColumnas = len(matriz[0])

    # la transpuesta tiene dimensiones invertidas, columnas por filas
    matrizTranspuesta = [[0] * totalFilas for _ in range(totalColumnas)]

    for indiceFila in range(totalFilas):
        for indiceColumna in range(totalColumnas):
            # la fila indiceFila columna indiceColumna pasa a ser fila indiceColumna columna indiceFila
            matrizTranspuesta[indiceColumna][indiceFila] = matriz[indiceFila][indiceColumna]

    return matrizTranspuesta

def imprimirMatriz(matriz):
    # por cada fila en la matriz, imprimimos
    for fila in matriz:
        print(fila)

matriz = [[1, 2, 3],
          [4, 5, 6]]

print("Matriz Original:")
imprimirMatriz(matriz)
print("Matriz Transpuesta:")
imprimirMatriz(transponerMatriz(matriz))
'''