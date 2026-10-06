'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Profesor: Bryan Hernández Sibaja

Laboratorio Semana 2: Práctica de Examen

Fecha de entrega: 22/03/2026
'''

#ejercicio 1
'''
def contadorKM ():
    
    #establecemos la tarifa base
    tarifaBase = 700

    #solicitamos la cantidad de km
    km = int(input("Ingrese la cantidad de kilometros: ")) 


    #establecemos el costo para los primero 5 km
    if km > 0 and km <= 5:

        costoKM = tarifaBase + (km * 650)

    #establecemos el costo para de 5 a 15 km
    elif km > 4 and km < 16:

        costoKM = tarifaBase + (km * 550)

        
    #establecemos el costo para mas de 15 km en adelante
    elif km > 15:
        costoKM = tarifaBase + (km * 500)
    
        
    #error en caso de que ingrese un numero negativo
    else:
        costoKM = 'ERROR'

    #mensaje para el usuario
    print("El costo de su tarifa es: ", costoKM)

    return (costoKM)

contadorKM()
'''


#ejercicio 2
'''
def aprobacion ():
    
    #solicitamos nombre
    nombre = input("Ingrese su nombre: ")
    
    #solicitamos salario
    salario = int(input("Ingrese su salario: "))

    #solicitamos años
    año = int(input("Cantidad de años de antiguedad: "))

    #solicitamos si posee deudas para cambiar el valor
    deudas = input("Posee deudas? (S/N) ")

    if deudas == "s":
        deudas = True
    else:
        deudas = False
        

    #codigo para las 3 condiciones verdaderas
    if salario >= 600000 and año >= 2 and deudas == False:
        print("Aprobado ")
    
    #codigo para 2 condiciones verdaderas
    elif salario > 600000 or año >= 2 or deudas == False and (salario > 600000 or año >= 2 or deudas == False):
        print("Aprobado con revision")

    #codigo para 1 condion verdadera
    elif salario > 600000 or año >= 2 or deudas == False:
        print("Rechazado, solo cumple con 1")

    #codigo para cuando no es ninguna
    elif salario < 600000 and año < 2 and deudas == True:
        print("Rechadado, no cumple ninguna")
    
    #por si el usuario ingresa algun otro valor
    else:
        print("ERROR")

    return ()

aprobacion()
'''


#ejercicio 3
'''
# solicitamos la contraseña
contraseña = input("Ingrese su contraseña: ")

#definimos la funcion
def evaluacion (contraseña):

    #en cada variable preguntamos si cierto caracter en especifico esta dentro de la contraseña para saber si cumplimos con la norma
    #de que contengo numeros, letras o caracteres especiales
    numeros = "0" in contraseña or "1" in contraseña or "2" in contraseña or "3" in contraseña or "4" in contraseña or "5" in contraseña or "6" in contraseña or "7" in contraseña or "8" in contraseña or "9" in contraseña

    letras = "a" in contraseña or "b" in contraseña or "c" in contraseña or "d" in contraseña or "e" in contraseña or "f" in contraseña or "g" in contraseña or "h" in contraseña or "i" in contraseña or "j" in contraseña or "k" in contraseña or "l" in contraseña or "m" in contraseña or "n" in contraseña or "o" in contraseña or "p" in contraseña or "q" in contraseña or "r" in contraseña or "s" in contraseña or "t" in contraseña or "u" in contraseña or "v" in contraseña or "w" in contraseña or "x" in contraseña or "y" in contraseña or "z" in contraseña

    caracter = "@" in contraseña or "#" in contraseña or "*" in contraseña or "!" in contraseña

    #validamos que la contraseña tenga mas de 10 caracteres como minimo
    if len(contraseña) > 9:

        #dentro de este if validamos que primero cumpla con las 3 condiciones, luego solo con dos, por ultimo solo con una
        #y ya para finalizar sino cumple con ninguna la contraseña es insegura
        if numeros and letras and caracter:
            print("Su contraseña es fuerte")
        elif (numeros and letras and not caracter) or (numeros and not letras and caracter) or (not numeros and letras and caracter):
            print("Su contraseña es media")
        elif (numeros and not letras and not caracter) or (not numeros and not letras and caracter) or (not numeros and letras and not caracter):
            print("Su contraseña es debil")
        else:
            print("Su contraseña es insegura")

    #validacion si no cumple con los 10 caracteres
    else:
        print("La contraseña debe ser igual o mayor a 10 caracteres")

    return (contraseña)

