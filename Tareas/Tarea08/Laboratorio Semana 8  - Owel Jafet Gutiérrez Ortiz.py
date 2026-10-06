#Portada
'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 10: Laboratorio Semana 8: Estructuras de Datos

Fecha de entrega: 26/04/2026
'''

# Ejercicio 01: Análisis avanzado de texto
# Descripción: Recibe un texto y realiza un análisis completo de sus palabras.
'''
Comentarios Ejercicios: 01

Primero, Recibimos un texto, que lo convertimos en minucula, despues le quitamos signos de puntuacion, luego lo separamos por palabras.

Segundo, verificamos mediante un for cuantas palabras iguales hay, luego que identificamos las palabras unicas las guardamos en un diccionario

Tercero, Determinamos la palabras mas larga, la palabra mas frecuente.

Cuarto, Determiminamos el top 3 de palabras frecuentes y lo guardamos en una variable, tambien guardamos en una variable la cantidad del
total de palabras y palabras unicas.

Quinto, Por ultimo imprimimos los resultados y llamamos la funcion.
'''
'''
#Codigo Ejercicio: 01

texto = input("Ingrese un texo: ")

def analisisTexto(texto):

    #convertirmos en minuscula el texto.
    textoMiniscula = texto.lower()

    #recorremos el texto y eliminamos los signos de puntacion.
    caracteresEspeciales = ".,;:¿?¡!"
    textoLimpio = ""
    for caracter in textoMiniscula:
        if caracter not in caracteresEspeciales:
            textoLimpio =  textoLimpio + caracter

    #separamos el texto en palabras
    palabras = textoLimpio.split()

    
    diccionarioPalabra = {}
    listaPalabrasUnicas = []
    palabraMasLarga = ""
    palabraMasFrecuente = ""
    cantidadFrecuencia = 0
    
    #contamos la cantidad de veces que aparece una palabra.
    for palabra in palabras:
        if palabra in diccionarioPalabra:
            diccionarioPalabra[palabra] = diccionarioPalabra[palabra] + 1
        else:
            diccionarioPalabra[palabra] = 1

    #guardamos en un diccionario las palabras con 1 de frecuencia.
    for palabra in diccionarioPalabra:
        if diccionarioPalabra[palabra] == 1:
            listaPalabrasUnicas.append(palabra)

    # determinamos la palabra mas larga
    for palabra in diccionarioPalabra:
        if len(palabra) > len(palabraMasLarga):
            palabraMasLarga = palabra

    # determinamos la palabara mas frecuente
    for palabra in diccionarioPalabra:
        if diccionarioPalabra[palabra] > cantidadFrecuencia:
            cantidadFrecuencia = diccionarioPalabra[palabra]
            palabraMasFrecuente = palabra

    #guardamos en una variable el resultado de un sorted donde se muestran solo 3 que las 3 palabras mas frecuentes
    palabrasFrecuentesTOP3 = sorted(diccionarioPalabra, key=diccionarioPalabra.get, reverse=True)[:3]    
    
    #guardamos la cantidad de palabras
    cantidadTotalPalabras = len(palabras)
    cantidadTotalPalabrasUnicas =  len(listaPalabrasUnicas)

    #imprimimos los resultados
    print("")
    print("Texto original:", texto)

    print("")
    print("Cantidad de Palabras Totales:", cantidadTotalPalabras)

    print("")
    print("Cantidad de Palabras Unicas:", cantidadTotalPalabrasUnicas)

    print("")
    print("TOP 3: Palabras Frecuentes:")
    for cantidad, palabra in enumerate (palabrasFrecuentesTOP3, 1):
        print(f"{cantidad}. {palabra}")

    print("")
    print("Palabra más Larga:", palabraMasLarga)

    print("")
    print("Palabra más Frecuente:", palabraMasFrecuente)

    print("")
    print("Palabras Unicas:")
    for cantidad, palabra in enumerate(listaPalabrasUnicas, 1):
        print(f"{cantidad}. {palabra}")

    print("")
    print("Todas las Palabras: ")
    print(f"{'Palabra':<30} {'Frecuencia'}")
    for palabra, frecuencia in diccionarioPalabra.items():
        #print("Palabra:", palabra, "Cantidad de frecuencia:", frecuencia)
        print(f"{palabra:<30} {frecuencia}")

analisisTexto(texto)
'''

# Ejercicio 02: Sistema de inventario
# Descripción: Implemente un sistema que administre un inventario de productos utilizando diccionarios.
'''
Comentarios Ejercicios: 02

Primero, desarrollamos el programa mediante funciones como mostrar menu, validar un string (que nos sirve para que un string cumpla con unos determinados parametros),
agregar productos, actualizar cantidad o precio, eliminar o consultar productos,

Segundo, cada funcion cumple con un propositvo, en menu, desplegamos el menu y validamos que la opcion para menejar el flujo del menu sea correcta. 

Tercero, en agregar productos manejas la parte de solicitar los datos, validarlos y guardarlos en un diccionario. tambien validamos que no hayan repetidos.

Cuarto, tenemos una subfuncion reutilizable que es para validar un string con ciertos parametros, en actualizar cantidad o precio, verificamos que no este vacio el inventario
y que el producto exista para efectuar el cambio. tambien validamos que no haya datos negativos.

Quinto, eliminar producto, validamos que el diccionario no este vacio, luego que el nombre coincida con uno y luego solicitamos una confirmacion extra para proceder con la
eliminacion del producto.

Sexto, consultar producto, validamos que el diccionario no este vacio, luego que el nombre coincida con uno y luego mostramos los datos de ese producto y si tiene menos de 5
en cantidad mostramos una alerta.

Septimo, mostrar inventario, validamos que el diccionario no este vacio y luego mostramos todos los producto dentro del inventario.
'''
'''
#declaramos un diccionario global
inventario = {}

