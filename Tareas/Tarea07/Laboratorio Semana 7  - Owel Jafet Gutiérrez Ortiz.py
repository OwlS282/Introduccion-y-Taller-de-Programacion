#Portada
'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 9: Laboratorio Semana 7: Ciclos

Fecha de entrega: 19/04/2026
'''

#1
'''
Primero, definimos una funcion donde recibe como parametro un numero inicial y un numero final, tambien
dentro de la funcion definimos una lista, y recorremos el intervalo asignado por el usuario, donde por
cada numero verifica si es un numero primo, y lo añade a la lista.

Segundo, validamos el ingreso de los datos que sean validos y en caso de que no capturamos el error, y
solicitarmos los datos hasta que sean validos.

Tercero, por ultimo imprimimos la lista.

'''
'''
def numerosPrimos(numeroInicio, numeroFinal):

    listaNumeroPrimos = []

    for numero in range(numeroInicio, numeroFinal + 1, 1):
        
        numeroPrimo = True

        if numero <= 1:
            numeroPrimo = False

        for divisor in range(2, numero-1, 1):

            if numero % divisor == 0:
                numeroPrimo = False
                break

        if numeroPrimo == True:
            listaNumeroPrimos.append(numero)
        
    print(listaNumeroPrimos)
    return listaNumeroPrimos

while True:
    try:
        numeroInicio =  int(input("Ingrese el numero inicial: "))
        break

    except ValueError:
        print("Error, ingrese un numero")

while True:
    try:
        numeroFinal =  int(input("Ingrese el numero final: "))
        break
    
    except ValueError:
        print("Error, ingrese un numero")

numerosPrimos(numeroInicio, numeroFinal)
'''

#2
'''
Primero. creamos una funcion de validar contraseña donde creamos 4 booleanos, 3 de ellos para manejar las validaciones
de uso de una mayuscula, un numero y que cumpla con la longitud minima de 8.

Segundo, una vez validado determinamos si cimple con las 3 validaciones para determinar si es segura o no.
'''
'''
def validarContraseña(contraseña):
    
    tieneLongitud = False
    tieneMayusculas = False
    tieneNumeros = False
    seguridad =  False

    if len(contraseña) >= 8:
        tieneLongitud = True
    
    for letra in contraseña:
        if letra.isupper():
            tieneMayusculas = True
        if letra.isdigit():
            tieneNumeros = True
    
    if tieneLongitud == True and tieneMayusculas == True and tieneNumeros == True:
        seguridad = True
    else:
        seguridad = False

    if seguridad == True:
        print("La contraseña es segura")
    else:
        print("La contraseña no es segura")
    
    return seguridad

contraseña = input("Ingrese una contraseña: ")
validarContraseña(contraseña)
'''

#3
'''
Primero, validamos que el usuario ingrese un numero y sea valido.

Segundo, definimos una funcion que reciba un numero como parametro,
con la definicion de una lista, y la variable de anterior y actual,
y hacemos el calculo, donde definimos 0 y 1 como valores iniciales,
hacemos una nueva variable donde es la suma del anterior con el actual
y asi sucesivamente hasta que sea mayor al numero ingresado  
'''
'''
def serieFinobacci(numero):

    secuencia = [0, 1]
    anterior = 0
    actual = 1

    while actual < numero:
        nuevo = anterior + actual
        secuencia.append(nuevo)
        anterior = actual
        actual = nuevo
    
    if numero == 0:
        secuencia = [0]

    print(secuencia)
    return secuencia

while True:
    try:
        numero =  int(input("Ingrese un numero: "))
        break
    
    except ValueError:
        print("Error, ingrese un numero")

serieFinobacci(numero)
'''

#4
'''
Primero definimos la funcion y despues los contadores, al principio validamos que numero no sea la palabra fin,
despues validamos que sea un numero valido, y asi lo validamos hasta que nos salgamos del ciclo y mostramos
los contadores respectivos.
'''
'''
def contadorNumero ():
    contadorPositivos = 0 
    contadorCeros = 0
    contadorNegativos = 0

    while True:

        try:
            numero =  input("Ingrese un numero: ")

            if numero.lower() == "fin":
                break

            numero =  int(numero)

            if numero > 0:
                contadorPositivos = contadorPositivos + 1

            elif numero == 0:
                contadorCeros = contadorCeros + 1

            elif numero < 0:
                contadorNegativos = contadorNegativos + 1
        
        except ValueError:
            print("Error, ingrese un numero")

    print("Contador de Positivos: ", contadorPositivos)
    print("Contador de Ceros: ", contadorCeros)
    print("Contador de Negativos: ", contadorNegativos)
    return