evaluacion(contraseña)
'''


#ejercicio 4
'''
def envio ():
    
    #ingresamos los kg
    kg = int (input("Ingrese los kg del paquete: "))

    #ingresamos el tipo de envio y definimos el costo del envio
    envio = input("Ingrese el tipo de envio ('normal' o 'express'): ")
    costoE = 0

    destino = False

    #ingresamos el destino y definimos el costo
    destino = input("Ingrese el destino ('dentro' o 'fuera') del pais: ")
    costoD = 0

    #if para asignar precio y manejo del booleano
    if destino == "fuera":
        destino = True
        costoD = 3500
    else:
        destino = False
        costoD = 0

    #if para asignar el precio del envio
    if envio == "express":
        costoE = 2000
    else:
        costoE = 0

    #if para hacer manejo de los precios segun los kgs
    if kg <= 1:
        precio = 2500
    
    elif kg > 1 and kg < 6:
        precio = 4000
    
    elif kg > 5:
        precio = 6500
    
    else:
        precio == "Error"

    precioTotal = precio + costoE + costoD

    print("El costo total del envio es: ", precioTotal)

    return (precioTotal)

envio ()
'''


#ejercicio 5
'''
#solicitamos las horas
horas = int(input("Ingrese el total de horas trabajadas: "))

#creamos la funcion recibiendo el parametro horas
def jornadaLaboral (horas):
    
    #dividimos horas entre 8 para saber cuantos dias tenemos
    diasL = horas // 8
    #sacamos las horas restantes que no pudieron ser horas
    horasRest = horas % 8
    #dividimos los dias en 5 para saber cunatas semanas tenemos
    semanasL = diasL // 5
    #sacamos los dias que no llegaron a ser semanas para saber cuantos dias tenemos
    horasRest = diasL % 5

    print("Semanas Laboradas: ", semanasL)
    print("Dias Laborados: ", diasL)
    print("Horas Laboradas: ", horasRest)

    #este if sirve para saber que tipo de jornada es
    if horas > 80:
        print("Jornada extendida")
    
    elif horas > 39 and horas < 81:
        print("Jornada normal")
    
    elif horas < 40:
        print("Jornada corta")

    elif horas <= 0:
        print("El numero debe ser mayor a 0")
    
    else:
        print("Error")

    return(horasRest, diasL, semanasL)

jornadaLaboral(horas)
'''


#ejercicio 6
'''
#solicitamos el nombre, monto y mebresia
nombre = input("Ingrese su nombre: ")

monto = int(input("Ingresa el monto de la compra: "))

membresia = input("Posee membresia? (s/n): ")

#definimos funcion
def membresiaT (nombre, monto, membresia):

    #manejamos la membresia como booleano dependiendo que ingrese el usuario
    if membresia == "s" or membresia == "S":
        membresia = True
    elif membresia == "n" or membresia == "N":
        membresia = False
    else:
        membresia = "ERROR"


    #manejo de la logica del monto 
    if membresia == True and monto > 50000:
        descuento = monto * 0.15
    elif membresia == True and monto <= 50000:
        descuento = monto * 0.08
    elif membresia == False and monto > 70000:
        descuento = monto * 0.05
    else:
        descuento = 0

    total = monto - descuento

    #imprimimos los datos
    print("El subtotal es: ", monto)
    print("El descuento es: ", int (descuento))
    print("El total es: ", int (total))

    return (nombre, monto, membresia)

membresiaT(nombre, monto, membresia)
'''


#ejercicio 7
'''
#solicitamos los valores de los lados
lado1 = int(input("Ingrese el valor del lado 1: "))
lado2 = int(input("Ingrese el valor del lado 2: "))
lado3 = int(input("Ingrese el valor del lado 3: "))