def mostrarMenu ():
    
    while True:

        print("1. Agregar Producto")
        print("2. Actualizar Cantidad de Producto")
        print("3. Actualizar Precio de Producto")
        print("4. Eliminar Producto")
        print("5. Consultar Producto")
        print("6. Mostrar Inventario")
        print("7. Salir")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-7): "))
                
            match opcion:

                case 1:
                    agregarProductos()
                    
                case 2:
                    actualizarCantidad()

                case 3:
                    actualizarPrecio()

                case 4:
                    eliminarProducto()
                
                case 5:
                    consultarProducto()

                case 6:
                    mostrarInventario()

                case 7:
                    print("Saliendo...")
                    return
                    
                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 7!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")

def agregarProductos():

    while True:

        nombreProducto = input("Ingrese el nombre del producto: ").title()
        
        #validamos para que no exista producto duplicado
        if nombreProducto in inventario:
            print("Error, este producto ya existe")
            return

        else:
            string =  nombreProducto
            if validarString(string) == True:
                nombreProducto = string
                break


    while True:

        try:
            cantidadProducto = int(input("Ingrese la cantidad del producto: "))
            if cantidadProducto <= 0:
                print("La cantidad no puede ser negativa o igual a 0")
            else:
                print("Cantidad registrada con éxito")
                break
            
        except ValueError:
            print("Error, solo se permiten digitos")

    while True:

        try:
            precioProducto = float(input("Ingrese el precio del producto: "))
            if precioProducto <= 0:
                print("El precio no puede ser negativo o igual a 0")
            else:
                print("Precio registrado con éxito")
                break
            
        except ValueError:
            print("Error, solo se permiten digitos")

    #guardamos los datos del producto en el diccionario
    inventario[nombreProducto] = {"cantidad": cantidadProducto, "precio": precioProducto}
    print("Producto Registrado con exito!")
    
    return

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

def actualizarCantidad():
    
    if len(inventario) == 0:
        print("Error, no hay producto registrados")
        return
    
    else:
        nombreProducto = input("Ingrese el nombre del producto a buscar: ").title()

        if not nombreProducto in inventario:
            print("Error, este producto no existe")
            return

        else:

            while True:
                    try:
                        cantidadProducto = int(input("Ingrese la cantidad del producto: "))
                        if cantidadProducto <= 0:
                            print("La cantidad no puede ser negativa o igual a 0")
                        else:
                            inventario[nombreProducto]["cantidad"] = cantidadProducto
                            print("Cantidad registrada con éxito")
                            break
                        
                    except ValueError:
                        print("Error, solo se permiten digitos")

def actualizarPrecio():
    
    if len(inventario) == 0:
        print("Error, no hay producto registrados")
        return
    
    else:
        nombreProducto = input("Ingrese el nombre del producto a buscar: ").title()

        if not nombreProducto in inventario:
            print("Error, este producto no existe")
            return

        else:

            while True:
                    try:
                        precioProducto = float(input("Ingrese el precio del producto: "))
                        if precioProducto <= 0:
                            print("El precio no puede ser negativo o igual a 0")
                        else:
                            inventario[nombreProducto]["precio"] = precioProducto
                            print("Precio registrado con éxito")
                            break
                        
                    except ValueError:
                        print("Error, solo se permiten digitos")

def eliminarProducto():
    
    if len(inventario) == 0:
        print("Error, no hay producto registrados")
        return
    
    else:    
        nombreProducto = input("Ingrese el nombre del producto a buscar: ").title()

        if not nombreProducto in inventario:
            print("Error, este producto no existe")
            return

        else:
            pregunta = input("Esta seguro que desea eliminar el producto? (s/n)")
            match pregunta.lower():

                case "s":
                        del inventario[nombreProducto]
                        print("Producto eliminado con éxito")
                
                case "n":
                        print("Eliminacion cancelada")
                        return
                case _:
                        print("Error, Ingrese solo 's' o 'n'.")

def consultarProducto():

    if len(inventario) == 0:
        print("Error, no hay producto registrados")
        return
    
    else:
        nombreProducto = input("Ingrese el nombre del producto a buscar: ").title()

        if not nombreProducto in inventario:
            print("Error, este producto no existe")
            return

        else:
            #estructura de datos:
            #primero definimos la fila con los nombres y el espacio entre ellas.
            print(f"{'Nombre':<30}{'Cantidad':<30}{'Precio':<30}")
            #luego imprimimos los datos que van en cada fila con el mismo espacio
            print(f"{nombreProducto:<30}{inventario[nombreProducto]['cantidad']:<30}{inventario[nombreProducto]['precio']:.2f}")
            if inventario[nombreProducto]["cantidad"] < 5:
                print("")
                print(f"Stock bajo: {nombreProducto}")

def mostrarInventario():
    
    if len(inventario) == 0:
        print("Error, no hay producto registrados")
        return

    else:
        #estructura de datos:
        #primero definimos la fila con los nombres y el espacio entre ellas.
        print(f"{'Nombre':<30}{'Cantidad':<30}{'Precio':<30}")
        for producto, datos in inventario.items(): #diccionario.items nos permite obtener valores asocioados a un elemento.
            #luego imprimimos los datos que van en cada fila con el mismo espacio
            print(f"{producto:<30}{datos['cantidad']:<30}{datos['precio']:.2f}")#.2f signifa que solo se van a mostrar 2 decimales.
            if datos["cantidad"] < 5:
                print("")
                print(f"Stock bajo: {producto}")
    
mostrarMenu()
'''

# Ejercicio 03: Registro de ventas y reporte general
# Descripción: Cree un programa que registre ventas y genere estadísticas.
'''
Comentarios Ejercicios: 03

Primero, en la funcion registrar ventas solicitamos los datos, los  validamos, y los guardamos como diccionario dentro de una lista.

Segundo, en la funcion mostrar venta, validamos que haya ventas, y si las hay las mostramos todas.

Tercero, en mostrar reporte, realizamos el calculo de el ingreso total, o sea la suma de todas las ventas, el producto mas vendido o sea,
de mayor cantidad, categoria con mayor ingreso y por ultimo imprimimos lo resultado.

Cuarto, por ultimo tenenmos la funcion de menu, en la cual manejamos el flujo del menu.
'''
'''
#declaramos una lista global
ventas = []

