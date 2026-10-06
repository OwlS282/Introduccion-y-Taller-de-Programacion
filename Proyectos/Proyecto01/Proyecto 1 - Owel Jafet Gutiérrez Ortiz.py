'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 8: Proyecto #1

Fecha de entrega: 17/04/2026
'''

'''
- Importamos 'datetime' para el uso del tiempo.
- El 'os' para esperar tecla y limpiar consola. 
- Usamos 're' para la funcion de hacer match con alguna variable.
'''
import os
from os import system
import re
from datetime import datetime

'''
Definimos visitas y vehiculos como diccionarios para almacenar los datos guardos por el sistema
'''
visitas = []
vehiculos = []

### Funciones de Validacion
## Funciones de Registro
# Funciones Principales

### Funciones de Validacion el Registro del Visitante
'''
Validación de Nombre:

- Nombre no puede estar vacío
- Nombre no puede ser menor que 3 caracteres.
- Nombre no puede ser mayor que 30 caracteres.
- Nombre solo puede contener letras mayúsculas y minúsculas, tildes, la ñ y la ü.
- Nombre no puede contener doble espacio.

'''
def nombreValidacion (nombreVisitante):

    if nombreVisitante == "":
        print("El nombre no puede estar vacío")
        os.system("Pause")
        system("cls")
        return False

    if len(nombreVisitante) < 3:
        print("El nombre debe tener al menos 4 caracteres")
        os.system("Pause")
        system("cls")
        return False

    if len(nombreVisitante) > 31:
        print("El nombre no puede tener más de 30 caracteres")
        os.system("Pause")
        system("cls")
        return False

    if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$", nombreVisitante):
        print("El nombre solo puede contener letras")
        os.system("Pause")
        system("cls")
        return False

    if "  " in nombreVisitante:
        print("El nombre no puede tener espacios dobles")
        os.system("Pause")
        system("cls")
        return False

    print("Nombre registrado con éxito")
    os.system("Pause")
    system("cls")
    return True

'''
Validación de ID:

- Seleccionamos el tipo de identificacion y luego validamos el ID seleccionado
    
    - Cedula, TIM o Licencia:
        - ID debe ser un digito.
        - ID tiene que ser examente de 9 digitos.
        - ID no puede comenzar con 0.
    
    - DIMEX:
        - ID debe ser un digito.
        - ID tiene que ser examente de 12 digitos.
        - ID no puede comenzar con 0.
        
    - Pasaporte:
        - ID tiene que ser examente de 9 caracteres.
        - ID debe contener numero y letras
        - ID debe comenzar con una letra

'''
def idValidacion (tipo, idVisitante):

    if tipo == "1":
            
        while True:

            idVisitante = (input("Ingrese la cédula del visitante (123456789): "))

            if not idVisitante.isdigit():
                print("La cédula solo puede contener digitos del 0 al 9")
                os.system("Pause")
                system("cls")
                continue

            if len(idVisitante) != 9:
                print("La cédula debe de contener exactamente 9 digitos")
                os.system("Pause")
                system("cls")
                continue

            if idVisitante[0] == "0":
                print("La cédula no puede comenzar con 0")
                os.system("Pause")
                system("cls")
                continue
            
            print("ID registrado con éxito")
            os.system("Pause")
            system("cls")
            return idVisitante

    elif tipo == "2":
            
        while True:

            idVisitante = (input("Ingrese el TIM del visitante (123456789): "))

            if not idVisitante.isdigit():
                print("El TIM solo puede contener digitos del 0 al 9")
                os.system("Pause")
                system("cls")
                continue

            if len(idVisitante) != 9:
                print("El TIM debe de contener exactamente 9 digitos")
                os.system("Pause")
                system("cls")
                continue

            if idVisitante[0] == "0":
                print("El TIM no puede comenzar con 0")
                os.system("Pause")
                system("cls")
                continue
            
            os.system("Pause")
            system("cls")
            return idVisitante
        
    elif tipo == "3":
            
        while True:

            idVisitante = (input("Ingrese el DIMEX del visitante (123045607890): "))

            if not idVisitante.isdigit():
                print("El DIMEX solo puede contener digitos del 0 al 9")
                os.system("Pause")
                system("cls")
                continue

            if len(idVisitante) != 12:
                print("La cédula debe de contener exactamente 12 digitos")
                os.system("Pause")
                system("cls")
                continue
            
            if idVisitante[0] == 0:
                print("El DIMEX no puede comenzar con 0")
                os.system("Pause")
                system("cls")
                continue
            
            os.system("Pause")
            system("cls")
            return idVisitante

    elif tipo == "4":
            
        while True:

            idVisitante = (input("Ingrese el pasaporte del visitante (A12345678): "))

            if len(idVisitante) != 9:
                print("La cédula debe de contener exactamente 9 caracteres")
                os.system("Pause")
                system("cls")
                continue

            if not re.match(r"^[a-zA-Z0-9]+$", idVisitante):
                print("El pasaporte solo contiene letras y numeros")
                os.system("Pause")
                system("cls")
                continue
            
            if not re.match(r"^[a-zA-Z]+$", idVisitante[0]):
                print("El pasaporte debe comenzar con una letra")
                os.system("Pause")
                system("cls")
                continue
            
            os.system("Pause")
            system("cls")
            return idVisitante
        
    elif tipo == "5":
            
        while True:

            idVisitante = (input("Ingrese la licencia del visitante (123456789): "))

            if not idVisitante.isdigit():
                print("La licencia solo puede contener digitos del 0 al 9")
                os.system("Pause")
                system("cls")
                continue

            if len(idVisitante) != 9:
                print("La licencia debe de contener exactamente 9 digitos")
                os.system("Pause")
                system("cls")
                continue
            
            if idVisitante[0] == "0":
                print("La licencia no puede comenzar con 0")
                os.system("Pause")
                system("cls")
                continue
            
            os.system("Pause")
            system("cls")
            return idVisitante   
    else:
       
        print("Ingrese una opción válida")
        os.system("Pause")
        system("cls")
        return False

'''
Validación de Destino:

- Seleccionamos el tipo de destino y caso 1 (luego ingresamos el numero del apartamento) o caso 2 (luego seleccionamos unidad de destino)
    
    - Apartamento o Casa:
        - Destino debe ser un dígitos.
        - Destino tiene que ser exactamente de 3 dígitos.
        - Destino no puede ser 000.
    
    - Unidad Destino:
        - Destino debe ser una letra de la 'A' a la 'C'.
        - Destino tiene que ser exactamente de 1 caracter.

'''
def destinoValidacion(tipo):

    if tipo == "1":

        while True:

            destinoVisitante = (input("Ingrese el numero del apartamento de destino (001-100): "))

            if not destinoVisitante.isdigit():
                print("El numero de apartamento solo puede contener digitos del 0 al 9")
                os.system("Pause")
                system("cls")
                continue

            if len(destinoVisitante) != 3:
                print("El numero de apartamento debe de contener exactamente 3 digitos")
                os.system("Pause")
                system("cls")
                continue
            
            if destinoVisitante == "000":
                print("El numero de apartamento debe de ser igual o mayor a 001")
                os.system("Pause")
                system("cls")
                continue
            
            print("Destino registrado con éxito")
            os.system("Pause")
            system("cls")
            return "Apartamento", destinoVisitante

    elif tipo == "2":
            
        while True:

            destinoVisitante = (input("Ingrese el numero de casa de destino (001-100): "))

            if not destinoVisitante.isdigit():
                print("El numero de casa solo puede contener digitos del 0 al 9")
                os.system("Pause")
                system("cls")
                continue

            if len(destinoVisitante) != 3:
                print("El numero de casa debe de contener exactamente 3 digitos")
                os.system("Pause")
                system("cls")
                continue
            
            if destinoVisitante == "000":
                print("El numero de casa debe de ser igual o mayor a 001")
                os.system("Pause")
                system("cls")
                continue
            
            print("Destino registrado con éxito")
            os.system("Pause")
            system("cls")
            return "Casa", destinoVisitante
        
    elif tipo == "3":
            
        while True:

            destinoVisitante = (input("Ingrese la unidad de destino (A, B o C): "))

            if not re.match(r"^[a-cA-C]+$", destinoVisitante):
                print("Ingrese una letra válida")
                os.system("Pause")
                system("cls")
                continue
            
            if len(destinoVisitante) != 1:
                print("La unidad de destino debe de contener exactamente 1 letra")
                os.system("Pause")
                system("cls")
                continue
            
            print("Destino registrado con éxito")
            os.system("Pause")
            system("cls")
            return "Unidad", destinoVisitante
    else:
       
        print("Ingrese una opción válida")
        os.system("Pause")
        system("cls")
        return False

'''
Validación de Motivo:

- Motivo no puede estar vacío.
- Motivo no puede ser menor que 4 caracteres.
- Motivo no puede ser mayor que 30 caracteres.
- Motivo solo puede contener letras mayúsculas y minúsculas, tildes, numeros, la ñ y la ü.
- Motivo no puede contener doble espacio.

'''     
def motivoValidacion(motivoVisitante):

    if motivoVisitante == "":
        print("El motivo no puede estar vacío")
        os.system("Pause")
        system("cls")
        return False

    if len(motivoVisitante) < 3:
        print("El motivo debe tener al menos 4 caracteres")
        os.system("Pause")
        system("cls")
        return False

    if len(motivoVisitante) > 31:
        print("El motivo no puede tener más de 30 caracteres")
        os.system("Pause")
        system("cls")
        return False

    if not re.match(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s]+$", motivoVisitante):
        print("El motivo solo puede contener letras y numeros")
        os.system("Pause")
        system("cls")
        return False

    if "  " in motivoVisitante:
        print("El motivo no puede tener espacios dobles")
        os.system("Pause")
        system("cls")
        return False

    print("Motivo registrado con éxito")
    os.system("Pause")
    system("cls")
    return True

'''
Validación de Hora de Entrada:

- Hora de Entrada no puede estar vacío.
- Hora de Entrada debe seguir el formato de 2 numero '12', dos puntos ':' y 2 numeros nuevamente '34'.

    - Partimos Hora de Entrada en dos una parte antes de los dos puntos (:) y la otra despues y los llamamos, horas y minutos.
        - Horas no puede ser menos que 0 ni mayor que 23.
        - Minutos no puede ser menos que 0 ni mayor que 59. 

'''
def horaEntradaValidacion(horaEntrada):

    if horaEntrada == "":
        print("La hora de entrada no puede estar vacía")
        os.system("Pause")
        system("cls")
        return False
    
    if not re.match(r"^\d{2}:\d{2}$", horaEntrada):
        print("Formato de hora de entrada inválido, HH:MM")
        os.system("Pause")
        system("cls")
        return False
    
    horas, minutos = horaEntrada.split(":")

    if not (0 <= int(horas) <= 23):
        print("La hora de entrada debe estar entre las 00 y 23 horas")
        os.system("Pause")
        system("cls")
        return False
    
    if not (0 <= int(minutos) <= 59):
        print("Los minutos de la hora de entrada debe estar entre las 00 y 59 minutos")
        os.system("Pause")
        system("cls")
        return False

    print("Hora de entrada registrado con éxito")
    os.system("Pause")
    system("cls")
    return True

'''
Validación de Hora de Salida:

- Hora de Salida no puede estar vacío.
- Hora de Salida debe seguir el formato de 2 numero '12', dos puntos ':' y 2 numeros nuevamente '34'.

    - Partimos Hora de Salida en dos una parte antes de los dos puntos (:) y la otra despues y los llamamos, horas y minutos.
        - Horas no puede ser menos que 0 ni mayor que 23.
        - Minutos no puede ser menos que 0 ni mayor que 59. 

'''
def horaSalidaValidacion(horaSalida):
    
    if horaSalida == "":
        print("La hora de salida no puede estar vacía")
        os.system("Pause")
        system("cls")
        return False
    
    if not re.match(r"^\d{2}:\d{2}$", horaSalida):
        print("Formato de hora de salida inválido, HH:MM")
        os.system("Pause")
        system("cls")        
        return False

    horas, minutos = horaSalida.split(":")

    if not (0 <= int(horas) <= 23):
        print("La hora de salida debe estar entre las 00 y 23 horas")
        os.system("Pause")
        system("cls")        
        return False

    if not (0 <= int(minutos) <= 59):
        print("Los minutos de la hora de salida debe estar entre las 00 y 59 minutos")
        os.system("Pause")
        system("cls")
        return False

    print("Hora de salida registrado con éxito")
    os.system("Pause")
    system("cls")
    return True

'''
Validación de Estado:

- Seleccionamos el tipo de estado y luego asignamos el estado seleccionado.
'''
def estadoValidacion(tipo, estadoVisita):
    
    if tipo == "1":
        
        estadoVisita = "Pendiente"
        print("El estado del visitante es: ", estadoVisita)
        print("Estado registrado con éxito")
        os.system("Pause")
        system("cls")
        return estadoVisita
    
    if tipo == "2":
        
        estadoVisita = "Dentro"
        print("El estado del visitante es: ", estadoVisita)
        print("Estado registrado con éxito")
        os.system("Pause")
        system("cls")
        return estadoVisita    
    
    if tipo == "3":
        
        estadoVisita = "Finalizada"
        print("El estado del visitante es: ", estadoVisita)
        print("Estado registrado con éxito")
        os.system("Pause")
        system("cls")
        return estadoVisita
    
    if tipo == "4":
        
        estadoVisita = "Cancelada"
        print("El estado del visitante es: ", estadoVisita)
        print("Estado registrado con éxito")
        os.system("Pause")
        system("cls")
        return estadoVisita
                
    else:
       
        print("Ingrese una opción válida")
        os.system("Pause")
        system("cls")
        return False
###

### Funciones de Validacion del Registro del Vehiculo del Visitante
'''
Validación de Vehiculo (si posee o no):

- Seleccionamos si posee vehiculo o no, y validamos que solo ingrese opciones validas.
'''
def vehiculoValidacion(tipo):
    
    if not tipo.isdigit():
            print("La opcion solo puede contener digitos númericos")
            os.system("Pause")
            system("cls")
            return False
        
    if not (1 <= int(tipo) <= 2):
            print("La opcion solo puede ser del 1 o 2")
            os.system("Pause")
            system("cls")
            return False
    
    print("Registrando al vehiculo..,")
    os.system("Pause")
    system("cls")
    return True

'''
Validación de Placa de Vehiculo

- Ingresamos la placa y validamos el formato, si es placa con letras y numero o solo numeros.
    - Si solo ingresamos con numero debe seguir un formato 3 numero - 3 numero (123-456).
    - Si ingresamos letras debe ser 3 letras - 3 numero (ABC-123).
'''
def placaValidacion(placaVehiculo):

    if re.match(r"^\d{3}-\d{3}$", placaVehiculo):
        
        numeros, numeros = placaVehiculo.split("-")
        
        if not numeros.isdigit():
            print("Los digitos de la placa debe estar entre los valores 0 y 9")
            os.system("Pause")
            system("cls")
            return False
        return True
    
    elif re.match(r"^[A-Z]{3}-\d{3}$", placaVehiculo):

        letras, numeros = placaVehiculo.split("-")

        if not letras.isalpha():
            print("Las valores deben estat entre las letras de la A hasta la Z")
            os.system("Pause")
            system("cls")
            return False
    
        if not numeros.isdigit():
            print("Los digitos de la placa debe estar entre los valores 0 y 9")
            os.system("Pause")
            system("cls")
            return False
        
    else:

        print("Formato Inválido debe ser ABC-123 o 123-456")
        os.system("Pause")
        os.system("cls")    
        return False
    
    print("Placa registrada con éxito")
    os.system("pause")
    os.system("cls")
    return True

'''
Validación de Marca de Vehiculo:

- Marca no puede estar vacío
- Marca no puede ser menor que 3 caracteres.
- Marca no puede ser mayor que 30 caracteres.
- Marca solo puede contener letras mayúsculas y minúsculas, tildes, la ñ y la ü.
- Marca no puede contener doble espacio.

'''
def marcaValidacion(marcaVehiculo):

    if marcaVehiculo == "":
        print("La marca no puede estar vacía")
        os.system("Pause")
        system("cls")
        return False

    if len(marcaVehiculo) < 2:
        print("La marca debe tener al menos 3 caracteres")
        os.system("Pause")
        system("cls")
        return False

    if len(marcaVehiculo) > 31:
        print("La marca no puede tener más de 30 caracteres")
        os.system("Pause")
        system("cls")
        return False

    if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$", marcaVehiculo):
        print("La marca solo puede contener letras")
        os.system("Pause")
        system("cls")
        return False

    if "  " in marcaVehiculo:
        print("La marca no puede tener espacios dobles")
        os.system("Pause")
        system("cls")
        return False

    print("Marca registrada con éxito")
    os.system("Pause")
    system("cls")
    return True

'''
Validación de Modelo de Vehiculo:

- Modelo no puede estar vacío
- Modelo no puede ser menor que 3 caracteres.
- Modelo no puede ser mayor que 30 caracteres.
- Modelo solo puede contener letras mayúsculas y minúsculas, tildes, la ñ y la ü.
- Modelo no puede contener doble espacio.

'''
def modeloValidacion(modeloVehiculo):

    if modeloVehiculo == "":
        print("El modelo no puede estar vacío")
        os.system("Pause")
        system("cls")
        return False

    if len(modeloVehiculo) < 2:
        print("El modelo debe tener al menos 3 caracteres")
        os.system("Pause")
        system("cls")
        return False

    if len(modeloVehiculo) > 31:
        print("El modelo no puede tener más de 30 caracteres")
        os.system("Pause")
        system("cls")
        return False

    if not re.match(r"^[a-zA-Z0-9\s\-]+$", modeloVehiculo):
        print("El modelo solo puede contener letras, numero y guiones")
        os.system("Pause")
        system("cls")
        return False

    if "  " in modeloVehiculo:
        print("El modelo no puede tener espacios dobles")
        os.system("Pause")
        system("cls")
        return False

    print("Modelo registrado con éxito")
    os.system("Pause")
    system("cls")
    return True

'''
Validación de Color de Vehiculo:

- Color no puede estar vacío
- Color no puede ser menor que 3 caracteres.
- Color no puede ser mayor que 30 caracteres.
- Color solo puede contener letras mayúsculas y minúsculas, tildes, la ñ y la ü.
- Color no puede contener doble espacio.

