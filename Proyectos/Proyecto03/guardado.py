'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 19, Proyecto #3: SiembraTEC

Fecha de entrega: 29/06/2026

'''

import json
import time

from productos import *
from jugador import Jugador
from terreno import Terreno


def guardarPartida(jugador):
    """
    Guarda el estado completo de la partida en un archivo JSON.
    Incluye datos del jugador, terrenos, productos colocados,
    inventario, estadísticas y disponibilidad de Lana.

    Args:
        jugador (Jugador): El objeto jugador con toda la información de la partida.
    """
    datos = {
        "Jugador": {
            "nombre": jugador.getNombre(),
            "monedas": jugador.getMonedas(),
            "tiempoInicio": jugador.getTiempoInicio(),
            "totalMonedasGeneradas": jugador.getTotalMonedasGeneradas(),
            "totalProductosComprados": jugador.getTotalProductosComprados(),
            "cantidadTerrenos": jugador.getCantidadTerrenos(),
            "tiempoAcumulado": jugador.getTiempoTotal(),
            "inventario": [{"tipo": p.getNombre(), "rotacion": p.getRotacion() if hasattr(p, 'getRotacion') else 0} for p in jugador.getInventario()],
            "cantidadPorTipo": jugador.getCantidadPorTipo(),
        },
        "terrenos": [],
        "lanaDisponible": jugador.getLVHDisponible()
    }

    for terreno in jugador.getTerrenos():
        terrenoInfo = {
            "id": terreno.getID(),
            "matriz": []
        }

        for fila in terreno.getMatriz():
            filaInfo = []
            for celda in fila:
                if celda is None:
                    filaInfo.append(None)
                else:
                    filaInfo.append({
                        "tipo": celda.getNombre(),
                        "horaInicio": celda.getHoraInicio(),
                        "rotacion": celda.getRotacion() if hasattr(celda, 'getRotacion') else 0
                    })
            terrenoInfo["matriz"].append(filaInfo)

        datos["terrenos"].append(terrenoInfo)

    with open("partida.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)


def cargarPartida():
    """
    Carga una partida guardada desde el archivo JSON y reconstruye
    todos los objetos del juego incluyendo jugador, terrenos,
    productos colocados e inventario.

    Returns:
        Jugador: El objeto jugador con toda la información restaurada.
    """
    with open("partida.json", "r") as archivo:
        datos = json.load(archivo)

    jugador = Jugador(datos["Jugador"]["nombre"])
    jugador._monedas = datos["Jugador"]["monedas"]
    jugador._tiempoInicio = time.time()
    jugador._tiempoAcumulado = datos["Jugador"]["tiempoAcumulado"]
    jugador._totalMonedasGeneradas = datos["Jugador"]["totalMonedasGeneradas"]
    jugador._totalProductosComprados = datos["Jugador"]["totalProductosComprados"]
    jugador._cantidadTerrenos = datos["Jugador"]["cantidadTerrenos"]
    jugador._cantidadPorTipo = datos["Jugador"].get("cantidadPorTipo", {})
    jugador._LVHDisponible = datos.get("lanaDisponible", True)

    # diccionario que mapea nombres de productos a sus clases
    tipos = {
        "Trigo": Trigo, "Maiz": Maiz, "Zanahoria": Zanahoria,
        "Tomate": Tomate, "Papa": Papa,
        "Gallina": Gallina, "Pato": Pato, "Oveja": Oveja,
        "Cerdo": Cerdo, "Vaca": Vaca, "Lana": VacaEspecial,
        "Manzano": Manzano, "Naranjo": Naranjo, "Limonero": Limonero,
        "Cacaotero": Cacaotero, "Cafetal": Cafetal,
        "Cerca": Cerca, "Banco": Banco, "Fuente": Fuente,
        "Estatua": Estatua, "Molino": Molino
    }

    # restaurar inventario
    for item in datos["Jugador"].get("inventario", []):
        if item["tipo"] in tipos:
            producto = tipos[item["tipo"]]()
            if hasattr(producto, 'rotacion'):
                producto.rotacion = item.get("rotacion", 0)
            jugador._inventario.append(producto)

    # restaurar terrenos y productos colocados
    for terrenoInfo in datos["terrenos"]:
        terreno = Terreno(terrenoInfo["id"])
        for numeroFila, fila in enumerate(terrenoInfo["matriz"]):
            for numeroColumna, celda in enumerate(fila):
                if celda is not None:
                    producto = tipos[celda["tipo"]]()
                    producto._horaInicio = celda["horaInicio"]
                    if hasattr(producto, 'rotacion'):
                        producto.rotacion = celda.get("rotacion", 0)
                    terreno._matriz[numeroFila][numeroColumna] = producto
        jugador._terrenos.append(terreno)

    return jugador