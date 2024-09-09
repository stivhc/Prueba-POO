from datetime import date
from error import LargoExcedidoError
from anuncio import Video, Social, Display

class Campania:
    """Clase que representa una campaña publicitaria, que contiene anuncios."""

    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list) -> None:
        """
        Inicializa la campaña con un nombre, fechas y anuncios validados.
        Si el nombre excede los 250 caracteres, lanza una excepción.
        """
        if len(nombre) > 250:
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres")
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        # Se convierte cada anuncio en la instancia correspondiente (Video, Display, Social).
        self.__anuncios = [self.__obtener_instancia_anuncio(anuncio) for anuncio in anuncios]

    def __obtener_instancia_anuncio(self, anuncio: dict):
        """
        Obtiene la instancia correcta de anuncio (Video, Display, Social) según el tipo.
        Devuelve la instancia de Video, Display o Social, basada en los datos del anuncio.
        """
        tipo_anuncio = anuncio.get("tipo", "").lower()
        ancho = anuncio.get("ancho", 0)
        alto = anuncio.get("alto", 0)
        url_archivo = anuncio.get("url_archivo", "")
        url_clic = anuncio.get("url_clic", "")
        sub_tipo = anuncio.get("sub_tipo", "")
        duracion = anuncio.get("duracion", 0)

        if tipo_anuncio == "video":
            return Video(url_archivo, url_clic, sub_tipo, duracion)
        elif tipo_anuncio == "social":
            return Social(ancho, alto, url_clic, url_clic, sub_tipo)
        else:
            return Display(ancho, alto, url_clic, url_clic, sub_tipo)

    @property
    def nombre(self) -> str:
        """Devuelve el nombre de la campaña."""
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        """Establece el nombre de la campaña, lanzando una excepción si excede los 250 caracteres."""
        if len(nombre) > 250:
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres")
        self.__nombre = nombre