def registrarVentas():
    
    while True:

        nombreProducto = input("Ingrese el nombre del producto: ").title()

        string =  nombreProducto
        if validarString(string) == True:
            nombreProducto = string
            break
    
    while True:

        print("Seleccione la Categoria del Producto")
        print("")
        print("1. Frutas y Verduras")
        print("2. Lácteos")
        print("3. Carnes y Pescados")
        print("4. Bebidas")
        print("5. Panadería")
        print("6. Otros")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-6): "))
                
            match opcion:

                case 1:
                    categoriaProducto = "Frutas y Verduras"
                    print("Registrado con éxito")
                    break

                case 2:
                    categoriaProducto = "Lácteos"
                    print("Registrado con éxito")
                    break

                case 3:
                    categoriaProducto = "Carnes y Pescados"
                    print("Registrado con éxito")
                    break

                case 4:
                    categoriaProducto = "Bebidas"
                    print("Registrado con éxito")
                    break

                case 5:
                    categoriaProducto ="Panadería"
                    print("Registrado con éxito")
                    break

                case 6:
                    categoriaProducto = "Otros"
                    print("Registrado con éxito")
                    break
                    
                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 6!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")

    while True:

        try:
            precioProducto = int(input("Ingrese el precio del producto: "))
            if precioProducto <= 0:
                print("El precio no puede ser negativo o igual a 0")
            else:
                print("Precio registrado con éxito")
                break
            
        except ValueError:
            print("Error, solo se permiten digitos")

    while True:

        try:
            cantidadProductoVendida = int(input("Ingrese la cantidad del producto: "))
            if cantidadProductoVendida <= 0:
                print("La cantidad no puede ser negativa o igual a 0")
            else:
                print("Cantidad registrada con éxito")
                break
            
        except ValueError:
            print("Error, solo se permiten digitos")

    ventas.append({
    
        "producto": nombreProducto,
        "categoria": categoriaProducto,
        "precio": precioProducto,
        "cantidad": cantidadProductoVendida,
        "total": precioProducto * cantidadProductoVendida
    
    })

    print("Producto Registrado con exito!")

def validarString (string):

    if string == "":
        print("Error, no puede estar vacío")
        return False

    if len(string) < 3:
        print("Error, debe tener al menos 3 caracteres")
        return False

    if len(string) > 15:
        print("Error, no debe tener más de 15 caracteres")
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

def mostrarVentas():

    if len(ventas) == 0:
        print("No hay ventas registradas")
        return
    
    else:
        print(f"{'Producto':<30}{'Categoria':<30}{'Precio':<30}{'Cantidad':<30}{'Total':<30}")
        for venta in ventas:
            print(f"{venta['producto']:<30}{venta['categoria']:<30}{venta['precio']:<30}{venta['cantidad']:<30}{venta['total']:.2f}")

def mostrarReporte():

    if len(ventas) == 0:
        print("No hay ventas registradas")
        return
    
    else:

        #ingreso total
        ingresoTotal = 0
        for venta in ventas:
            ingresoTotal = ingresoTotal + venta["total"]
        
        #producto mas vendidos
        productosVendidos = {}
        for venta in ventas:
            if venta["producto"] in productosVendidos:
                productosVendidos[venta["producto"]] = productosVendidos[venta["producto"]] + venta["cantidad"]
            else:
                productosVendidos[venta["producto"]] = venta["cantidad"]

        #categorias con mas ingreso
        categorias = {}
        for venta in ventas:
            if venta["categoria"] in categorias:
                categorias[venta["categoria"]] = categorias[venta["categoria"]] + venta["total"]
            else:
                categorias[venta["categoria"]] = venta["total"]


        #guardamos en una variable la categoria mas vendida y el producto mas vendido
        categoriaMasIngresos = 0
        maxIngreso = 0
        for categoria in categorias:
            if categorias[categoria] > maxIngreso:
                maxIngreso = categorias[categoria]
                categoriaMasIngresos = categoria

        masVendido = ""
        maxCantidad = 0
        for producto in productosVendidos:
            if productosVendidos[producto] > maxCantidad:
                maxCantidad = productosVendidos[producto]
                masVendido = producto

        #venta mayores a un monto en especifico
        ventasConsultadas = 0
        monto = float(input("Ingrese el monto minimo: "))
        print(f"{'Producto':<30}{'Categoria':<30}{'Total':<30}")
        for venta in ventas:
            if venta["total"] > monto:
                print(f"{venta['producto']:<30}{venta['categoria']:<30}{venta['total']:.2f}")
                ventasConsultadas = ventasConsultadas + 1
        
        if ventasConsultadas == 0:
            print("Error, no existen ventas con ese monto")
        
        print("")
        print("Ingreso total:", ingresoTotal)
        print("")
        print("Producto más vendido:", masVendido)
        print("")
        print("Categoría con más ingresos:", categoriaMasIngresos)
        print("")

def mostrarMenu():
    
    while True:

        print("1. Registrar Venta")
        print("2. Mostrar Venta")
        print("3. Ver Reporte")
        print("4. Salir")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-4): "))
                
            match opcion:

                case 1:
                    registrarVentas()
                    
                case 2:
                    mostrarVentas()

                case 3:
                    mostrarReporte()

                case 4:
                    print("Saliendo...")
                    return
                    
                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 4!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")
    
mostrarMenu()
'''

# Ejercicio 04: Clasificación de estudiantes por rendimiento
# Descripción: Elabore un programa para clasificar estudiantes según sus notas.
'''
Comentarios Ejercicios: 04

Primero, en la funcion agregar estudiante, los datos para que sean validos y luego los guardamos, como el nombre
que cumpla con ciertos parametros y la nota que este dentro de 1 a 100.

Segundo, en la funcion clasificar estudiante, validamos que que haya registro de estudiantes, una vez validado
realizamos el calculo de agregarlos a un diccionario que contiene listas dependiendo de su nota, tambien calculamos
el promedio. Tambien sacamos la nota mas alta y mas baja la guardamos en una variable cada una. Por ultimo
hacemos un print con los datos y tratando de mejorar la estructura de los datos.