#definimos la funcion
def triangulo (lado1, lado2, lado3):
    
    #validamos que sea un numero mayor a 0 o sea un numero positivo
    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        
        #manejo de la logica para saber que tipo de triangulo es
        if lado1 == lado2 and lado2 == lado3:
            print("Es un triangulo equilatero")
        elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
            print("Es un triangulo isosceles")
        elif lado1 != lado2 and lado2 != lado3:
            print("Es un triangulo escaleno")
    #en caso de el numero no sea mayor a 0, da error
    else:
        print("ERROR")

    return

triangulo(lado1, lado2, lado3)
'''


#ejercicio 8
'''
#solicitamos el dato de consumo
consumoM = int(input("Ingrese el consumo mensual: "))

#definimos la funcion
def consuElec (consumoM):

    #if para saber si aplica o no el recargo
    if consumoM > 300:
        recargo = 2500
    else:
        recargo = 0
    
    #if para saber cuando es el monto que debe pagar
    if consumoM > 0 and consumoM <= 100:
        pago = consumoM * 3
    elif consumoM > 100 and consumoM <= 250:
        pago = consumoM * 5
    elif consumoM > 250:
        pago = consumoM * 7
    else:
        #en caso de que ingrese un valor negativo
        print("El monto debe ser mayor a 0")

    #sacamos el total
    total = pago + recargo

    #if para mostrar el consumo y mostrar el tipo de consumo
    if consumoM > 0 and consumoM <= 100:
        print("El monto total es de: ", total, " y el consumo fue bajo")
    elif consumoM > 100 and consumoM <= 250:
        print("El monto total es de: ", total, " y el consumo fue moderado")
    elif consumoM > 250:
        print("El monto total es de: ", total, " y el consumo fue alto")

    return (total)

consuElec(consumoM)
'''


#ejercicio 9
'''
#solicitamos el usuario, contra y codigo
usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")
codigo = int (input("Ingrese su codigo: "))

#definimos la funcion
def acceso (usuario, contraseña, codigo):
    
    #usamos este if para validar que primer se cumplan las 3 condiciones para el acceso
    if usuario == "admin" and contraseña == "python2026" and codigo == 123456:
        print("Acceso total")
    #ahora validamos que cumpla con la contraseña y usuario y tambien el codigo sea diferente al correcto
    elif usuario == "admin" and contraseña == "python2026" and codigo != 123456:
        print("Acceso parcial")
    #cualquier otro caso
    else:
        print("Acceso denegado")

    return (usuario, contraseña, codigo)

acceso(usuario, contraseña, codigo)
'''


#ejercicio 10
'''
def cine ():

    #solicitamos los valores de edad, cantidad de entradas y definimos al booleanos promocion
    edad = int(input("Ingrese su edad: "))
    
    entradas = int(input("Ingrese la cantidad de entradas: "))

    promocion = False

    #con este if filtramos que la edad no sea un numero negativo
    if edad > 0:

        #con este if definimos el precio de las entradas dandole limitaciones por edades
        if edad < 12:
            precio = 2500
        elif edad > 65:
            precio = 2000
        else:
            precio = 3500

        #preguntamos si es dia de promocion para cambiar el valor del booleano
        promocion = input("Es dia de promocion? (s/n): ")
        
        if promocion == "S" or promocion == "s":
            promocion = True
        
        elif promocion == "N" or promocion == "n":
            promocion = False
        
        #si ingresa otra letra que no sea lo que se le solicita da error
        else:
            print("ERROR, ingre un valor correcto (S/N)")
        
        #sacamos el monto total a pagar
        total = (entradas * precio)

        #ya sabiendo el monto a pagar si es dia de promocion, aplicamos el descuento solo si cumple con ambas validaciones
        if promocion == True and entradas >= 3:
            total = total + (total * 0.1)
        #sino entonces el precio queda igual
        else:
            total

        #mostramos el precio de forma entera para eliminar el decimal
        print("El monto a pagar es: ", int (total))

    #si usuario ingresa una edad menor a 0 entonces no funciona
    else:
        print("La edad debe ser mayor a 0")

    return

