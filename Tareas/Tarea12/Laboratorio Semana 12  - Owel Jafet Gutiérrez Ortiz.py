'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 12: Laboratorio

Fecha de entrega: 24/05/2026

'''

#Impares - Pila
#Pares - Cola

# Ejercicio 1 - Suma recursiva de dígitos (PILA)
'''
def sumaDigitosPila(numero):
    #caso base, si el numero tiene un solo numero lo retornamos
    if numero < 10:
        return numero
    #caso recursivo, sumamos el ultimo con el resto
    return (numero % 10) + sumaDigitosPila(numero // 10)

#validamos que el numero sea un dato valido (positivo y sea numero)
while True:

    try:
        numero = int(input("Ingrese el numero: "))
        if numero <= 0:
            print("El numero no puede ser negativo o igual a 0")
        else:
            print("Numero registrado con éxito")
            print(f"La suma del numero: {numero} es {sumaDigitosPila(numero)}")
            break
            
    except ValueError:
        print("Error, solo se permiten digitos")
'''

# Ejercicio 2 - Invertir un String (COLA)
'''
def invertirStringCola(string, acumulador=""):
    #caso base, string vacio, retorna el acumulador con el resultado
    if not string:
        return acumulador
    #caso recursivo, toma el primer caracter y lo coloca al inicio del acumulador
    return invertirStringCola(string[1:], string[0] + acumulador)

#Validacion para que el string sea un dato valido
def validarString(string):

    if string == "":
        print("Error, no puede estar vacío")
        return False

    if len(string) < 3:
        print("Error, debe tener al menos 3 caracteres")
        return False

    if len(string) > 30:
        print("Error, no debe tener más de 30 caracteres")
        return False

    #usamos esta alternativa para permitir el uso del metodo isalpha, porque ese metodo no permite el uso de espacios, por ello 
    #utilizamos replace para cambiar los espacios por algo vacio y que no afecte la validacion
    if not string.replace(" ", "").isalpha():
        print("Error, debe tener solo letras")
        return False

    if "  " in string:
        print("Error, no puede tener espacios dobles")
        return False

    print("Registrado con éxito")
    return True

while True:
    string = input("Ingrese un string: ")
    if validarString(string) == True:
        print(f"El texto original es: {string} y su inverso es: {invertirStringCola(string)}")
'''

# Ejercicio 3 - Contar vocales (PILA)
'''
def contarVocalesPila(string):
    #caso base, string vacio, no hay vocales
    if not string:
        return 0
    #primera letra del string
    actual = string[0]
    #resto del string
    restante = string[1:]
    #verificamos si el actual es vocal
    vocal = 1 if actual.lower() in "aeiou" else 0

    #caso recursivo, sumamos vocal actual + vocales restantes
    return vocal + contarVocalesPila(restante)

#Validacion para que el string sea un dato valido
def validarString(string):

    if string == "":
        print("Error, no puede estar vacío")
        return False

    if len(string) < 3:
        print("Error, debe tener al menos 3 caracteres")
        return False

    if len(string) > 30:
        print("Error, no debe tener más de 30 caracteres")
        return False

    #usamos esta alternativa para permitir el uso del metodo isalpha, porque ese metodo no permite el uso de espacios, por ello 
    #utilizamos replace para cambiar los espacios por algo vacio y que no afecte la validacion
    if not string.replace(" ", "").isalpha():
        print("Error, debe tener solo letras")
        return False

    if "  " in string:
        print("Error, no puede tener espacios dobles")
        return False

    print("Registrado con éxito")
    return True

while True:
    string = input("Ingrese un string: ")
    if validarString(string) == True:
        print(f"El texto original es: {string} y tiene: {contarVocalesPila(string)} vocales")
'''

# Ejercicio 4 - Potencia Recursiva (COLA)
'''
def potenciaCola(base, exponente, acumulador=1):
    #caso base, exponente 0, cualquier numero elevado a 0 es 1
    if exponente == 0:
        return acumulador
    #caso recursivo, multiplicamos el acumulador por la base
    return potenciaCola(base, exponente - 1, acumulador * base)

#validaciones para que los datos sean correctos
while True:

    try:
        base = int(input("Ingrese la base: "))
        if base < 0:
            print("La base no puede ser negativo o igual a 0")
        else:
            print("Numero registrado con éxito")
            break
            
    except ValueError:
        print("Error, solo se permiten digitos")

while True:

    try:
        exponente = int(input("Ingrese el exponente: "))
        if exponente < 0:
            print("El exponente no puede ser negativo o igual a 0")
        else:
            print("Numero registrado con éxito")
            break
            
    except ValueError:
        print("Error, solo se permiten digitos")

print(f"La base es {base} y su exponente es {exponente}, el resultado es: {potenciaCola(base, exponente)}")
'''

# Ejercicio 5 - Máximo de una lista (PILA)
'''
lista = []

def maximoListaPila(lista):
    #caso base, lista con un elemento, ese el maximo
    if len(lista) == 1:
        return lista[0]
    #caso recursivo, compararar el primero con el resto para determinar si el maximo
    maximoResto = maximoListaPila(lista[1:])
    return lista[0] if lista[0] > maximoResto else maximoResto

while True:

        try:
            numero = (input("Ingrese un numero para la lista: "))
            if numero.lower() == "fin":
                print("Saliendo...")
                break
            else:
                numero = int(numero)
                lista.append(numero)
                print("Numeros registros con exito")
        
        except ValueError:
            print("Error, ingrese un numero")
print(f"El maximo de las lista es: {maximoListaPila(lista)}")
'''

# Ejercicio 6 - Buscar elemento en lista (COLA)
'''
lista = []

def buscarElementoCola(lista, elemento, indice=0):
    #caso base, se llego al final sin encontrar nada
    if indice >= len(lista):
        return False
    #caso base, elemento encontrado
    if lista[indice] == elemento:
        return True
    #caso recursivo: busca en el siguiente indice
    return buscarElementoCola(lista, elemento, indice + 1)

while True:

        try:
            numero = (input("Ingrese un numero para la lista: "))
            if numero.lower() == "fin":
                print("Saliendo...")
                break
            else:
                numero = int(numero)
                lista.append(numero)
                print("Numeros registros con exito")
        
        except ValueError:
            print("Error, ingrese un numero")

while True:

        try:
            elemento = int(input("Ingrese un numero para buscar en la lista: "))
            print(f"Buscando el elemento: {elemento}, {buscarElementoCola(lista, elemento)}!")
            break
        
        except ValueError:
            print("Error, ingrese un numero")
'''

# Ejercicio 7 - Contar apariciones (PILA)
'''
lista = []

def contarAparicionesPila(lista, valor):
    #caso base, lista vacia, ninguna aparacion
    if not lista:
        return 0
    #verificamos si el primer elemento es igual al valor buscado
    coincide = 1 if lista[0] == valor else 0

    #caso recursivo, sumamos coincidencia + apariciones en el resto
    return coincide + contarAparicionesPila(lista[1:], valor)

while True:

        try:
            numero = (input("Ingrese un numero para la lista: "))
            if numero.lower() == "fin":
                print("Saliendo...")
                break
            else:
                numero = int(numero)
                lista.append(numero)
                print("Numeros registros con exito")
        
        except ValueError:
            print("Error, ingrese un numero")

while True:

        try:
            valor = (input("Ingrese un numero para buscar en la lista: "))
            if valor.lower() == "fin":
                print("Saliendo...")
                break
            else:
                valor = int(valor)
                print(f"Buscando el elemento: {valor}, aparece un total de: {contarAparicionesPila(lista, valor)}")
        
        except ValueError:
            print("Error, ingrese un numero")
'''

# Ejercicio 8 - Decimal a Binario (COLA)
'''
def decimalABinarioCola(numero, acumulador=""):
    #caso base, numero es 0, retornar el resultado acumulado
    if numero == 0:
        return acumulador if acumulador else "0"
    #caso recursivo, el bit actual va al incicio del acumulador
    return decimalABinarioCola(numero // 2, str(numero % 2) + acumulador)

while True:

        try:
            numero = int(input("Ingrese un numero para convertir a binario: "))
            print(f"El numero: {numero}, en binario es: {decimalABinarioCola(numero)}")
            break
        
        except ValueError:
            print("Error, ingrese un numero")
'''

# Ejercicio 9 - Palíndromo Recursivo (PILA)
'''
def validacionPalidromo(texto):
    texto =  texto.replace(" ", "").lower()
    return esPalindromoPila(texto)

def esPalindromoPila(texto):
    #caso base, 0 o 1 caracteres siempre es palindromo
    if len(texto) <= 1:
        return True
    #si los extremos no coinciden, no es palindromo
    if texto[0] != texto[-1]:
        return False
    
    #caso recursivo, verificamos el texto si los extremos
    return esPalindromoPila(texto[1:-1])

#Validacion para que el string sea un dato valido
def validarString(string):

    if string == "":
        print("Error, no puede estar vacío")
        return False

    if "  " in string:
        print("Error, no puede tener espacios dobles")
        return False

    print("Registrado con éxito")
    return True

while True:
    string = input("Ingrese un string: ")
    if validarString(string) == True:
        print(f"El texto original es: {string}, el texto es un Palindromo? {esPalindromoPila(string)}!")
'''

# Ejercicio 10 - Eliminar duplicados consecutivos (COLA)
'''
def eliminarDuplicadoCola(string, acumulador=""):
    #caso base, string vacio, retornar el acumulador
    if not string:
        return acumulador
    
    #si el acumulador esta vacio o el ultimo caracter es diferente, agregar
    if not acumulador or string[0] != acumulador[-1]:
        return eliminarDuplicadoCola(string[1:], acumulador + string[0])
    
    # si es duplicado consecutivo, ignorarlo
    return eliminarDuplicadoCola(string[1:], acumulador)

#Validacion para que el string sea un dato valido
def validarString(string):

    if string == "":
        print("Error, no puede estar vacío")
        return False
    
    #usamos esta alternativa para permitir el uso del metodo isalpha, porque ese metodo no permite el uso de espacios, por ello 
    #utilizamos replace para cambiar los espacios por algo vacio y que no afecte la validacion
    if not string.replace(" ", "").isalpha():
        print("Error, debe tener solo letras")
        return False

    if "  " in string:
        print("Error, no puede tener espacios dobles")
        return False

    print("Registrado con éxito")
    return True

while True:
    string = input("Ingrese un string: ")
    if validarString(string) == True:
        print(f"Sin duplicados: {eliminarDuplicadoCola(string)}")
'''

# Ejercicio 11 - Suma de matrices (PILA)
'''
matriz = []

def sumaMatrizPila(matriz):
    
    #caso base, matriz vacia
    if not matriz:
        return 0 
    
    # Caso recursivo, sumar la primera fila + suma del resto de la matriz
    return sumaFilaPila(matriz[0]) + sumaMatrizPila(matriz[1:])

def sumaFilaPila(fila):
    #caso base, fila vacia
    if not fila:
        return 0
    
    # Caso recursivo, sumar el primer elemento + suma del resto de la fila
    return fila[0] + sumaFilaPila(fila[1:])

# cantidad de filas
filas = int(input("Ingrese la cantidad de filas de la matriz: "))

# recorremos filas
for fila in range(filas):
    listaFila = []

    # cantidad de columnas
    columnas = int(input(f"Ingrese la cantidad de numeros en la fila {fila+1}? "))
    
    #recorremmos cada columa para pedir los numero de la fila
    for columna in range(columnas):
        numero = int(input(f"  Numero [{fila+1}][{columna+1}]: "))
        listaFila.append(numero)

    # agregamos la fila completa a la matriz
    matriz.append(listaFila)

# suma total
print(f"La suma total de la matriz es: {sumaMatrizPila(matriz)}")
'''

# Ejercicio 12 - Recorrido recursivo de carpetas simuladas (COLA)
'''
def recorrerCarpetasCola(estructura, indice=0):
    
    #caso base, se recorrio toda la estructura
    if indice >= len(estructura):
        return
    
    elemento = estructura[indice]

    if isinstance(elemento, list):
        recorrerCarpetasCola(elemento, 0)
    
    else:
        #si es un archivo, imprimirlo
        print(elemento)

    # caso recursivo: continuar con el siguiente elemento
    recorrerCarpetasCola(estructura, indice + 1)

estructura = ["foto.png", ["docs", "tarea.docx", "pdf.pdf"], "video.mp4"]

print(f"archivos de la estructura: ")
recorrerCarpetasCola(estructura)
'''

# Ejercicio 13 - Aplanar listas anidadas (PILA)
'''
def aplanarListaPila(lista):
    #caso base, lista vacia
    if not lista:
        return []
    primer = lista[0]
    resto = lista[1:]

    #si el primer elemento es una lista aplanarla tammbien
    if isinstance(primer, list):
        return aplanarListaPila(primer) + aplanarListaPila(resto)
    
    #sino es lista, agregarlo y continuar con el resto
    return[primer] + aplanarListaPila(resto)

lista= [1, [2, [3, 4]], 5]
print(f"Lista Original: {lista}")
print(f"Lista Aplanada: {aplanarListaPila(lista)}")
'''

# Ejercicio 14 - Verificar Secuencia Ascendente (COLA)
'''
lista = []

def esAscendenteCola(lista, indice=0):
    #caso base, se llega al penultimo elemento, la secuencia es valida
    if indice >= len(lista) - 1:
        return True
    
    #si el elemento actual no es menor que el siguiente, no es ascendnte
    if lista[indice] >= lista[indice + 1]:
        return False
    
    #caso recursivo, verificar el resto
    return esAscendenteCola(lista, indice + 1)

while True:

        try:
            numero = (input("Ingrese un numero para la lista: "))
            if numero.lower() == "fin":
                print("Saliendo...")
                break
            else:
                numero = int(numero)
                lista.append(numero)
                print("Numeros registros con exito")
        
        except ValueError:
            print("Error, ingrese un numero")

print(f"La lista actual: {lista} es ascendente? {esAscendenteCola(lista)}!")
'''

# Ejercicio 15 - Secuencia Alternada de Pares e Impares (PILA)
'''
lista = []
def esAlternadaPila(lista):
    #caso base, 0 o 1 elemento, siempre es alternada
    if len(lista) <= 1:
        return True
    
    primero = lista[0]
    segundo = lista[1]

    #verificar si los dos primeros alterna (uno par y uno impar)
    if (primero % 2 == 0) == (segundo % 2 == 0):
        #ambos son pares o ambos son impares, alterna.
        return False
    
    #caso recursivo, verificar el resto de la lista
    return esAlternadaPila(lista[1:])
    
while True:

        try:
            numero = (input("Ingrese un numero para la lista: "))
            if numero.lower() == "fin":
                print("Saliendo...")
                break
            else:
                numero = int(numero)
                lista.append(numero)
                print("Numeros registros con exito")
        
        except ValueError:
            print("Error, ingrese un numero")

print(f"La lista actual: {lista} es alterna de pares e impares? {esAlternadaPila(lista)}!")
'''