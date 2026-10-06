'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 15: Laboratorio (Semana 15): POO

Fecha de entrega: 13/06/2026

'''

class Membresia:

    # NIVEL 1 ----------------------------------------------------------------------
    def __init__(self, numero, nombre):
        
        # Datos que el usuario nos da al crear la membresía
        self.numeroMembresia = numero
        self.nombreCliente = nombre

        # estos arrancan de 0 siempre, no los solicitamos al usuario
        self.sesionesDisponibles = 0
        self.totalSesionesCompradas = 0
        self.cantidadCompras = 0
        self.totalSesionesUsadas = 0
        self.cantidadUsos = 0

        # el estado siempre comienza como activa
        self.estado = "Activa"
    # ------------------------------------------------------------------------------

    # NIVEL 2 ----------------------------------------------------------------------
    def comprarSesiones(self, cantidad):
        
        #primero verificamos el estado
        if self.estado != "Activa":
            return "Membresia suspendida"
        
        # si esta activa
        self.sesionesDisponibles += cantidad
        self.totalSesionesCompradas += cantidad
        self.cantidadCompras += 1
        return f"Compra exitosa. Sesiones disponibles: {self.sesionesDisponibles}"
    
    def utilizarSesion(self):
        # primero verificamos si esta activa
        if self.estado != "Activa":
            return "Membresia suspendida"
        # segundo si tiene sesiones disponibles
        if self.sesionesDisponibles == 0:
            return "Sesiones insuficientes"
        
        # si pasa las validaciones 
        self.sesionesDisponibles -= 1
        self.totalSesionesUsadas += 1
        self.cantidadUsos += 1
        return "Sesion utilizada correctamente"
    
    def verSesionesDisponibles(self):
        # retornamos las sesiones disponibles
        return self.sesionesDisponibles 
    
    def verInformacionMembresia(self):
        # guardamos los datos para hacer el return solo de la variable de forma mas sencilla
        informacion = f"""
            Número de membresía : {self.numeroMembresia}
            Nombre del cliente  : {self.nombreCliente}
            Sesiones disponibles: {self.sesionesDisponibles}
            Total compradas     : {self.totalSesionesCompradas}
            Cantidad de compras : {self.cantidadCompras}
            Total utilizadas    : {self.totalSesionesUsadas}
            Cantidad de usos    : {self.cantidadUsos}
            Estado              : {self.estado}
            """
        return informacion
    
    def suspenderMembresia(self):
        self.estado = "Suspendida"
        return "La membresia fue suspendida"
    
    def activarMembresia(self):
        self.estado = "Activa"
        return "La membresia fue activada"
    
    # ------------------------------------------------------------------------------

# NIVEL 3 ----------------------------------------------------------------------
membresias = []

def buscarMebresias(numero):
    for membresia in membresias:
        if membresia.numeroMembresia == numero:
            return membresia
    #sino la encuentra retorna none
    return None 

def validarMembresia():
    while True:
        try:
            numero = int(input("Numero de membresia: "))
            return numero

        except ValueError:
            print("Error, opcion invalida. Ingrese un digito")

def validarNombre(nombre):
    # Verificamos si está vacio
    if nombre.strip() == "":
        print("El nombre no puede estar vacío")
        return False
    
    # Verificamos que solo tenga letras y espacios
    if not nombre.replace(" ", "").isalpha():
        print("El nombre solo puede contener letras")
        return False
    
    # Verificamos longitud minima
    if len(nombre.strip()) < 3:
        print("El nombre debe tener al menos 3 caracteres")
        return False
    
    # Si paso todas las validaciones
    return True

# menu principal
while True:

    print("╔════════════════════════════════════════════╗")
    print("║         Sistema de Gimnasio de TEC         ║")
    print("╠════════════════════════════════════════════╣")
    print("║   1. Crear Nueva Membresia                 ║")
    print("║   2. Comprar Sesiones                      ║")
    print("║   3. Utilizar Sesiones                     ║")
    print("║   4. Ver Sesiones Disponibles              ║")
    print("║   5. Ver Informacion de una Membresia      ║")
    print("║   6. Suspender Membresia                   ║")
    print("║   7. Activar Membresia                     ║")
    print("║   8. Ver Todas las Membresias              ║")
    print("║   0. Salir                                 ║")
    print("╚════════════════════════════════════════════╝")
    print("")

    # validacion de opcion menu
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            break

        except ValueError:
            print("Error, opcion invalida. Ingrese un digito")

    # en cada caso de menu
    match opcion:
        case 1:
            numero = validarMembresia()
            if buscarMebresias(numero) != None:
                print("Ya existe una membresia con ese numero")
            else:
                 while True:
                    nombre = input("Nombre del cliente: ")
                    if validarNombre(nombre):
                        break

            nueva = Membresia(numero, nombre)
            membresias.append(nueva)
            print("¡Membresia creada exitosamente!")


        case 2:
            numero = validarMembresia()
            membresia = buscarMebresias(numero)
            if membresia != None:
                cantidad = int(input("¿Cuantas sesiones desea comprar? "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0")
                else:
                    print(membresia.comprarSesiones(cantidad))
            else:
                print("Membresia no encontrada")

        case 3:
            numero = validarMembresia()
            membresia = buscarMebresias(numero)
            if membresia != None:
                print(membresia.utilizarSesion())
            else:
                print("Membresia no encontrada")

        case 4:
            numero = validarMembresia()
            membresia = buscarMebresias(numero)
            if membresia != None:
                print(f"Sesiones disponibles: {membresia.verSesionesDisponibles()}")
            else:
                print("Membresia no encontrada")

        case 5:
            numero = validarMembresia()
            membresia = buscarMebresias(numero)
            if membresia != None:
                print(membresia.verInformacionMembresia())
            else:
                print("Membresia no encontrada")

        case 6:
            numero = validarMembresia()
            membresia = buscarMebresias(numero)
            if membresia != None:
                if membresia.estado == "Suspendida":
                    print("La Membresia ya está suspendida")
                else:
                    print(membresia.suspenderMembresia())
            else:
                print("Membresia no encontrada")

        case 7:
            numero = validarMembresia()
            membresia = buscarMebresias(numero)
            if membresia != None:
                if membresia.estado == "Activa":
                    print("La Membresia ya está activada")
                else:
                    print(membresia.activarMembresia())
            else:
                print("Membresia no encontrada")

        case 8:
            if len(membresias) == 0:
                print("No hay membresias registradas")
            else:
                for membresia in membresias:
                    print(membresia.verInformacionMembresia())

        case 0:
            print("¡Hasta luego!")
            break

        case _:
            print("Error, la opcion debe estar entre 0 y 8")
            pass

# ------------------------------------------------------------------------------