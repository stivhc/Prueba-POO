# -*- coding: utf-8 -*-
"""
Script demo para interactuar con las clases definidas.
Permite modificar atributos de una campaña y manejar excepciones.
"""

import logging
from datetime import date
from campania import Campania  # Importa la clase Campania correctamente

# Configuración de logging para registrar errores en un archivo
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Crear una instancia de Campania con un solo anuncio de tipo Video
c = Campania("Campania Demo", date.today(), date.today(), [
    {
        "tipo": "video",         # Tipo de anuncio: Video
        "url_clic": "sin-url",   # URL donde se dirige el clic (valor predeterminado)
        "url_archivo": "sin-url", # URL del archivo del anuncio (valor predeterminado)
        "sub_tipo": "instream",  # Subtipo del anuncio de video (instream/outstream)
        "duracion": 30           # Duración del video en segundos
    }
])

try:
    # Solicitar al usuario un nuevo nombre para la campaña
    nombre = input("Ingrese nuevo nombre de la campaña: ")
    c.nombre = nombre  # Actualizar el nombre de la campaña

    # Solicitar al usuario un nuevo subtipo de anuncio
    sub_tipo = input("Ingrese nuevo sub tipo del anuncio:")
    c.anuncios[0].sub_tipo = sub_tipo  # Actualizar el subtipo del anuncio

except Exception as e:
    # Registrar el error en 'error.log' en caso de excepción
    logging.error(f"{e}")
    print("Ha ocurrido un error, por favor revise el archivo 'error.log'.")