contadorNumero()
'''

#5
'''
Primero, definimos una funcion que recibe como parametro el numero digitado por el usuario, en el cual
hacemos el calculo, definimos suma en 0, para hacer la suma y luego compararla con el numero que ingresamos.

Segundo, validamos la entrada del dato del usuario, y llamamos la funcion y verificamos si es true o false
para determinar si el numero es un numero perfecto
'''
'''
def numeroPerfecto(numero):

    suma = 0

    for divisor in range(1, numero-1):

        if numero % divisor == 0:
            suma = suma + divisor
    
    if suma == numero:
        return True
    else:
        return False
    

while True:
    try:
        numero =  int(input("Ingrese un numero: "))
        break
        
    except ValueError:
        print("Error, ingrese un numero")

if numeroPerfecto(numero) == True:
    print("Es un numero perfecto")
else:
    print("No es un numero perfecto")
'''

#6
'''
Primero, importamos la libreria random.

Segundo, definimos la funcion, asignamos un numero random del 1 al 10000 y lo guardamos
en la variable numeroOculto, luego damos pistas dependiendo si es mayor o menos, hasta
que adivine el numero.

Tercero, validamos que el dato ingresado sea correcto y no cause error.
'''
'''
import random
def adivinarNumero():

    numeroOculto = random.randint(1, 10000)
    
    while True:
        try:
            numero =  int(input("Ingrese un numero: "))
        
            if numero == numeroOculto:
                print("Adivinaste el numero")
                break

            else:
                if numero > numeroOculto:
                    print("El numero es menor")

                elif numero < numeroOculto:
                    print("El numero es mayor")

        except ValueError:
            print("Error, ingrese un numero")


adivinarNumero()
'''

#7
'''
Primero, creamos una funcion, definimos los contadores y solicitamos el texto.

Segundo, luego pasamos el texto todo a minusculas para un manejos mas sencillo 
y recorremos cada caracter validando que sea consonante o vocal y le sumamos 1
al contador, en caso contrario solo vamos al siguiente.

Tercero, imprimimos los contadores.

Cuarto, llamamos la funcion.
'''
'''
def conteoLetras():

    contadorVocales = 0 
    contadorConsonantes = 0
        
    texto =  input("Ingrese un texto: ")

    for caracter in texto.lower():

        if caracter.isalpha():
                   
            if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
                contadorVocales = contadorVocales + 1
                    
            else:
                contadorConsonantes =  contadorConsonantes + 1

    print("Contador de Vocales: ", contadorVocales)
    print("Contador de Consonantes: ", contadorConsonantes)

conteoLetras()
'''

#8
'''
Primero, definimos una funcion, y unas variables vacias, junto con booleano para determinar a si es palindromo.

Segundo, solcitamos la palabra y mediante un for le quitamos los espacios y la volvemos minuscula para luego
volver a guardarla.

Tercero, una vez ya limpia la palabra le hacemos el conteo de atras hacia adelante, y si es igual a la palabra
inicial u original entonces es palindromo.

Cuarto, por ultimo lo imprimimos y mostramos los datos.
'''
'''
def verificacionPalindromo():

    palabra = "" 
    palabraLimpia = ""
    palabraAlreves = ""
    palindromo = False
        
    palabra =  input("Ingrese una palabra: ")

    for caracter in palabra:
        if caracter != " ":
            palabraLimpia = palabraLimpia + caracter.lower()

    for caracter in range(len(palabraLimpia) - 1, -1, -1):
        palabraAlreves = palabraAlreves + palabraLimpia[caracter]

    if palabraLimpia == palabraAlreves:
        palindromo = True
    else:
        palindromo = False

    if palindromo == True:
        print("Palabra Original:", palabraLimpia)
        print("Palabra Alreves:", palabraAlreves)
        print("")
        print("Si es Palindromo")
    else:
        print("Palabra Original:", palabraLimpia)
        print("Palabra Alreves:", palabraAlreves)
        print("")
        print("No es Palindromo")

