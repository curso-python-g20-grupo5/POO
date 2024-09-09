from abc import ABC, abstractmethod
from error import SubTipoInvalidoError


class Anuncio(ABC):
    """Clase base abstracta para representar diferentes tipos de anuncios.

    Args:
        subtipo (str): El subtipo del anuncio.

    Attributes:
        _subtipo (str): El subtipo del anuncio.

    Methods:
        __str__: Método abstracto que debe ser implementado por las clases hijas.
        subtipo: Propiedad getter y setter para el atributo _subtipo.
    """

    def __init__(self, subtipo):
        """Inicializa un objeto de la clase Anuncio.

        Args:
            subtipo (str): El subtipo del anuncio.
        """
        self._subtipo = subtipo

    @abstractmethod
    def __str__(self):
        """Método abstracto que devuelve una representación en cadena del anuncio.

        Returns:
            str: Representación en cadena del anuncio.
        """
        pass

    @property
    def subtipo(self):
        """Obtiene el subtipo del anuncio.

        Returns:
            str: El subtipo del anuncio.
        """
        return self._subtipo

    @subtipo.setter
    def subtipo(self, value):
        """Establece el subtipo del anuncio.

        Args:
            value (str): El nuevo subtipo del anuncio.
        """
        self._subtipo = value


class Video(Anuncio):
    """Clase que representa un anuncio de tipo Video.

    Args:
        ancho (int): El ancho del video en píxeles.
        alto (int): El alto del video en píxeles.
        subtipo (str): El subtipo del anuncio de video. Debe estar en la lista SUB_TIPOS.
        duracion (int): La duración del video en segundos.

    Attributes:
        ancho (int): El ancho del video.
        alto (int): El alto del video.
        duracion (int): La duración del video en segundos.
        SUB_TIPOS (list): Lista de subtipos válidos para el anuncio de tipo Video.
    """

    SUB_TIPOS = ["instream", "outstream"]

    def __init__(self, ancho, alto, subtipo, duracion):
        """Inicializa un objeto de la clase Video.

        Args:
            ancho (int): El ancho del video.
            alto (int): El alto del video.
            subtipo (str): El subtipo del anuncio de video.
            duracion (int): La duración del video en segundos.

        Raises:
            SubTipoInvalidoError: Si el subtipo no es válido.
        """
        super().__init__(subtipo)
        if subtipo not in Video.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {subtipo} no es válido para Video")

        self.ancho = ancho if ancho > 0 else 1
        self.alto = alto if alto > 0 else 1
        self.duracion = duracion

    def __str__(self):
        """Devuelve una representación en cadena del anuncio de video.

        Returns:
            str: Representación en cadena del anuncio de video.
        """
        return f"Video subtipo: {self.subtipo}, dimensiones: {self.ancho}x{self.alto}, duración: {self.duracion} seg"


class Display(Anuncio):
    """Clase que representa un anuncio de tipo Display.

    Args:
        subtipo (str): El subtipo del anuncio de display. Debe estar en la lista SUB_TIPOS.

    Attributes:
        SUB_TIPOS (list): Lista de subtipos válidos para el anuncio de tipo Display.
    """

    SUB_TIPOS = ["tradicional", "native"]

    def __init__(self, subtipo):
        """Inicializa un objeto de la clase Display.

        Args:
            subtipo (str): El subtipo del anuncio de display.

        Raises:
            SubTipoInvalidoError: Si el subtipo no es válido.
        """
        super().__init__(subtipo)
        if subtipo not in Display.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {subtipo} no es válido para Display")

    def __str__(self):
        """Devuelve una representación en cadena del anuncio de display.

        Returns:
            str: Representación en cadena del anuncio de display.
        """
        return f"Display subtipo: {self.subtipo}"


class Social(Anuncio):
    """Clase que representa un anuncio de tipo Social.

    Args:
        subtipo (str): El subtipo del anuncio de social. Debe estar en la lista SUB_TIPOS.

    Attributes:
        SUB_TIPOS (list): Lista de subtipos válidos para el anuncio de tipo Social.
    """

    SUB_TIPOS = ["facebook", "linkedin"]

    def __init__(self, subtipo):
        """Inicializa un objeto de la clase Social.

        Args:
            subtipo (str): El subtipo del anuncio de social.

        Raises:
            SubTipoInvalidoError: Si el subtipo no es válido.
        """
        super().__init__(subtipo)
        if subtipo not in Social.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {subtipo} no es válido para Social")

    def __str__(self):
        """Devuelve una representación en cadena del anuncio de social.

        Returns:
            str: Representación en cadena del anuncio de social.
        """
        return f"Social subtipo: {self.subtipo}"