Tercero, mostrar menu nos sirve para manejar el flujo del menu.
'''
'''
#definimos una lista global donde van las tuplas
estudiantes = []

def agregarEstudiantes():

    while True:

        nombreEstudiante = input("Ingrese el nombre del estudiante: ").title()
        string =  nombreEstudiante
        if validarString(string) == True:
            nombreEstudiante = string
            break
    
    while True:

        try:
            notaEstudiante = float(input("Ingrese la nota del estudiante: "))
            if notaEstudiante < 0 or notaEstudiante > 100:
                print("La nota no puede ser negativa y tiene que ser de 1 a 100")
            else:
                print("Nota registrada con éxito")
                break
            
        except ValueError:
            print("Error, solo se permiten digitos")

    estudiantes.append((nombreEstudiante, notaEstudiante))

def clasificarEstudiantes():
    
    if len(estudiantes) == 0:
        print("Error, no hay estudiantes registrados!")
        return
    
    else:

        clasificacion = {

            "Excelente": [],
            "Bueno": [],
            "Regular": [],
            "Reprobado": []

        }

        for estudiante in estudiantes:
            nombre = estudiante[0]
            nota = estudiante[1]

            if nota >= 90:
                clasificacion["Excelente"].append(nombre)
            elif nota >= 80:
                clasificacion["Bueno"].append(nombre)
            elif nota >= 70:
                clasificacion["Regular"].append(nombre)
            else:
                clasificacion["Reprobado"].append(nombre)

        sumaNotas = 0
        for estudiante in estudiantes:
            nota = estudiante[1]

            sumaNotas = sumaNotas + nota
        
        promedio = sumaNotas / len(estudiantes)

        # determinamos la nota mas alta
        notaMasAlta = 0
        for estudiante in estudiantes:
            nota = estudiante[1]

            if nota > notaMasAlta:
                notaMasAlta = nota

        # determinamos la nota mas baja
        notaMasBaja = 100
        for estudiante in estudiantes:
            nota = estudiante[1]

            if nota < notaMasBaja:
                notaMasBaja = nota

        print("Clasificación:")
        print(f"{'Categoria:':<30}{'Nombre:':<30}")
        for categoria, nombres in clasificacion.items():#sirve para obtener tanto la clave como el valor
            print(f"{categoria:<30}{nombres}") 
        
        print("")
        print(f"Promedio general : {promedio:.2f}")#.2f sirve para poner 2 decimales al final
        print(f"Nota mas alta    : {notaMasAlta:.2f}")#.2f sirve para poner 2 decimales al final
        print(f"Nota mas baja    : {notaMasBaja:.2f}")#.2f sirve para poner 2 decimales al final
        print("")

        print(f"{'Categoria:':<30}{'Cantidad:':<30}")
        for categoria, nombres in clasificacion.items():#sirve para obtener tanto la clave como el valor
            print(f"{categoria:<30}{len(nombres)} estudiantes")

def validarString (string):

    if string == "":
        print("Error, no puede estar vacío")
        return False

    if len(string) < 3:
        print("Error, debe tener al menos 3 caracteres")
        return False

    if len(string) > 15:
        print("Error, no debe tener más de 15 caracteres")
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

def mostrarMenu():
    
    while True:

        print("1. Agregar Estudiante")
        print("2. Ver Reporte")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-3): "))
                
            match opcion:

                case 1:
                    agregarEstudiantes()
                    
                case 2:
                    clasificarEstudiantes()

                case 3:
                    print("Saliendo...")
                    return
                    
                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 3!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")
    
mostrarMenu()
'''

# Ejercicio 05: Comparación compleja de dos listas
# Descripción: Desarrolle un programa que compare dos listas numéricas.
'''
Comentarios Ejercicios: 05

Primero, definimos una funcion para ingresar numero a las listas hasta que se escriba la palabra fin, se valida
que el dato ingresado sea un entero. Tambien se limpian las listas.

Segundo, en la funcion de operaciones de listas, primero validamos que en ambas listas haya datos para comparar
de otro modo no se muestra el reporte, dentro de la funcion quitamos duplicamos de la primera y segunda lista,
determinamos los comunes, los exclusivos tanto en la primera como en la segunda lista, la union de ambos, y
tambien los pares e impares comunes los guardamos dentro de una lista, por ultimo imprimimos.

Tercero, tenemos una funcion menu donde manejamos el flujo del programa.

'''
'''
#definimos listas globales
primeraLista = []
segundaLista = []

def ingresarLista():

    primeraLista.clear()
    while True:

        try:
            primerNumero = (input("Ingrese un numero para la primera lista: "))
            if primerNumero.lower() == "fin":
                print("Saliendo...")
                break

            else:
                primerNumero = int(primerNumero)
                primeraLista.append(primerNumero)
                print("Numeros registros con exito")
        
        except ValueError:
            print("Error, ingrese un numero")
    
    segundaLista.clear()
    while True:

        try:
            segundoNumero =  (input("Ingrese un numero para la segunda lista: "))
            if segundoNumero.lower() == "fin":
                print("Saliendo...")
                break
            
            else:
                segundoNumero = int(segundoNumero)
                segundaLista.append(segundoNumero)
                print("Numeros registros con exito")
        
        except ValueError:
            print("Error, ingrese un numero")

