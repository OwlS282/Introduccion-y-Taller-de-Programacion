#Portada
'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 10: Primer Examen en Digital

Fecha de entrega: 27/04/2026
'''

# Ejercicio 01
'''
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

    print("Nombre registrado con éxito")
    return True

def evaluacionDesempeño():

    while True:
        nombre = input ("Ingrese su nombre: ").title()
        string =  nombre
        if validarString(string) == True:
            nombre = string
            break
    
    while True:
        try:
            productividad = int(input("Ingrese la productividad: "))
            if productividad < 0 or productividad > 100:
                print("Error, la productividad debe estar entre 0 y 100")
            else:
                print("Registrado con éxito")
                break
                        
        except ValueError:
            print("Error, solo se permiten digitos")

    while True:
        try:
            puntualidad = int(input("Ingrese la puntualidad: "))
            if puntualidad < 0 or puntualidad > 100:
                print("Error, la puntualidad debe estar entre 0 y 100")
            else:
                print("Registrado con éxito")
                break
                        
        except ValueError:
            print("Error, solo se permiten digitos")


    while True:
        try:
            trabajoEquipo = int(input("Ingrese el trabajo en equipo: "))
            if trabajoEquipo < 0 or trabajoEquipo > 100:
                print("Error, el trabajo en equipo debe estar entre 0 y 100")
            else:
                print("Registrado con éxito")
                break
                        
        except ValueError:
            print("Error, solo se permiten digitos")

    return nombre, productividad, puntualidad, trabajoEquipo
        
def calculoEvaluacion(nombre, productividad, puntualidad, trabajoEquipo):

    clasificacion = ""
    promedioEvaluacion = (productividad * 0.5) + (puntualidad * 0.25) + (trabajoEquipo * 0.25)

    if promedioEvaluacion >= 90:
        clasificacion = "Excelente"
    elif promedioEvaluacion >= 75:
        clasificacion = "Bueno"
    elif promedioEvaluacion >= 60:
        clasificacion = "Regular"
    else:
        clasificacion = "Deficiente"

    print(f"Hola, {nombre}, su promedio fue {promedioEvaluacion:.2f}, por lo que usted fue, {clasificacion}")

    return (promedioEvaluacion, clasificacion)

nombre, productividad, puntualidad, trabajoEquipo = evaluacionDesempeño()
calculoEvaluacion(nombre, productividad, puntualidad, trabajoEquipo)
'''

# Ejercicio 02
'''
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

    print("Nombre registrado con éxito")
    return True

def ingresarDatos():

    while True:
        nombre = input ("Ingrese su nombre: ").title()
        string =  nombre
        if validarString(string) == True:
            nombre = string
            break
    
    while True:
        try:
            horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
            if horasTrabajadas < 0:
                print("Error, las horas trabajadas no pueden ser negativas")
            else:
                print("Registrado con éxito")
                break
                        
        except ValueError:
            print("Error, solo se permiten digitos")

    while True:
        try:
            pagoPorHora = int(input("Ingrese el pago por hora: "))
            if pagoPorHora < 0:
                print("Error, el pago de por horas no pueden ser negativas")
            else:
                print("Registrado con éxito")
                break
                        
        except ValueError:
            print("Error, solo se permiten digitos")

    return nombre, horasTrabajadas, pagoPorHora

def calculoSalario(nombre, horasTrabajadas, pagoPorHora):

    if horasTrabajadas > 40:
        horasExtra = horasTrabajadas - 40
        salarioBase = 40 * pagoPorHora
        pagoHorasExtras = horasExtra * pagoPorHora * 1.5

    else:
        horasExtra = 0
        salarioBase = horasTrabajadas * pagoPorHora
        pagoHorasExtras = 0
    
    salario = salarioBase + pagoHorasExtras

    if salario > 500000:
        impuesto = salario * 0.1
        salario = salario - impuesto
    
    else:
        impuesto = 0
    
    print(f"Hola, {nombre}")
    print(f"Su salario base es: {salarioBase}")
    print(f"Su pago por horas extras es: {pagoHorasExtras}")
    print(f"Su impuesto es: {impuesto}")
    print(f"Su salario final es: {salario}")
     
nombre, horasTrabajadas, pagoPorHora = ingresarDatos()
calculoSalario(nombre, horasTrabajadas, pagoPorHora)
'''

# Ejercicio 03
'''
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

    print("Nombre registrado con éxito")
    return True

def ingresarDatos():

    while True:
        nombre = input ("Ingrese su nombre: ").title()
        string =  nombre
        if validarString(string) == True:
            nombre = string
            break
    
    while True:
        try:
            noches = int(input("Ingrese las noches: "))
            if noches < 0:
                print("Error, las noches no pueden ser negativas")
            else:
                print("Registrado con éxito")
                break
                        
        except ValueError:
            print("Error, solo se permiten digitos")

    while True:

        print("Seleccione el Tipo de Habitacion")
        print("")
        print("1. Sencillo")
        print("2. Doble")
        print("3. Suite")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-3): "))
                
            match opcion:

                case 1:
                    habitacion = "Sencilla"
                    print("Registrado con éxito")
                    break

                case 2:
                    habitacion = "Doble"
                    print("Registrado con éxito")
                    break

                case 3:
                    habitacion = "Suite"
                    print("Registrado con éxito")
                    break

                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 3!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")

    return nombre, noches, habitacion

def calcularReserva(nombre, noches, habitacion):

    if habitacion == "Sencilla":
        costoHabitacion = 25000 * noches

    elif habitacion == "Doble":
        costoHabitacion = 40000 * noches

    elif habitacion == "Suite":
        costoHabitacion = 70000 * noches

    if noches > 5:
        descuento = costoHabitacion * 0.1
    else:
        descuento = 0

    totalPagar = costoHabitacion - descuento

    if habitacion == "Suite":
        impuesto = totalPagar * 0.05
        totalPagar = totalPagar + impuesto
    else:
        impuesto = 0

    print(f"Hola, {nombre}")
    print(f"Costo base es {costoHabitacion}")
    print(f"Descuento es {descuento}")
    print(f"Impuesto suite es {impuesto}")
    print(f"Total a pagar es {totalPagar}")

    return totalPagar

nombre, noches, habitacion = ingresarDatos()
calcularReserva(nombre, noches, habitacion)
'''