verificacionPalindromo()
'''

#9
'''
Primero, definimos la funcion con recibiendo dos numeros.

Segundo, creamos un meno que se maneja con los simbolos de las operaciones
solicitamos y validamos que solo se permitan opciones validas.

Tercero, depediendo la operacion seleccionada se ejecuta el codigo de su
respectiva operacion matematica

Cuarto, validamos los casos en las diviones donde el segundo numero sea 0
ya que no es posible una division.

Quinto, tambien los numero son validados para que sean de tipo entero y
no den error

Sexto, por ultimo primimos el resultado de la respectiva solucion
'''
'''
def calculadoraMatch(primerNumero, segundoNumero):
    while True:
        print("")
        print("'+' para Suma")
        print("'-' para Resta")
        print("'*' para Multiplicacion")
        print("'/' para Division")
        print("'//' para Division Entera")
        print("'%' para Modulo")
        print("")
        opcion = input("Ingrese el simbolo de la operacion que desea: ")

        match opcion:

            case "+":
                total = primerNumero + segundoNumero
                print("La suma de", primerNumero, "+", segundoNumero, "es:", total)
                break

            case "-":
                total = primerNumero - segundoNumero
                print("La resta de", primerNumero, "-", segundoNumero, "es:", total)
                break

            case "*":
                total = primerNumero * segundoNumero
                print("La multiplicacion de", primerNumero, "*", segundoNumero, "es:", total)
                break

            case "/":
                if segundoNumero == 0:
                    print("No se puede dividir entre 0")
                
                else:
                    total = primerNumero / segundoNumero
                    print("La divison de", primerNumero, "/", segundoNumero, "es:", total)
                    break
                
            case "//":
                if segundoNumero == 0:
                    print("No se puede dividir entre 0")
                
                else:
                    total = primerNumero // segundoNumero
                    print("La divison entera de", primerNumero, "//", segundoNumero, "es:", total)
                    break

            case "%":
                if segundoNumero == 0:
                    print("No se puede dividir entre 0")
                
                else:
                    total = primerNumero % segundoNumero
                    print("El modulo de", primerNumero, "%", segundoNumero, "es:", total)
                    break

            case _:
                print("Error, opcion incorrecta, por favor ingrese el signo de su operacion")


while True:
    try:
        primerNumero =  int(input("Ingrese un numero: "))
        break
    
    except ValueError:
        print("Error, ingrese un numero")

while True:
    try:
        segundoNumero =  int(input("Ingrese un numero: "))
        break
    
    except ValueError:
        print("Error, ingrese un numero")

calculadoraMatch(primerNumero, segundoNumero)
'''

#10
'''
Primero, definimos la funcion y tambien listas vacias.

Segundo, hacemos un ciclo infinito para que el usuario ingrese
numero de forma infinita hasta que escriba la palabra fin y
asi creamos una lista.

Tercero, recorremos la lista de los numeros, si el numero ya fue contado se omite,
inicializamos el contador en 0, recorremos nuevamente la lista para saber cuantas
veces aparace el numero actual, si coincide el contado se incrementa.

Cuarto, guardamos el numero que contamos para no repetir el proceso e imprimimos
el resultado.
'''
'''
def contadorFrecuencia():

    listaNumeros = []
    listaRepetidos = []

    while True:

        try:
            numero =  input("Ingrese un numero: ")

            if numero.lower() == "fin":
                break

            numero =  int(numero)

            listaNumeros.append(numero)
        
        except ValueError:
            print("Error, ingrese un numero")

    for numero in listaNumeros:
        if numero in listaRepetidos:
            continue

        contador = 0

        for repetido in listaNumeros:
            if repetido == numero:
                contador = contador + 1
        
        listaRepetidos.append(numero)
        print("El", numero, "aparece", contador, "de veces")

contadorFrecuencia()
'''

#11
'''
Primero, definimos la funcion con el recibimiento del parametro de numeroDecimal,