'''
def colorValidacion(colorVehiculo):

    if colorVehiculo == "":
        print("El color no puede estar vacío")
        os.system("Pause")
        system("cls")
        return False

    if len(colorVehiculo) < 3:
        print("El color debe tener al menos 4 caracteres")
        os.system("Pause")
        system("cls")
        return False

    if len(colorVehiculo) > 21:
        print("El color no puede tener más de 20 caracteres")
        os.system("Pause")
        system("cls")
        return False

    if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$", colorVehiculo):
        print("El color solo puede contener letras")
        os.system("Pause")
        system("cls")
        return False

    if "  " in colorVehiculo:
        print("El color no puede tener espacios dobles")
        os.system("Pause")
        system("cls")
        return False

    print("Color registrado con éxito")
    os.system("Pause")
    system("cls")
    return True    

'''
Validación de Tipo de Vehiculo:

- Consultamos que ingrese la opcion correcta, y luego asignamos el tipo.

'''
def tipoValidacion(tipo, tipoVehiculo):

    if tipo == "1":
        
        tipoVehiculo = "Automóvil"
        print("El tipo de vehiculo del visitante es: ", tipoVehiculo)
        print("Tipo de vehiculo registrado con éxito")
        os.system("Pause")
        system("cls")
        return tipoVehiculo
    
    if tipo == "2":
        
        tipoVehiculo = "Motocicleta"
        print("El tipo de vehiculo del visitante es: ", tipoVehiculo)
        print("Tipo de vehiculo registrado con éxito")
        os.system("Pause")
        system("cls")
        return tipoVehiculo    
                
    else:
       
        print("Ingrese una opción válida")
        os.system("Pause")
        system("cls")
        return False
###

### Funciones de Validaciones de Menus
'''
Validación de Menu de Principal:

- Opcion tiene que ser digito
- Opcion tiene que estar entre 0 y 7

'''
def menuValidacion (opcion): 

    if not opcion.isdigit():
            print("La opcion solo puede contener digitos númericos")
            os.system("Pause")
            system("cls")
            return False
        
    if not (0 <= int(opcion) <= 7):
            print("La opcion solo puede ser del 0 al 7")
            os.system("Pause")
            system("cls")
            return False
            
    os.system("Pause")
    system("cls")
    return True

'''
Validación de Menu de Modificar:

- Opcion tiene que ser digito
- Opcion tiene que estar entre 0 y 5

'''
def menuModificarValidacion (opcion): 

    if not opcion.isdigit():
            print("La opcion solo puede contener digitos númericos")
            os.system("Pause")
            system("cls")
            return False
        
    if not (0 <= int(opcion) <= 5):
            print("La opcion solo puede ser del 0 al 5")
            os.system("Pause")
            system("cls")
            return False
    
    os.system("Pause")
    system("cls")
    return True

'''
Validación de Menu de Eliminar:

- Opcion tiene que ser digito
- Opcion tiene que estar entre 0 y 2

'''
def menuEliminarValidacion(opcion):

    if not opcion.isdigit():
            print("La opcion solo puede contener digitos númericos")
            os.system("Pause")
            system("cls")
            return False
        
    if not (0 <= int(opcion) <= 2):
            print("La opcion solo puede ser del 0 al 2")
            os.system("Pause")
            system("cls")
            return False
    
    os.system("Pause")
    system("cls")
    return True

'''
Validación de Menu de Mostrar:

- Opcion tiene que ser digito
- Opcion tiene que estar entre 0 y 3

'''
def menuMostrarValidacion(opcion):

    if not opcion.isdigit():
            print("La opcion solo puede contener digitos númericos")
            os.system("Pause")
            system("cls")
            return False
        
    if not (0 <= int(opcion) <= 3):
            print("La opcion solo puede ser del 0 al 3")
            os.system("Pause")
            system("cls")
            return False
    
    os.system("Pause")
    system("cls")
    return True
###

### Funciones Principales ###

# Funcion de Registro de Visitante
'''
Funcion de Registrar Visitas:

- Esta funcion pide los datos de las variables y llama a la funcion para validar cada dato. No pasa de pregunta hasta que sea dato sea correcto y valido y asi con cada una.
- Por ultimo guardamos los datos de la variable en un diccionario
'''
def registrarVisitante():
    
    while True:

        nombreVisitante = input("Ingrese el nombre del visitante: ")

        if nombreValidacion(nombreVisitante) == True:
            break
            
    while True:
        
        idVisitante = 0

        tipo = (input("Seleccione el tipo de ID del visitante (1. Cédula, 2. TIM, 3. DIMEX, 4. Pasaporte, 5. Licencia): "))
        
        #validacion de forma interna de que no este vacio
        if tipo == "":
            print("No puede estar vacío")
            os.system("Pause")
            system("cls")
            continue

        idVisitante = idValidacion(tipo, idVisitante)
        
        if idVisitante != False:
            break

    while True:

        tipo = (input("Seleccione el destino del visitante (1. Apartamento, 2. Casa, 3. Unidad de Destino): "))

        #validacion de forma interna de que no este vacio
        if tipo == "":
            print("No puede estar vacío")
            os.system("Pause")
            system("cls")
            continue

        resultado = destinoValidacion(tipo)

        if resultado != None:
            tipoDestino, destino = resultado
            break

    while True:

        motivoVisita = input("Ingrese el motivo del visitante: ")
        if motivoValidacion(motivoVisita) == True:
            break

    while True:

        horaEntrada = ""
        horaEntrada = input("Ingrese la entrada del visitante (HH:MM): ")

        if horaEntradaValidacion(horaEntrada) == True:
            break

    while True:

        horaSalida = ""
        horaSalida = input("Ingrese la salida del visitante (HH:MM): ")

        if horaSalidaValidacion(horaSalida) == True:
            break

    while True:

        estadoVisita = ""
        tipo = (input("Seleccione el estado del visitante (1. Pendiente, 2. Dentro, 3. Finalizada, 4. Cancelada): "))
        
        #validacion de forma interna de que no este vacio
        if tipo == "":
            print("No puede estar vacío")
            os.system("Pause")
            system("cls")
            continue

        estadoVisita = estadoValidacion(tipo, estadoVisita)

        if estadoVisita != False:
            break


    while True:
        
        tipo = input("Ingrese si posee vehiculo (1. Si, 2. No): ")

        if tipo == "":
            print("No puede estar vacío")
            os.system("Pause")
            system("cls")
            continue

        if vehiculoValidacion(tipo) == True:
            
            tipo = int(tipo)
  
            if tipo == 1:
                vehiculo = registroVehiculo()
                break
            else:
                vehiculo = None
                break

    visitante = {
        "nombre": nombreVisitante,
        "id": idVisitante,
        "tipoDestino": tipoDestino,
        "destino": destino,
        "motivo": motivoVisita,
        "horaEntrada": horaEntrada,
        "horaSalida": horaSalida,
        "estado": estadoVisita,
        "vehiculo": vehiculo
    }

    visitas.append(visitante)
    print("Visitante registrado con éxito")
    os.system("Pause")
    os.system("cls")
    return

## Funcion de Registro de Vehiculo de Visitante
'''
Funcion de Registrar Vehiculos de Visitantes:

- Esta funcion pide los datos de las variables y llama a la funcion para validar cada dato. No pasa de pregunta hasta que sea dato sea correcto y valido y asi con cada una.
- Por ultimo guardamos los datos de la variable en un diccionario
'''
def registroVehiculo():

    while True:

        placaVehiculo = input("Ingrese la placa del vehiculo del visitante (ABC-123 o 123-456): ")

        #validacion interna de que no sea vacia
        if placaVehiculo == "":
            print("No puede estar vacío")
            os.system("Pause")
            system("cls")
            continue

        if placaValidacion(placaVehiculo) == True:

            break

    while True:

        marcaVehiculo = input("Ingrese la marca del vehiculo del visitante: ")

        if marcaValidacion(marcaVehiculo) == True:
            break
    
    while True:

        modeloVehiculo = input("Ingrese el modelo del vehiculo del visitante: ")

        if modeloValidacion(modeloVehiculo) == True:
            break

    while True:
        
        colorVehiculo = input("Ingrese el color del vehiculo del visitante: ")
        
        if colorValidacion(colorVehiculo) == True:
            break

    while True:
        
        tipoVehiculo = ""
        tipo = (input("Seleccione el estado del visitante (1. Automóvil, 2. Motocicleta): "))

        #validacion interna de que no sea vacia
        if tipo == "":
            print("No puede estar vacío")
            os.system("Pause")
            system("cls")
            continue

        tipoVehiculo = tipoValidacion(tipo, tipoVehiculo)

        if tipoVehiculo != False:
            break

    vehiculo = {
        "placa": placaVehiculo,
        "marca": marcaVehiculo,
        "modelo": modeloVehiculo,
        "color": colorVehiculo,
        "tipo": tipoVehiculo
    }

    vehiculos.append(vehiculo)
    print("Vehiculo registrado con éxito")
    os.system("Pause")
    os.system("cls")
    return vehiculo

# Funcion de Consulta del Visitante
'''
Funcion de Consultar a los Visitantes:

- Validamos que haya visitas en el diccionario
- Esta funcion muestra todos los datos de los visitantes, incluyendo si cuentan o no con vehiculo.
'''
def consultarVisitas():

    if len(visitas) == 0:

        print("╔═══════════════════════════════════════════════════╗")
        print("║             No Hay Visitas Registradas            ║")
        print("╚═══════════════════════════════════════════════════╝")
        return
    
    else:

        for visitante in visitas:

            print("╔═══════════════════════════════════════════════════════════════════╗")
            print("║                        Visitas Registradas                        ║")
            print("╠═══════════════════════════════════════════════════════════════════╣")
            print(f"║ Nombre:    ", visitante["nombre"])
            print(f"║ ID:        ", visitante["id"])
            print(f"║ Destino:    {visitante['tipoDestino']} {visitante['destino']}")
            print(f"║ Motivo:    ", visitante["motivo"])
            print(f"║ Entrada:   ", visitante["horaEntrada"])
            print(f"║ Salida:    ", visitante["horaSalida"])
            print(f"║ Estado:    ", visitante["estado"])

            if visitante["vehiculo"] is None:
                print(f"║ Vehículo:   Sin vehículo")
                print("╚═══════════════════════════════════════════════════════════════════╝")
            
            else:
                print(f"║ Placa:     ", visitante["vehiculo"]["placa"])
                print(f"║ Marca:     ", visitante["vehiculo"]["marca"])
                print(f"║ Modelo:    ", visitante["vehiculo"]["modelo"])
                print(f"║ Color:     ", visitante["vehiculo"]["color"])
                print(f"║ Tipo:      ", visitante["vehiculo"]["tipo"])
                print("╚═══════════════════════════════════════════════════════════════════╝")

# Funcion de Modificar al Visitante
'''
Funcion de Modificar a los Visitantes:

- Validamos que haya visitas en el diccionario.
- Validamos que ingrese una opcion correcta.
- Validamos que no sean vistantes registrados con un estado diferente a 'Finalizada' o 'Cancelada'.
- En esta funcion primero nos muestra los visitantes existentes enumeranolos del 1 hasta el ultimo que exista, luego de seleccionar uno, 
nos redirige a un menu en el cual nos muestra que queremos cambiar, por ultimo seleccionamos lo que queremos modificar, pedimos el datos y
luego lo validamos que sea correcto para despues volver a guardarlo en el diccionario.
'''
def modificarVisitas():

    if len(visitas) == 0:

        print("╔═══════════════════════════════════════════════════╗")
        print("║             No Hay Visitas Registradas            ║")
        print("╚═══════════════════════════════════════════════════╝")
        return
    
    else:

        for numero, visita in enumerate(visitas, start=1):
            print("╔═════════════════════════════════════════════════════════════════════╗")
            print(f"║ Visita #{numero} - {visita['nombre']} - {visita['estado']}")
            print("╚═════════════════════════════════════════════════════════════════════╝")
        
        while True:
            
            print("")
            numero = input("Ingrese el numero de la visita a modificar: ")

            if not numero.isdigit():
                print("Ingrese solo números")
                continue

            numero = int(numero)

            if numero < 1 or numero > len(visitas):
                print("Número de visita inválido")
                continue

            break

        indice = numero -1 
        visita = visitas[indice]

        if visita['estado'] == "Finalizada" or visita['estado'] == "Cancelada":
            
            print("No se puede modificar una visita en estado 'Finalizada' o 'Cancelada' ")

        else:

            while True:
                os.system("cls")
                print("╔═══════════════════════════════════════════════════╗")
                print("║                  Modificar Visita                 ║")
                print("╠═══════════════════════════════════════════════════╣")
                print("║   1. Motivo                                       ║")
                print("║   2. Hora de Entrada                              ║")
                print("║   3. Hora de Salida                               ║")
                print("║   4. Destino                                      ║")
                print("║   5. Vehiculo                                     ║")
                print("║   0. Volver                                       ║")
                print("╚═══════════════════════════════════════════════════╝")
                print("")
                opcion = (input("Ingrese una opción: "))

                if menuModificarValidacion(opcion) == True:

                    if opcion == "1":

                        while True:

                            motivoVisita = input("Ingrese el motivo del visitante: ")
                            
                            if motivoValidacion(motivoVisita) == True:
                                visita["motivo"] = motivoVisita
                                print("Motivo de la visita modificada con éxito")
                                break
                    
                    elif opcion == "2":

                        while True:

                            horaEntrada = input("Ingrese la entrada del visitante (HH:MM): ")
                            
                            if horaEntradaValidacion(horaEntrada) == True:
                                visita["horaEntrada"] = horaEntrada
                                print("La hora de entrada de la visita ha sido modificada con éxito")
                                break

                    elif opcion == "3":

                        while True:

                            horaSalida = input("Ingrese la salida del visitante (HH:MM): ")
                            
                            if horaSalidaValidacion(horaSalida) == True:
                                visita["horaSalida"] = horaSalida
                                print("La hora de salida de la visita ha sido modificada con éxito")
                                break

                    elif opcion == "4":

                        while True:

                            destinoVisitante = ""
                            tipo = int(input("Seleccione el destino del visitante (1. Apartamento, 2. Casa, 3. Unidad de Destino): "))

                            destinoVisitante = destinoValidacion(tipo, destinoVisitante)
                            visita["destino"] = destinoVisitante
                            print("El destino de la visita ha sido modificado con éxito")
                            if destinoVisitante != False:
                                break


                    elif opcion == "5":

                        while True:

                            tipo = input("Ingrese si posee vehiculo (1. Si, 2. No): ")
                            
                            if vehiculoValidacion(tipo) == True:
                                
                                tipo = int(tipo)
                    
                                if tipo == 1:
                                    vehiculo = registroVehiculo()
                                    visita["vehiculo"] = vehiculo
                                    break
                                else:
                                    vehiculo = None
                                    break

                    elif opcion == "0":
                        return
                    
                else:
                    print("Error: por favor ingrese una opcion válida")

# Funcion de Eliminar al Visitante
'''
Funcion de Eliminar a los Visitantes:

- Validamos que haya visitas en el diccionario.
- Validamos que ingrese una opcion correcta.
- Validamos que no sean vistantes registrados con un estado diferente a 'Finalizada' o 'Cancelada'.
- En esta funcion primero nos muestra los visitantes existentes enumeranolos del 1 hasta el ultimo que exista, luego de seleccionar uno, 
nos redirige a un menu en el cual nos muestra que queremos hacer, eliminar o cancelar la vista, despues validamos preguntale si realmente
esta seguro de querer eliminar o cancelar la visita, por ultimo lo guardamos en el diccionario.
'''
def eliminarVisitas():

    if len(visitas) == 0:

        print("╔═══════════════════════════════════════════════════╗")
        print("║             No Hay Visitas Registradas            ║")
        print("╚═══════════════════════════════════════════════════╝")
        return
    
    else:

        for numero, visita in enumerate(visitas, start=1):
            print("╔═════════════════════════════════════════════════════════════════════╗")
            print(f"║ Visita #{numero} - {visita['nombre']} - {visita['estado']}")
            print("╚═════════════════════════════════════════════════════════════════════╝")
        
        while True:
            
            print("")
            numero = input("Ingrese el numero de la visita a eliminar: ")

            if not numero.isdigit():
                print("Ingrese solo números")
                continue

            numero = int(numero)

            if numero < 1 or numero > len(visitas):
                print("Número de visita inválido")
                continue

            break

        indice = numero -1 

        visita = visitas[indice]

        if visita['estado'] == "Finalizada" or visita['estado'] == "Cancelada":
            
            print("No se puede cancelar o eliminar una visita en estado 'Finalizada' o 'Cancelada' ")

        else:

            while True:

                os.system("cls")
                print("╔═══════════════════════════════════════════════════╗")
                print("║                  Eliminar Visitas                 ║")
                print("╠═══════════════════════════════════════════════════╣")
                print("║   1. Cancelar Visita                              ║")
                print("║   2. Eliminar Visita                              ║")
                print("║   0. Salir                                        ║")
                print("╚═══════════════════════════════════════════════════╝")
                print("")

                opcion = (input("Ingrese una opción: "))

                if menuModificarValidacion(opcion) == True:

                    if opcion == "1":

                        while True:
                            confirmacion = input("¿Está seguro? (s/n): ")

                            if confirmacion not in ["s", "n", "S", "N"]:
                                print("Ingrese solo s o n")
                                continue

                            if confirmacion.lower() == "s":
                                visita["estado"] = "Cancelada"
                                print("Visita cancelada con éxito")
                                break

                            elif confirmacion.lower() == "n":
                                print("Operación cancelada")
                                break
                    
                    elif opcion == "2":

                        while True:
                            confirmacion = input("¿Está seguro? (s/n): ")

                            if confirmacion not in ["s", "n", "S", "N"]:
                                print("Ingrese solo s o n")
                                continue

                            if confirmacion.lower() == "s":
                                visitas.pop(indice)
                                print("Visita eliminada con éxito")
                                break

                            elif confirmacion.lower() == "n":
                                print("Operación cancelada")
                                break

                    elif opcion == "0":
                        return
                    
                else:
                    print("Error: por favor ingrese una opcion válida")

# Funcion de Modificar al Visitante
'''
Funcion de Registrar Entrada a los Visitantes:

- Validamos que haya visitas en el diccionario.
- Validamos que el estado de la visita sea 'Pendiente' para poder realizar el cambio a 'Dentro'
- En esta funcion realiza el cambio de 'Pendiente' a 'Dentro', siempre y cuando se cumplan las validaciones.
'''
def registrarEntradaVisitas():
    
    if len(visitas) == 0:

        print("╔═══════════════════════════════════════════════════╗")
        print("║             No Hay Visitas Registradas            ║")
        print("╚═══════════════════════════════════════════════════╝")
        return
    
    else:

        for numero, visita in enumerate(visitas, start=1):
            print("╔═════════════════════════════════════════════════════════════════════╗")
            print(f"║ Visita #{numero} - {visita['nombre']} - {visita['estado']}")
            print("╚═════════════════════════════════════════════════════════════════════╝")
        
        while True:

            print ("")
            numero = input("Ingrese el numero de la visita a modificar: ")

            #validamos de forma interna que solo ingrese numeros
            if not numero.isdigit():
                print("Ingrese solo números")
                continue

            numero = int(numero)
            
            #validamos que la opciones enten dentro del rango
            if numero < 1 or numero > len(visitas):
                print("Número de visita inválido")
                continue

            break

        indice = numero -1 
        visita = visitas[indice]

        if visita['estado'] != "Pendiente":
            
            print("Solo se puede registrar entrada de visitas con estado: 'Pendiente' ")

        else:

            visita["estado"] = "Dentro"
            print("Entrada registrada con éxito")

    return

# Funcion de Modificar al Visitante
'''
Funcion de Registrar Salida a los Visitantes:

- Validamos que haya visitas en el diccionario.
- Validamos que el estado de la visita sea 'Dentro' para poder realizar el cambio a 'Finalizada'
- En esta funcion realiza el cambio de 'Dentro' a 'Finalizada', siempre y cuando se cumplan las validaciones.
'''
def registrarSalidaVisitas():
    
    if len(visitas) == 0:

        print("╔═══════════════════════════════════════════════════╗")
        print("║             No Hay Visitas Registradas            ║")
        print("╚═══════════════════════════════════════════════════╝")
        return
    
    else:

        for numero, visita in enumerate(visitas, start=1):
            print("╔═════════════════════════════════════════════════════════════════════╗")
            print(f"║ Visita #{numero} - {visita['nombre']} - {visita['estado']}")
            print("╚═════════════════════════════════════════════════════════════════════╝")
        
        while True:

            print("")
            numero = input("Ingrese el numero de la visita a modificar: ")

            #validamos de forma interna que solo ingrese numeros
            if not numero.isdigit():
                print("Ingrese solo números")
                continue

            numero = int(numero)

            #validamos que la opciones enten dentro del rango
            if numero < 1 or numero > len(visitas):
                print("Número de visita inválido")
                continue

            break

        indice = numero -1 
        visita = visitas[indice]

        if visita['estado'] != "Dentro":
            
            print("Solo se puede registrar salida de visitas con estado: 'Dentro' ")

        else:

            visita["estado"] = "Finalizada"
            print("Salida registrada con éxito")

    return

# Funcion de Modificar al Visitante
'''
Funcion de Consultas a los Visitantes:

- Validamos que haya visitas en el diccionario.
- Validamos que la opcion sea correcta.
- Esta funcion muestra un menu y llama a su respectiva funcion dependiendo de los datos que queramos visualizar.
'''
def consultasVisitas():

    if len(visitas) == 0:

        print("╔═══════════════════════════════════════════════════╗")
        print("║             No Hay Visitas Registradas            ║")
        print("╚═══════════════════════════════════════════════════╝")
        return
    
    else:

        opcion = 0

        while True:

            os.system("cls")
            print("╔═══════════════════════════════════════════════════╗")
            print("║               Consultar Visitas                   ║")
            print("╠═══════════════════════════════════════════════════╣")
            print("║   1. Visitantes Dentro del Edificio               ║")
            print("║   2. Visitantes con Vehiculo                      ║")
            print("║   3. Visitantes Registrados en Depto o Casa       ║")
            print("║   0. Salir                                        ║")
            print("╚═══════════════════════════════════════════════════╝")
            print("")

            opcion = (input("Ingrese una opción: "))

            if menuMostrarValidacion(opcion) ==  True:

                if opcion == "1":
                    dentroVisitas()
                    os.system("Pause")
                    os.system("cls")

                elif opcion == "2":
                    conVehiculoVisitas()
                    os.system("Pause")
                    os.system("cls")
            
                elif opcion == "3":
                    conApartamentoVisitas()
                    os.system("Pause")
                    os.system("cls")

                elif opcion == "0":
                    break            
            else:
                print("Error: por favor ingrese una opcion válida")
    return

## Funciona de Mostrar Vistantes Dentro del Edificio, esta dentro de la funcion de consultas
'''
SubFuncion de Consultar a los Visitantes Dentro del Edificio:

- Validamos que haya visitas en el diccionario
- Esta funcion muestra todos los datos de los visitantes que estan con el estado 'Dentro', incluyendo si cuentan o no con vehiculo.
'''
def dentroVisitas():
    
        if len(visitas) == 0:

            print("╔═══════════════════════════════════════════════════╗")
            print("║             No Hay Visitas Registradas            ║")
            print("╚═══════════════════════════════════════════════════╝")
            return
        
        else:

            encontrados = 0

            for visita in visitas:
                if visita['estado'] == "Dentro":
                    print("╔═══════════════════════════════════════════════════════════════════╗")
                    print("║                    Visitas Dentro del Edificio                    ║")
                    print("╠═══════════════════════════════════════════════════════════════════╣")
                    print(f"║ Nombre:    ", visita["nombre"])
                    print(f"║ ID:        ", visita["id"])
                    print(f"║ Destino:    {visita['tipoDestino']} {visita['destino']}")
                    print(f"║ Motivo:    ", visita["motivo"])
                    print(f"║ Entrada:   ", visita["horaEntrada"])
                    print(f"║ Salida:    ", visita["horaSalida"])
                    print(f"║ Estado:    ", visita["estado"])
                    print("╚═══════════════════════════════════════════════════════════════════╝")
                    encontrados += 1
            
            if encontrados == 0:
                print("No hay visitantes dentro del edificio")
        
        return

## Funciona de Mostrar Vistantes con Vehiculo, esta dentro de la funcion de consultas
'''
SubFuncion de Consultar a los Visitantes con Vehiculo:

