'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 15: Correción del Examén III

Fecha de entrega: 02/06/2026

'''

#Ejercicio 01 - Recusividada de Pila
'''
def obtenerPrimeraPalabra(string):
    # Recorre la oración hasta encontrar un espacio
    palabra = ""
    for letra in string:
        if letra == " ":
            break
        palabra = palabra + letra
    return palabra


def obtenerRestoString(string, primeraPalabra):
    # Devuelve todo lo que viene después de la primera palabra
    longitudPrimeraPalabra = len(primeraPalabra)
    return string[longitudPrimeraPalabra + 1:]


def invertirString(string):
    # Caso base, si no hay espacio, es una sola palabra
    if " " not in string:
        return string

    # Separamos la primera palabra del resto
    primeraPalabra = obtenerPrimeraPalabra(string)
    restoString = obtenerRestoString(string, primeraPalabra)

    # caso recursivo, primero invertimos el resto, luego agregamos la primera
    return invertirString(restoString) + " " + primeraPalabra


# ejemplo de examen
#stringOriginal = "Python es poderoso"
stringOriginal = input("Ingrese un string: ")
stringInvertido = invertirString(stringOriginal)
print(stringInvertido)
'''

#Ejercicio 02 - Recusividada de Cola
'''
def listaOrdenada(listaNumeros):

    # Caso base, un solo elemento siempre esta ordenado
    if len(listaNumeros) == 1:
        return True

    primerNumero = listaNumeros[0]
    segundoNumero = listaNumeros[1]

    # Si el primero es mayor que el siguiente, no esta ordenada
    if primerNumero > segundoNumero:
        return False

    # Recursividad de cola, se retorna directamente la llamada recursiva
    # sin hacer ninguna operacion con el resultado
    return listaOrdenada(listaNumeros[1:])


# Ejemplos de examen
print(listaOrdenada([1, 2, 3, 4, 5]))  # True
#print(listaOrdenada([1, 3, 2, 4, 5]))  # False
#print(listaOrdenada([5, 4, 3, 2, 1]))  # False
'''

#Ejercicio 03 - Recusividada de Pila
'''
def elementoExistenteLista(elemento, listaNumeros):
    # Caso base, lista vacia, el elemento no existe
    if len(listaNumeros) == 0:
        return False

    # Si el primero coincide, existe
    if listaNumeros[0] == elemento:
        return True

    # Si no, buscar en el resto
    return elementoExistenteLista(elemento, listaNumeros[1:])


def sinDuplicados(listaNumeros):

    # Caso base, lista vacia, no hay nada que procesar
    if len(listaNumeros) == 0:
        return []

    primerElemento = listaNumeros[0]
    restoLista = listaNumeros[1:]

    # Procesar el resto primero
    listaSinDuplicados = sinDuplicados(restoLista)

    # Al regresar si el elemento ya existe en el resultado, lo descartamos
    if elementoExistenteLista(primerElemento, listaSinDuplicados):
        return listaSinDuplicados

    # Si no existe, lo agregamos al inicio
    return [primerElemento] + listaSinDuplicados


# ejemplos de examen
print(sinDuplicados([1, 2, 2, 3, 1, 4]))              # [1, 2, 3, 4]
print(sinDuplicados(["a", "b", "a", "c", "b"]))       # ["a", "b", "c"]
print(sinDuplicados([1, "hola", 1, "hola", 2]))       # [1, "hola", 2]

#solo que no salen en orden.
'''