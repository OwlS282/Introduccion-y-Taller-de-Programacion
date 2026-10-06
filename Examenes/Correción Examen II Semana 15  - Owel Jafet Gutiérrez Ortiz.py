'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 15: Correción del Examén II

Fecha de entrega: 02/06/2026

'''

#Ejercicio 01
'''
def validarParentesis(expresion):
    ListaParentisis = []

    for caracter in expresion:

        # Si es apertura, la guardamos en la lista ListaParentisis
        if caracter == "(" or caracter == "[" or caracter == "{":
            ListaParentisis.append(caracter)

        # Si es cierre, verificamos que coincida con la ultima apertura
        elif caracter == ")":
            if len(ListaParentisis) == 0 or ListaParentisis[-1] != "(":
                return False
            ListaParentisis.pop()

        elif caracter == "]":
            if len(ListaParentisis) == 0 or ListaParentisis[-1] != "[":
                return False
            ListaParentisis.pop()

        elif caracter == "}":
            if len(ListaParentisis) == 0 or ListaParentisis[-1] != "{":
                return False
            ListaParentisis.pop()

    # Al final, la lista de ListaParentisis debe estar vacia
    if len(ListaParentisis) == 0:
        return True
    else:
        return False


# Ejemplos del examen

#print(validarParentesis("3+[(2*5)-{8/(4-2)}]"))  # True
#print(validarParentesis("3+[(2*5)-{8/(4-2)]"))   # False

# ejemolos manual
expresion = input("Ingrese una Operacion Matematica con Parentesis: ")
print(validarParentesis(expresion))
'''

#Ejercicio 02
'''
def comprimirLista(listaElementos):
    diccionarioElementos = {}

    # numero de grupoNumeros en el diccionario
    grupoNumeros = 1

    # cuantas veces se repite el elemento actual
    contador = 1

    # Recorremos desde el segundo elemento (indice 1)
    for indice in range(1, len(listaElementos)):

        elementoActual = listaElementos[indice]
        elementoAnterior = listaElementos[indice - 1]

        # mismo elemento que el anterior
        if elementoActual == elementoAnterior:
            contador = contador + 1

        else:
            # el elemento cambió, guardamos el grupoNumeros
            diccionarioElementos[grupoNumeros] = {

                "elemento": elementoAnterior,
                "cantidad": contador
                }
            grupoNumeros = grupoNumeros + 1
            # reiniciamos el contador
            contador = 1

    ultimoElemento = listaElementos[-1]


    # Guardamos el ultimo grupoNumeros (el for no lo guarda solo)
    diccionarioElementos[grupoNumeros] = {
        
        "elemento": ultimoElemento,
        "cantidad": contador
        
        }
    
    return diccionarioElementos


# Ejemplos de el examen
listaElementos = ["a", "a", "b", "b", "b", "c", "a"]
diccionarioElementos = comprimirLista(listaElementos)

for grupoNumeros in diccionarioElementos:
    print(grupoNumeros, ":", diccionarioElementos[grupoNumeros])
'''

#Ejercicio 03
'''
def analizarLista(listaNumeros):

    # Validar que la lista no esté vacía
    if len(listaNumeros) == 0:
        print("La lista está vacia")
        return None

    # Inicializar variables con el primer elemento
    valorMaximo = listaNumeros[0]
    valorMinimo = listaNumeros[0]
    sumaAcumulada = 0

    # Recorrer la lista comparando cada elemento
    for numero in listaNumeros:

        if numero > valorMaximo:
            valorMaximo = numero

        if numero < valorMinimo:
            valorMinimo = numero

        # Acumular la suma
        sumaAcumulada = sumaAcumulada + numero

    # Calcular el promedio
    cantidadElementos = len(listaNumeros)
    promedio = sumaAcumulada / cantidadElementos
    promedioRedondeado = round(promedio, 2)

    resultado = {
        "maximo": valorMaximo,
        "minimo": valorMinimo,
        "promedio": promedioRedondeado
    }

    return resultado


# ejemplo del examen
listaNumeros = [8, 3, 15, 6, 2, 10]
resultado = analizarLista(listaNumeros)

for dato in resultado:
    print(dato, ":", resultado[dato])
'''