cine()
'''


#ejercicio 11
'''
palabra1 = input("Ingrese la primera palabra: ")

palabra2 = input("Ingrese la segunda palabra: ")

def comparacion (palabra1, palabra2):

    if len(palabra1) > len(palabra2):
        print("La palabra 1:", palabra1, "tienen una mayor longitud que la palabra 2:", len(palabra1))
    elif len(palabra1) < len(palabra2):
        print("La palabra 2:", palabra2, "tienen una mayor longitud que la palabra 1: ", len(palabra2)) 
    else:
        print("La palabras: ", palabra1, "y", palabra2, "tienen la misma longitud y no hay palabra con mayor longitud")


    if len(palabra1) == len(palabra2):
        print("La palabras: ", palabra1, "y", palabra2, "tienen la misma longitud", "Palabra 1: ", len(palabra1), "Palabra 2: ", len(palabra2))
    elif len(palabra1) != len(palabra2):
        print("La palabras: ", palabra1, "y", palabra2, "no tienen la misma longitud", "Palabra 1: ", len(palabra1), "Palabra 2: ", len(palabra2))



    if palabra1[0] == palabra2[0]:
        print("La palabras: ", palabra1, "y", palabra2, "tienen la misma letra al comienzo: ", "Palabra 1:", palabra1[0], "Palabra 2", palabra2[0])
    else:
        print("La palabras: ", palabra1, "y", palabra2, "no tienen la misma letra al comienzo: ", "Palabra 1:", palabra1[0], "Palabra 2", palabra2[0])
    


    if len(palabra1) == len(palabra2):
        print("La palabras: ", palabra1, "y", palabra2, "son exactamente iguales: ", "Palabra 1:", palabra1,"Palabra 2", palabra2)
    else:
        print("La palabras: ", palabra1, "y", palabra2, "no son exactamente iguales: ", "Palabra 1:", palabra1,"Palabra 2", palabra2)
    
    
    return (palabra1, palabra2)

comparacion(palabra1, palabra2)
'''


#ejercicio 12
'''
#definimos la funcion
def matricula ():
    
    #solicitamos los valores, el nombre y cursos
    nombre = input("Ingrese el nombre del estudiante: ")

    cursos = int (input("Ingrese la cantidad de cursos matriculados: "))

    #asignamos valores a las variables, booleano a la beca, costo y descuento
    beca = False

    costoC = 23000

    descuento = 0

    #solicitamos al usuario si posee beca y lo manejamos con un if para cambiarle el valor 
    beca = (input("Posee beca? (S/N): "))
    
    if beca == "S" or beca == "s":
        beca = True
    elif beca == "N" or beca == "n":
        beca = False


    #asignamos descuentos por cantidad de cursos matriculados
    if cursos >= 5:
        descuento = 0.1
    else:
        descuento = 0

    #asignamos descuentos por si posee beca o no
    if beca == True:
        descuento = descuento + 0.25
    else:
        descuento
    
    #sacamos el monto inicial sin rebajas
    subtotal = cursos * costoC
    
    #sacamos el total ya aplicando el descuento en caso de que tenga 
    total = subtotal - (subtotal * descuento)

    #pasamos el descuento a un numero entero para que se vea de mejor forma en la interfaz de la terminal
    descuento = descuento * 100


    #imprimimos el reporte de la matricula
    print("La matricula de: ", nombre)
    print("Matriculo un total de:" , cursos, "cursos")
    print("El subtotal de matricula es: ", subtotal)
    print("El descuento aplicado es: ", int(descuento),"%")
    print("El monto total es: ", int(total))


    #con este if manejas de que nivel fue la matricula
    if cursos > 0:

        if cursos <= 2:
            print("EL nivel de la matricula fue baja")
        elif cursos >= 3 and cursos <= 4:
            print("EL nivel de la matricula fue regular")
        elif cursos >= 5:
            print("El nivel de la matricula fue alto")

    else:
        print("Al menos debe matricular un curso")

    return (nombre, cursos, beca, subtotal, descuento, total)

matricula()
'''