def operacionesListas():

    if len(primeraLista) == 0 or len(segundaLista) == 0:
        print("Error, ambas listas deben tener contener numeros")
        return
    
    else:
        #eliminamos duplicados
        primerSet = set(primeraLista)
        segundoSet = set(segundaLista)

        #los que hay en comun, ya habiando quitado los duplicados.
        comunes = primerSet & segundoSet

        #solo los que estan en la primera lista
        primeraListaExclusivos = primerSet - segundoSet

        #solo los que estan en la segunda lista
        segundaListaExclusivos = segundoSet - primerSet

        #la union de ambos si contar los repetidos
        union = primerSet | segundoSet
        
        #lista para guardar los pares o impares comunes
        comunesPares = []
        comunesImpares = []

        #verficamos si es par o no
        for numero in comunes:
            if numero % 2 == 0:
                comunesPares.append(numero)
            else:
                comunesImpares.append(numero)

        #.sorted() nos sirve para ordenar la lista de manera ascendente
        comunes = sorted(comunes)
        primeraListaExclusivos = sorted(primeraListaExclusivos)
        segundaListaExclusivos = sorted(segundaListaExclusivos)
        union = sorted(union)

        #imprimimos los resultados
        print("Primera Lista:", sorted(primeraLista))
        print("Segunda Lista:", sorted(segundaLista))
        print("")
        print("Elementos Comunes:", comunes)
        print("Primera Lista Exclusivos:", primeraListaExclusivos)
        print("Segunda Lista Exclusivos:", segundaListaExclusivos)
        print("")
        print("Union sin Repetidos:", union)
        print("Comunes Pares:", sorted(comunesPares))
        print("Comunes Impares:", sorted(comunesImpares))

def mostrarMenu():
    
    while True:

        print("1. Agregar Numeros a Listas")
        print("2. Ver Reporte")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-3): "))
                
            match opcion:

                case 1:
                    ingresarLista()
                    
                case 2:
                    operacionesListas()

                case 3:
                    print("Saliendo...")
                    return
                    
                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 3!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")
    
mostrarMenu()
'''

# Ejercicio 06: Agrupación de palabras por longitud
# Descripción: Diseñe un programa que agrupe palabras según su cantidad de caracteres.
'''
Comentarios Ejercicios: 06

Primero, registramos las palabras hasta que usuario escriba fin y validamos cada palabra.

Segundo, hacemos el calculo de la clasificacion de cada palabra, la añadimos a un diccionario, ordenamos la lista,
determinamos la clasificacion con mas palabras y por ultimo imprimimos los resultado. Tambien validamos que antes de
consultar los datos hayan palabras que consultar.
'''
'''
#definimos una lista global
palabras = []

def ingresarPalabras():

    while True:

        palabra = input("Ingrese una palabra: ").title()
        if palabra.lower() == "fin":
            print("Saliendo...")
            break
        
        else:
            string = palabra
            if validarString(string) == True:
                palabra = string
                palabras.append(palabra)
                print("Palabra registrada con exito")

def clasificacionPalabras():

    if len(palabras) == 0:
        print("No hay palabras registradas")
        return

    else:

        clasificacion = {}

        #añadimos la palabra en el diccionario de clasificacion dentro de la longitud de la palabra
        for palabra in palabras:
            longitud =  len(palabra)

            if longitud in clasificacion:
                if not palabra in clasificacion[longitud]:
                    clasificacion[longitud].append(palabra)
                
            else:
                clasificacion[longitud] = [palabra]
        
        #ordenamos la lista
        for longitud in clasificacion:
            clasificacion[longitud].sort()
        
        mayorLongitud = 0
        mayorClasificacion = 0

        #determinamos la categoria que tiene mas palabras
        for longitud in clasificacion:
            if len(clasificacion[longitud]) > mayorLongitud:
                mayorLongitud = len(clasificacion[longitud])
                mayorClasificacion = longitud

        #imprimimos los resultados
        for longitud, listaPalabras in clasificacion.items():
            print(f"Longitud {longitud:<10}{listaPalabras}")

        print("")
        print(f"Longitud con mas palabras: {mayorClasificacion}({mayorLongitud} palabras)")

def validarString (string):

    if string == "":
        print("Error, no puede estar vacío")
        return False

    if len(string) < 3:
        print("Error, debe tener al menos 3 caracteres")
        return False

    if len(string) > 15:
        print("Error, no debe tener más de 15 caracteres")
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

def mostrarMenu():
    
    while True:

        print("1. Agregar Palabras")
        print("2. Ver Reporte")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-3): "))
                
            match opcion:

                case 1:
                    ingresarPalabras()
                    
                case 2:
                    clasificacionPalabras()

                case 3:
                    print("Saliendo...")
                    return
                    
                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 3!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")

mostrarMenu()
'''

# Ejercicio 07: Inversión de diccionario con valores repetidos
# Descripción: Cree un programa que invierta un diccionario, manejando valores repetidos.
'''
Comentarios Ejercicios: 07

Primero, ingresamos los datos del diccionario mediante la funcion ingresar diccionario, donde el usuario selecciona una fruta y un color hasta que desee parar.

Segundo, invertimos el diccionario en la funcion invertir, donde si el color ya existe como clave los agregamos a la fruta de su listam, y sino creamos la
lista con la fruta. tambien lo ordenamos.

Tercero, mostramos los resultado, primero validamos que existan datos en el diccionario original y luego imprimimos ambos diccionarios.

Cuarto, manejamos un menu en mostrar menu donde se maneja el flujo del menu.

'''
'''
#definimos un diccionar global
diccionarioOriginal = {}