- Validamos que haya visitas en el diccionario
- Esta funcion muestra todos los datos de los visitantes que cuentan con vehiculo.
'''
def conVehiculoVisitas():
    
        if len(visitas) == 0:

            print("╔═══════════════════════════════════════════════════╗")
            print("║             No Hay Visitas Registradas            ║")
            print("╚═══════════════════════════════════════════════════╝")
            return
        
        else:

            encontrados = 0

            for visita in visitas:
                if visita['vehiculo'] is not None:
                    print("╔═══════════════════════════════════════════════════════════════════╗")
                    print("║                        Visitas con Vehiculo                       ║")
                    print("╠═══════════════════════════════════════════════════════════════════╣")
                    print(f"║ Nombre:    ", visita["nombre"])
                    print(f"║ ID:        ", visita["id"])
                    print(f"║ Destino:    {visita['tipoDestino']} {visita['destino']}")
                    print(f"║ Motivo:    ", visita["motivo"])
                    print(f"║ Entrada:   ", visita["horaEntrada"])
                    print(f"║ Salida:    ", visita["horaSalida"])
                    print(f"║ Estado:    ", visita["estado"])
                    print(f"║ Placa:     ", visita["vehiculo"]["placa"])
                    print(f"║ Marca:     ", visita["vehiculo"]["marca"])
                    print(f"║ Modelo:    ", visita["vehiculo"]["modelo"])
                    print(f"║ Color:     ", visita["vehiculo"]["color"])
                    print(f"║ Tipo:      ", visita["vehiculo"]["tipo"])
                    print("╚═══════════════════════════════════════════════════════════════════╝")
                    encontrados += 1
            
            if encontrados == 0:
                print("No hay visitantes con vehiculo")
        
        return

## Funciona de Mostrar Vistantes dentro de un Apartamento en Especifico, esta dentro de la funcion de consultas
'''
SubFuncion de Consultar a los Visitantes Dentro del Edificio:

- Validamos que haya visitas en el diccionario
- Esta funcion muestra todos los datos de los visitantes que se encuentran dentro de una 'Apartamento' o 'Casa' en especifico.
'''
def conApartamentoVisitas():
    
        if len(visitas) == 0:

            print("╔═══════════════════════════════════════════════════╗")
            print("║             No Hay Visitas Registradas            ║")
            print("╚═══════════════════════════════════════════════════╝")
            return
        
        else:
            
            encontrados = 0

            while True:

                tipo = (input("Seleccione el destino del visitante a consultar (1. Apartamento, 2. Casa, 3. Unidad de Destino): "))
                
                #validamos internamente que no puede estar vacio
                if tipo == "":
                    print("No puede estar vacío")
                    os.system("Pause")
                    system("cls")
                    continue

                resultado = destinoValidacion(tipo)

                if resultado != None:
                    tipoDestino, destino = resultado
                    break

            for visita in visitas:
                if visita['tipoDestino'] == tipoDestino and visita['destino'] == destino:
                    print("╔═══════════════════════════════════════════════════════════════════╗")
                    print("║                  Visitas en Aparatamento o Casa                   ║")
                    print("╠═══════════════════════════════════════════════════════════════════╣")
                    print(f"║ Nombre:    ", visita["nombre"])
                    print(f"║ ID:        ", visita["id"])
                    print(f"║ Destino:    {visita['tipoDestino']} {visita['destino']}")
                    print(f"║ Motivo:    ", visita["motivo"])
                    print(f"║ Entrada:   ", visita["horaEntrada"])
                    print(f"║ Salida:    ", visita["horaSalida"])
                    print(f"║ Estado:    ", visita["estado"])
                    print("╚═══════════════════════════════════════════════════════════════════╝")
                    encontrados += 1
            
            if encontrados == 0:
                print("No se encontraron visitas para ese destino")
        
        return

# Funcion del Menu
'''
Funcion de Consultar a los Visitantes Dentro del Edificio:

- Validamos que la opcion hasta que sea correcta.
- Esta funcion nos brinda un manejo del menu.
'''
def menuPrincipal ():

    opcion = 0

    while True:

        print("╔═══════════════════════════════════════════════════╗")
        print("║   Sistema de Registro de Visitantes y Vehículos   ║")
        print("╠═══════════════════════════════════════════════════╣")
        print("║   1. Registrar Visitas                            ║")
        print("║   2. Consultar Visitas                            ║")
        print("║   3. Modificar Visitas                            ║")
        print("║   4. Cancelar Visitas                             ║")
        print("║   5. Registrar Entrada                            ║")
        print("║   6. Registrar Salida                             ║")
        print("║   7. Consultas y Reportes                         ║")
        print("║   0. Salir                                        ║")
        print("╚═══════════════════════════════════════════════════╝")
        print("")

        opcion = (input("Ingrese una opción: "))

        if menuValidacion(opcion) ==  True:

            if opcion == "1":
                os.system("cls")
                registrarVisitante()
                os.system("Pause")
                os.system("cls")

            elif opcion == "2":
                os.system("cls")
                consultarVisitas()
                os.system("Pause")
                os.system("cls")
        
            elif opcion == "3":
                os.system("cls")
                modificarVisitas()
                os.system("Pause")
                os.system("cls")
            
            elif opcion == "4":
                os.system("cls")
                eliminarVisitas()
                os.system("Pause")
                os.system("cls")
            
            elif opcion == "5":
                os.system("cls")
                registrarEntradaVisitas()
                os.system("Pause")
                os.system("cls")
            
            elif opcion == "6":
                os.system("cls")
                registrarSalidaVisitas()
                os.system("Pause")
                os.system("cls")
            
            elif opcion == "7":
                os.system("cls")
                consultasVisitas()
                os.system("Pause")
                os.system("cls")

            elif opcion == "0":
                print("Saliendo...")
                break            
        else:
            os.system("Pause")
            print("Error: por favor ingrese una opcion válida")
            os.system("cls")

### Funciones Principales ###

# Llamada a MenuPrincipal
'''
Llamamos a la funcion menuPricipal para comenzar con la ejecucion del sistema.
'''
menuPrincipal()