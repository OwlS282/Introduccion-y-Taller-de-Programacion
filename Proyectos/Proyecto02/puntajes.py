'''
Instituto Tecnológico de Costa Rica

Nombre: Owel Jafet Gutiérrez Ortiz

Carnet: 2026800869

Profesor: Bryan Hernández Sibaja

Semana 12, Proyecto #2: Buscaminas

Fecha de entrega: 22/05/2026

'''
# Archivo: puntajes.py
# Descripción: Manejo de puntajes altos del juego Buscaminas

import json
import os

# Ruta base del proyecto para ubicar el archivo de puntajes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class archiPuntajes:
    """
    Clase que maneja el registro, almacenamiento y consulta
    de los mejores puntajes por nivel de dificultad.
    Los puntajes se guardan en un archivo JSON.
    """

    def __init__(self):
        # Al crear la instancia se cargan los puntajes existentes
        self.cargarPuntajes()

    # Carga de puntajes desde el archivo JSON
    def cargarPuntajes(self):
        """
        Lee el archivo puntajes.json y carga los datos en memoria.
        Si el archivo no existe, inicializa un diccionario vacío
        con las cinco categorías de dificultad.
        """
        try:
            with open(os.path.join(BASE_DIR, "puntajes.json"), "r") as archivoPuntajes:
                self.datos = json.load(archivoPuntajes)
        except FileNotFoundError:
            # Si no existe el archivo se crea la estructura vacía
            self.datos = {
                "facil": [],
                "medio": [],
                "dificil": [],
                "experto": [],
                "custom": []
            }

    # Guardado de un nuevo puntaje
    def guardarPuntajes(self, nivel, nombre, tiempo):
        """
        Agrega un nuevo puntaje al nivel indicado, ordena de menor
        a mayor tiempo y conserva solo los 10 mejores.
        Luego guarda los datos actualizados en el archivo JSON.
        """
        # Crear el registro del nuevo puntaje
        nuevoPuntaje = {"nombre": nombre, "tiempo": tiempo}

        # Agregar a la lista del nivel correspondiente
        self.datos[nivel].append(nuevoPuntaje)

        # Ordenar de menor a mayor tiempo (mejor puntaje primero)
        self.datos[nivel].sort(key=lambda x: x["tiempo"])

        # Conservar solo los 10 mejores puntajes
        self.datos[nivel] = self.datos[nivel][:10]

        # Guardar los datos actualizados en el archivo JSON
        with open(os.path.join(BASE_DIR, "puntajes.json"), "w") as archivoPuntajes:
            json.dump(self.datos, archivoPuntajes)

    # Consulta de puntajes por nivel
    def obtenerPuntajes(self, nivel):
        """
        Devuelve la lista de puntajes del nivel indicado,
        ordenada de menor a mayor tiempo.
        """
        return sorted(self.datos[nivel], key=lambda x: x["tiempo"])