def ingresarDiccionario():
    
    while True:
        while True:

            print("Seleccione una fruta")
            print("")
            print("1. Fresa")
            print("2. Manzana")
            print("3. Banano")
            print("4. Limon")
            print("5. Uva")
            print("6. Naranja")
            print("")

            try:
                opcion = int(input("Ingrese una opcion (1-6): "))
                    
                match opcion:

                    case 1:
                        fruta = "Fresa"
                        print("Registrado con éxito")
                        break

                    case 2:
                        fruta = "Manzana"
                        print("Registrado con éxito")
                        break

                    case 3:
                        fruta = "Banano"
                        print("Registrado con éxito")
                        break

                    case 4:
                        fruta = "Limon"
                        print("Registrado con éxito")
                        break

                    case 5:
                        fruta ="Uva"
                        print("Registrado con éxito")
                        break

                    case 6:
                        fruta = "Naranja"
                        print("Registrado con éxito")
                        break
                        
                    case _:
                        print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 6!")
                        continue
                
            except ValueError:
                print("Error, solo se permiten digitos")

        while True:

            print("Seleccione el color de fruta")
            print("")
            print("1. Rojo")
            print("2. Amarillo")
            print("3. Verde")
            print("4. Morado")
            print("5. Naranja")
            print("6. Azul")
            print("")

            try:
                opcion = int(input("Ingrese una opcion (1-6): "))
                    
                match opcion:

                    case 1:
                        color = "Rojo"
                        print("Registrado con éxito")
                        break

                    case 2:
                        color = "Amarillo"
                        print("Registrado con éxito")
                        break

                    case 3:
                        color = "Verde"
                        print("Registrado con éxito")
                        break

                    case 4:
                        color = "Morado"
                        print("Registrado con éxito")
                        break

                    case 5:
                        color ="Naranja"
                        print("Registrado con éxito")
                        break

                    case 6:
                        color = "Azul"
                        print("Registrado con éxito")
                        break
                        
                    case _:
                        print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 6!")
                        continue
                
            except ValueError:
                print("Error, solo se permiten digitos")

        diccionarioOriginal[fruta] = color
        print("Fruta registrada con exito!")

        pregunta = input("Desea agregar otra fruta? (s/n): ").lower()
        match pregunta:

            case "s":
                continue
            case "n":
                return
            case _:
                print("Error, ingrese 's' o 'n'")

def invertirDiccionario():

    diccionarioInvertido = {}

    #si el color ya existe como clave, la agregamos la fruta a su lista.
    for fruta, color in diccionarioOriginal.items():
        if color in diccionarioInvertido:
            diccionarioInvertido[color].append(fruta)

        #sino existe creamos una lista con la fruta
        else:
            diccionarioInvertido[color] = [fruta]

    #ordenamos el diccionario
    for fruta in diccionarioInvertido:
        diccionarioInvertido[fruta].sort()

    return diccionarioInvertido

def mostrarDiccionarios():
    
    if len(diccionarioOriginal) == 0:
        print("Error, el diccionario esta vacio")
        return
    
    else:
        #imprimimos el diccionario original
        print("Diccionario Original: ")
        for frutas, color in diccionarioOriginal.items():
            print(f"{frutas:<15}{color}")
        
        print("")
        
        #imprimimos el diccionario inverso
        diccionarioInvertido = invertirDiccionario()
        print("Diccionario Invertido: ")
        for color, frutas in diccionarioInvertido.items():
            print(f"{color:<15}{frutas}")

def mostrarMenu():
    
    while True:

        print("1. Ingreser Frutas")
        print("2. Ver Reporte")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-3): "))
                
            match opcion:

                case 1:
                    ingresarDiccionario()
                    
                case 2:
                    mostrarDiccionarios()

                case 3:
                    print("Saliendo...")
                    return
                    
                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 3!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")

mostrarMenu()
'''

# Ejercicio 08: Validador de contraseñas
# Descripción: Desarrolle un programa que valide la seguridad de una contraseña.
'''
Comentarios Ejercicios: 08

Primero, solicitamos la contraseña y la llamamos hacia una funcion donde vamos a validar si la contraseña es valida.

Segundo, dentro de la funcion creamos una lista que es donde vamos a almacenar los errores de manera de string, lo primero
es saber si cumple con almenos 8 caracteres de longitud, luego definimos algunos booleanos para saber si cumple con alguno de 
esos requisitos y guardarlos dentro de esa funcion, lo validamos caracter por caracter. Si alguno de esos booleanos es false
despues de verificar caracter por caracter es porque no cumplio alguno de los requisitos, por lo que vamos a guardar el error
dentro de la lista en forma de string.

Tercero, una vez validado todo los requisitos imprimimos los resultados, si no tiene errores es valida, en caso contrario si posee
1 o mas errores se los mostramos.
'''
'''
#solicitamos contraseña  
contraseña = input("Ingrese una contraseña: ")

def validarContraseña(contraseña):

    #lista de errores
    errores = []

    #verificamos si cumple 8 caracteres como minimo
    if len(contraseña) < 8:
        errores.append("Error: no menos de 8 caracteres")

    #variables para saber si cumple con los requisitos
    tieneMayuscula = False
    tieneMinuscula = False
    tieneNumero = False
    tieneSimbolo = False

    #recorremos el caracter de la contraseña y lo validamos.
    for caracter in contraseña:
        if caracter.isupper(): 
            tieneMayuscula = True
        if caracter.islower(): 
            tieneMinuscula = True
        if caracter.isdigit(): 
            tieneNumero = True
        if caracter in "!@#$%^&*": 
            tieneSimbolo = True

    #almacenamos el error en caso de que no cumpla.
    if not tieneMayuscula == True:
        errores.append("Error: no tiene mayusculas")
    if not tieneMinuscula == True:
        errores.append("Error: no tiene minisculas")
    if not tieneNumero == True:
        errores.append("Error: no tiene numeros")
    if not tieneSimbolo == True:
        errores.append("Error: no tiene simbolos")

    #validamos que si no hay errores es porque es correcta.
    if len(errores) == 0:
        print("Contraseña valida!")
    
    else:
        #imprimimos los errores, de la lista.
        print("Contraseña invalida estos son sus errores: ")
        for error in errores:
            print(error)

validarContraseña(contraseña)
'''

# Ejercicio 09: Sistema de votaciones con empate
# Descripción: Implemente un sistema que procese una lista de votos.
'''
Comentarios Ejercicios: 09

Primero, en ingresar votos, seleccionamos el candidato por el cual vamos a votar y le preguntamos al usuario si desea seguir votando o desea terminar.

Segundo, en procesar votos validamos que haya votacion de otra forma no podra ingresar a ver reporte. Definimos un conteo y contruimos los votos por candidato,
determinamos la cantidad maxima de votos, una lista de ganadores para derminar si existe la posibilidad de empate o no, ordenamos la lista y por ultimo
imprimimos los resultados, total de votos, el ganador o en caso de haya empate y un conjunto de los candidatos que almenos recibieron un voto.

Tercero, mostrar menu, manejamos el programa con un menu.

'''
'''
#definimos una lista.
votos = []