Segundo, definimos binario en vacio, y mientras numero sea mayor que 0 vamos a 
sacarle el modulo al numero, luego guardamos el binario y por ultimo le hace una
division absoluta a numeroDecimal para seguir con el siguiente digito.

Tercero, validamos que la entrada del numero sea correcta con la validacion de
try-except.
'''
'''
def conversionDecimalBinario(numeroDecimal):

    binario = ""
    
    while numeroDecimal > 0:

        residuo = numeroDecimal % 2
        binario = str(residuo) + binario
        numeroDecimal = numeroDecimal // 2
    
    print(binario)

    return binario

while True:
    try:
        numeroDecimal =  int(input("Ingrese un numero: "))
        break
    
    except ValueError:
        print("Error, ingrese un numero")

conversionDecimalBinario(numeroDecimal)
'''

#12
'''
Primero, definimos la funcion recibiendo el parametro de numero ya validado
de que sea un dato correcto.

Segundo, guardamos el numero original, el tamaño, y definimos la suma.

Tercero, mientras el numero sea mayor que 0, vamos a sacar el modulo, y
luego a realizar la suma, que es el digito con el exponente a la cantidad de
digitos del numero y lo suma, por ultimo le hacemos division absoluta
para eliminar ese digito y pasar con el siguiente.

Cuarto, si es igual retornamos un true o false y la suma, o sea una tupla

Quinto, llamamos a la funcion y luego, desempaquetamos la tupla para mostrar
los datos
'''
'''
def numeroArmstrong(numero):
    
    numeroOriginal = numero
    tamaño = len(str(numero))
    suma = 0
    
    while numero > 0:

        digito = numero % 10
        suma = suma + (digito ** tamaño)
        numero = numero // 10
    
    if suma == numeroOriginal:
        return True, suma
    
    else:
        return False, suma
    

while True:
    try:
        numero =  int(input("Ingrese un numero: "))
        break
    
    except ValueError:
        print("Error, ingrese un numero")

        
resultado, suma = numeroArmstrong(numero)

if resultado == True:
    print("Si es un numero Armstrong, El resultado es", suma)

else:
    print("No es un numero Armstrong, el resultado es", suma)
'''

#13
'''
Primero, definimos la funcion edificio que recibe como parametro un numero ya validado
de que sea un dato valido.

Segundo, primero imprimimos el techo y luego imprimimos el cuerpo del edificio de manera
decreciente hasta llegar a 0 y tambien imprimimos el numero del piso.

Tercero, validamos que el numero sea valido y llamamos la funcion.
'''
'''
def edificio(numero):
    
    print(" __")

    for piso in range(numero, 0, -1):
        print("|##| -> Piso", piso)


while True:
    try:
        numero =  int(input("Ingrese un numero: "))
        break
    
    except ValueError:
        print("Error, ingrese un numero")

edificio(numero)
'''

#14
'''
Primero, definimos una funcion que recibe como parametros una cadena principal y una subcadena.

Segundo, recorremos la cadena principal, definimos que coincide como true.

Tercero, dentro del for interno, recorremos la subcadena y si combinamos la cadena principal y
la subcadena y no coincide con lo recorrido en la subdecadena entonces coincide es false y
no salimos del ciclo.

Cuarto, si coincide retornamos true en caso contrario un false.

Quinto, solicitamos dos varibles con texto.

Sexto, dependiendo del valor que retorne la funcion determinamos el mensaje a mostrar, si es 
true, entonces la subcadena si existe en la cadena principal, de lo contrario la subcadena no
existe en el texto principal.
'''

def busquedaSubCadena (cadenaPrincipal, subcadena):

    for caracterPrincipal in range(len(cadenaPrincipal)):
    
        coincide =  True
        for caracterSecundario in range(len(subcadena)):

            if cadenaPrincipal[caracterPrincipal + caracterSecundario] != subcadena[caracterSecundario]:
                coincide = False
                break
        
        if coincide == True:
            return True
    
    return False
        

cadenaPrincipal = input("Ingrese una cadena: ")
subcadena = input("Ingrese una subcadena: ")

if busquedaSubCadena(cadenaPrincipal, subcadena) == True:
    print("La subcadena si existe en el texto")

else:
    print("La subcadena no existe en el texto")
