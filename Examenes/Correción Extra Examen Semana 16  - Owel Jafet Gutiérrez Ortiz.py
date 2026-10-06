#Ejercicio 1

def invertirSring(string, palabraActual=""):
    if string == "":
        return palabraActual

    caracter = string[-1]

    restoString = string[:-1]
    
    if caracter == " ":
        return palabraActual + " " + invertirSring(restoString)
    
    return invertirSring(restoString, caracter + palabraActual)


string = "Python es poderoso"
print(invertirSring(string))


#Ejercicio 2

class Videojuego:

    def __init__(self, titulo, genero, precio, stock, ventas):
        self.titulo = titulo
        self.genero = genero

        if precio > 0:
            self.precio = precio
        else:
            self.precio = 1

        if stock > 0:
            self.stock = stock
        else:
            self.stock = 0

        self.ventas = 0


    def mostrarInfo(self):

        print("Titulo:", self.titulo)
        print("Genero:", self.genero)
        print("Precio:", self.precio)
        print("Stock:", self.stock)
        print("Ventas:", self.ventas)
        print("")

    def vender(self, cantidad):

        if cantidad < 0:
            return "Error, cantidad debe ser Positiva"

        if cantidad > self.stock:
            return "Error, Stock insuficiente"

        self.stock -= cantidad
        self.ventas += cantidad


    def reabastecer(self, cantidad):

        if cantidad < 0:
            return "Error, cantidad deber ser Positiva"

        self.stock += cantidad


    def aplicarDescuento(self, porcentaje):

        if porcentaje < 0 or porcentaje > 50:
            return "Error, porcentaje Invalido"

        descuento =  self.precio * (porcentaje / 100)

        self.precio -= descuento

    def calcularIngresos(self):
        return self.ventas * self.precio

    def estaDisponible(self):
        return self.stock > 0


Juego1 = Videojuego("Rocket League", "Deportivo", 15000, 15, 0)
Juego2 = Videojuego("Valheim", "Aventura", 25000, 30, 0)
Juego3 = Videojuego("Candy Crush", "Arcade", 5000, 10, 0)

catalogo = [Juego1, Juego2, Juego3]

#mostrar
for juego in catalogo:
    juego.mostrarInfo()

#ventas
Juego1.vender(5)


#aplicar descuento
Juego2.aplicarDescuento(25)


#reabastecer        
Juego3.reabastecer(20)


#el mas vendido
masVendido = catalogo[0]
for juego in catalogo:
    if juego.ventas > masVendido.ventas:
        masVendido = juego.ventas
print("El juego mas vendido es:", masVendido.titulo)
print("")



#mostrar los disponibles
contador = 0
for juego in catalogo:
    if juego.estaDisponible():
        contador += 1
print("Se encuentran disponibles:", contador, "juegos")
print("")
    


for juego in catalogo:
    juego.mostrarInfo()


#ejercicio 3


def matrizEspejo(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] != matriz[f][columnas - 1 - c]:
                return False
    return True




matriz1 = [[1, 2, 2, 1],
          [3, 4, 4, 3],
          [5, 6, 6, 5],
          [7, 8, 8, 7]]

matriz2 = [[1, 2, 3],
          [4, 5, 4],
          [7, 8, 9]]

if matrizEspejo(matriz1) == True:
    print("La matriz 1 es un espejo Horizontal")
else:
    print("La matriz 1 no es un espejo Horizontal")


if matrizEspejo(matriz2) == True:
    print("La matriz 2 es un espejo Horizontal")
else:
    print("La matriz 2 no es un espejo Horizontal")