def ingresarVotos():
    
    while True:
        while True:

            print("Seleccione un candidato")
            print("")
            print("1. Juan")
            print("2. Maria")
            print("3. Pedro")
            print("4. Sara")
            print("")

            try:
                opcion = int(input("Ingrese una opcion (1-4): "))
                    
                match opcion:

                    case 1:
                        voto = "Juan"
                        print("Registrado con éxito")
                        break

                    case 2:
                        voto = "Maria"
                        print("Registrado con éxito")
                        break

                    case 3:
                        voto = "Pedro"
                        print("Registrado con éxito")
                        break

                    case 4:
                        voto = "Sara"
                        print("Registrado con éxito")
                        break
                        
                    case _:
                        print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 6!")
                        continue
                
            except ValueError:
                print("Error, solo se permiten digitos")


        votos.append(voto)
        print("Voto registrado con exito!")

        pregunta = input("Desea agregar votar otra vez? (s/n): ").lower()
        match pregunta:

            case "s":
                continue
            case "n":
                return
            case _:
                print("Error, ingrese 's' o 'n'")

def procesarVotos():
    
    if len(votos) == 0:
        print("Error, no hay votos realizados")
        return
    
    else:
        
        #definimos un diccionario
        conteo = {}
        
        #construimos el diccionario con el conteo de votos por candidato
        for voto in votos:
            if voto in conteo:
                conteo[voto] = conteo[voto] + 1
            
            else:
                conteo[voto] = 1

        #determinamos la cantidad maxima de votos
        maximoVotos = 0 
        for candidato in conteo:
            if conteo[candidato] > maximoVotos:
                maximoVotos = conteo[candidato]

        #añadimos el ganador o ganadores a la lista de ganadores
        ganadores = []
        for candidato in conteo:
            if conteo[candidato] == maximoVotos:
                ganadores.append(candidato)

        #ordenamos los ganadores
        ganadores.sort()

        #
        print(f"{'Candidato':<30}{'Votos'}")
        conteoOrdenado = sorted(conteo, key=conteo.get, reverse=True)#sorted(conteo) recorre el diccionario, key=conteo.get lo ordena por la cantidad de votos y reverse=True lo ordena de mayor a menor
        for candidato in conteoOrdenado:
            print(f"{candidato:<30}{conteo[candidato]}")

        #imprimimos los resultados
        #total de votos
        print("")
        print(f"Total de votos: {len(votos)}")

        #mostrar ganador o lista de empatados
        print("")
        if len(ganadores) > 1:
            print(f"Empate entre: {ganadores} con {maximoVotos} votos cada uno")
        else:
            print(f"Ganador: {ganadores[0]} con {maximoVotos} votos")

        candidatos = set(votos) #conjunto de candidatos que al menos recibieron un voto
        print("")
        print(f"Candidatos con votos: {candidatos}")

def mostrarMenu():
    
    while True:

        print("1. Ingreser Votos")
        print("2. Ver Reporte")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-3): "))
                
            match opcion:

                case 1:
                    ingresarVotos()
                    
                case 2:
                    procesarVotos()

                case 3:
                    print("Saliendo...")
                    return
                    
                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 3!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")

mostrarMenu()
'''

# Ejercicio 10: Fusión de listas de tuplas y promedio
# Descripción: Realice un programa que combine información proveniente de dos listas de tuplas.
'''
Comentarios Ejercicios: 10

Primero, ingresamos los estudiantes con sus notas, para eso usamos una funcion reutilizable la cual solo le cambiamos los parametros y podemos
volver a utilizarla e ingresamos nota hasta que el usuario ya no lo desee.

Segundo, validamos que haya notas de estudiantes en ambas listas, en fusionar listas, unimos las listas, creamos el diccionario final, luego guardamos
las notas en el diccionario en caso de que el nombre exista en ambas listas sacamos su promedio, despues definimos dos nuevas listas
para aprobados y reprobados en la cual vamos a agregar a su respectiva lista dependiendo si estan aprobados o reprobados por ultimo imprimimos
los resultados.

Tercero usamos un menu para el manejo del programa.
'''
'''
#definimos las listas
primeraLista = []
segundaLista = []

def ingresarEstudiantes(lista, nombreLista):

    while True:
        while True:

            nombreEstudiante = input("Ingrese el nombre del estudiante: ").title()
            string =  nombreEstudiante
            if validarString(string) == True:
                nombreEstudiante = string
                break
        
        while True:

            try:
                notaEstudiante = float(input("Ingrese la nota del estudiante: "))
                if notaEstudiante < 0 or notaEstudiante > 100:
                    print("La nota no puede ser negativa y tiene que ser de 1 a 100")
                else:
                    print("Nota registrada con éxito")
                    break
                
            except ValueError:
                print("Error, solo se permiten digitos")


        lista.append((nombreEstudiante, notaEstudiante))

        #preguntamos al usuario si dea agregar otra nota
        pregunta = input(f"Agregar otro a {nombreLista}? (s/n): ").lower()
        while pregunta != "s" and pregunta != "n":
            print("Error, ingrese 's' o 'n'")
            pregunta = input(f"Agregar otro a {nombreLista}? (s/n): ").lower()

        if pregunta == "n":
            return

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

def fusionarListas():

    if len(primeraLista) == 0 or len(segundaLista) == 0:
        print("Error, ambas listas deben tener estudiantes")
        return
    
    else:
        #unimos la lista
        listaUnida = primeraLista + segundaLista
        #declaramos un diccionario donde van las notas
        diccionarioFinal = {}
        
        #guardamos la notas en el diccionario y si el nombre existe en ambas sacamos su promedio
        for nombre, nota in listaUnida:
            if nombre in diccionarioFinal:
                diccionarioFinal[nombre] = (diccionarioFinal[nombre] + nota) / 2
            else:
                diccionarioFinal[nombre] = nota

        aprobados = []
        reprobados = []
        #determinamos si esta aprobados o reprobados
        for nombre, promedio in diccionarioFinal.items():
            if promedio >= 70:
                aprobados.append(nombre)
            else:
                reprobados.append(nombre)
        
        # prints de resultados
        print(f"{'Nombre':<30}{'Promedio'}")
        for nombre, promedio in diccionarioFinal.items():
            print(f"{nombre:<30}{promedio:.2f}")

        print("")
        print("Aprobados:", aprobados)
        print("Reprobados:", reprobados)
    
