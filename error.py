# -*- coding: utf-8 -*-
"""
Módulo de definición de excepciones personalizadas para la aplicación.
Define las excepciones relacionadas con la validación de anuncios y campañas.
"""

class Error(Exception):
    """Clase base para excepciones personalizadas."""
    pass

class LargoExcedidoError(Error):
    """
    Excepción lanzada cuando el nombre de la campaña excede el límite de caracteres permitido.
    Se lanza esta excepción si el nombre de la campaña tiene más de 250 caracteres.
    """
    pass

class SubTipoInvalidoError(Error):
    """
    Excepción lanzada cuando se encuentra un subtipo de anuncio no válido.
    Por ejemplo, si un subtipo no corresponde al tipo de anuncio (Video, Display, Social).
    """
    pass
