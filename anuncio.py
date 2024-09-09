from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    """Clase abstracta que representa un anuncio genérico."""
    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        """
        Inicializa un anuncio, verificando que el ancho y alto sean mayores que 0.
        Si son menores o iguales a 0, se asigna 1 como valor predeterminado.
        """
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo  # Por ahora, no se requiere validación adicional.
        self.__url_clic = url_clic  # Por ahora, no se requiere validación adicional.
        self.__sub_tipo = sub_tipo  # Validación se hace en el setter.

    @property
    def ancho(self) -> int:
        """Devuelve el ancho del anuncio."""
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        """Establece el ancho del anuncio, garantizando que sea mayor que 0."""
        self.__ancho = ancho if ancho > 0 else 1

    @property
    def alto(self) -> int:
        """Devuelve el alto del anuncio."""
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        """Establece el alto del anuncio, garantizando que sea mayor que 0."""
        self.__alto = alto if alto > 0 else 1

    @property
    def sub_tipo(self) -> str:
        """Devuelve el subtipo del anuncio."""
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str) -> None:
        """
        Establece el subtipo del anuncio, verificando si es válido para su tipo.
        Si no es válido, lanza una excepción SubTipoInvalidoError.
        """
        # La validación depende del tipo de anuncio (Video, Display o Social).
        if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS or
            isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS or
            isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError("El sub tipo indicado no está permitido para este formato")
        else:
            self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos():
        for cls in Anuncio.__subclasses__():
            print(f"FORMATO: {cls.FORMATO}")
            print("=" * 10)
            for sub_tipo in cls.SUB_TIPOS:
                print(f"- {sub_tipo}")

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = max(5, duracion)
    
    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        self._duracion = max(5, value)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