def mostrarMenu():
    
    while True:

        print("1. Ingreser Lista 1")
        print("2. Ingreser Lista 2")
        print("3. Ver Reporte")
        print("4. Salir")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-4): "))
                
            match opcion:

                case 1:
                    #llamamos una funcion con parametros especificos
                    ingresarEstudiantes(primeraLista, "Lista 1")
                    
                case 2:
                    #llamamos una funcion con parametros especificos
                    ingresarEstudiantes(segundaLista, "Lista 2")

                case 3:
                    fusionarListas()
                
                case 4:
                    print("Saliendo...")
                    return
                    
                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 4!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")

mostrarMenu()
'''

# Ejercicio 11: Eliminación de duplicados manteniendo el último valor
# Descripción: Diseñe un programa que elimine duplicados en una lista, pero manteniendo la última apariciónde cada elemento.
'''
Comentarios Ejercicios: 11

Primero, solicitamos numeros infinitamente y validamos que sea un numero hasta que el usuario desee.

Segundo, verificamos que la lista no este vacia para proceder, luego definimos una lista nueva donde van
los numeros sin duplicados, la variables vistos nos sirve para marcar a los numero ya contados, recorremos
la lista original de atras hacia adelante, verificamos si el numero ha sido visto, sino se agrega a resultado
y se marca como visto, luego invertimos la lista de resultados para que tome su orden original y por ultimo
imprimimos los datos.

Tercero, Manejamos el programa con la funcion del menu.
'''
'''
#definimos una lista global
numeros = []

def ingresarLista():

    numeros.clear()
    while True:

        try:
            numero = (input("Ingrese un numero para la lista: "))
            if numero.lower() == "fin":
                print("Saliendo...")
                break

            else:
                numero = int(numero)
                numeros.append(numero)
                print("Numeros registros con exito")
        
        except ValueError:
            print("Error, ingrese un numero")

def eliminarDuplicados():

    if len(numeros) == 0:
        print("Error, no hay numeros en la lista")
        return
    
    else:
        #aqui vamos a guardar la lista sin duplicados
        resultado = []
        vistos = set()#nos sirve para saber numero ya registrados
        
        #recorremos la lista de atras hacia adelante
        for elemento in numeros[::-1]:
            #si el numero no ha sido visto, se agrega a resultado y se marca como visto
            if elemento not in vistos:
                resultado.append(elemento)
                vistos.add(elemento)

        #invertimos el resultado para el orden original
        resultado = resultado[::-1]

        #imprimimos resultados.
        print("Lista Original:", numeros)
        print("Lista sin Duplicados:", resultado)

def mostrarMenu():
    
    while True:

        print("1. Ingreser Numeros en Lista")
        print("2. Ver Reporte")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("Ingrese una opcion (1-3): "))
                
            match opcion:

                case 1:
                    ingresarLista()
                    
                case 2:
                    eliminarDuplicados()

                case 3:
                    print("Saliendo...")
                    return
                    
                case _:
                    print("Error, opcion invalida. Ingrese una opcion valida! Solo se permiten digitos del 1 al 3!")
                    continue
            
        except ValueError:
            print("Error, solo se permiten digitos")

mostrarMenu()
'''
# Ejercicio 12: Búsqueda de subcadenas y posiciones
# Descripción: Elabore un programa que busque una subcadena dentro de un texto.
'''
Comentarios Ejercicios: 12

Primero, declaramos un lista global donde vamos a almacenar las posiciones de las subcandenas, despues
le solicitamos al usuario una cadena principal y una subcadena, recorremos la cadena principal hasta donde pueda
estar una subcadena.

Segundo, declaramos que existe una coincide en booleano hasta demostralo sino pasaria a false, luego comparamos
los caracteres de la subcadena con la cadena principal, sino encontramos coincidencia pasa a false, si, si encuentra
coincidencia entonces guardamos la posiciones del caracter.

Tercero, validamos si la subcadena existe dentro del texto principal, y si si existe, imprimimos los datos las apariciones
y la posicion. Tambien validamos si una aparicion se solapa con la siguiente e imprimimos el resultado.
'''
'''
#lista global para almacenar la posicones donde estan las subcadenas
posiciones = []

def busquedaSubCadena (cadenaPrincipal, subcadena):

    #recorremos la cadena principal hasta donde pueda estar la subcadena
    for caracterPrincipal in range(len(cadenaPrincipal) - len(subcadena) + 1):
        
        #asumimos que hay conincidencia hasta demostrar lo contrario.
        coincide =  True

        #comparamos cada caracter de la subcadena con la cadena principal
        for caracterSecundario in range(len(subcadena)):
            if cadenaPrincipal[caracterPrincipal + caracterSecundario] != subcadena[caracterSecundario]:
                coincide = False
                break
        
        #si todos los caracteres coincidieron, guardamos la posicion.
        if coincide == True:
            posiciones.append(caracterPrincipal)
    
    #validamos si la subcadena existe en el texto.
    if len(posiciones) == 0:
        print("La subcadena no existe")
    else:
        #imprimimos los datos, las apariciones y la posicion
        print("Apariciones:", len(posiciones))
        print("Posiciones:", posiciones)


        #detectamos si una aparicion se solapa con la siguiente.
        haySolapamiento = False
        for i in range(len(posiciones) - 1):
            if posiciones[i+1] - posiciones[i] < len(subcadena):
                haySolapamiento = True

        if haySolapamiento:
            print("Las apariciones se solapan")
        else:
            print("Las apariciones no se solapan")
        
#solicitamos datos al usuario y ejecutamos el programa de busqueda.
cadenaPrincipal = input("Ingrese una cadena: ")
subcadena = input("Ingrese una subcadena: ")
busquedaSubCadena(cadenaPrincipal, subcadena)
'''
