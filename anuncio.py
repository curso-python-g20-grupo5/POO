from abc import ABC, abstractmethod
from error import SubTipoInvalidoError


class Anuncio(ABC):
    """Clase base abstracta para representar diferentes tipos de anuncios.

    Args:
        subtipo (str): El subtipo del anuncio.

    Attributes:
        _subtipo (str): El subtipo del anuncio.
        _ancho (int): El ancho del anuncio. Si el valor es menor o igual a 0, se asigna 1.
        _alto (int): El alto del anuncio. Si el valor es menor o igual a 0, se asigna 1.

    Methods:
        __str__: Método abstracto que debe ser implementado por las clases hijas.
        subtipo: Propiedad getter y setter para el atributo _subtipo.
        ancho: Propiedad getter y setter para el atributo _ancho.
        alto: Propiedad getter y setter para el atributo _alto.
        mostrar_formatos: Método estático que muestra los formatos y sus subtipos asociados.
    """

    def __init__(self, subtipo, ancho=None, alto=None):
        """Inicializa un objeto de la clase Anuncio.

        Args:
            subtipo (str): El subtipo del anuncio.
            ancho (int, optional): El ancho del anuncio. Por defecto, se asigna 1 si no es válido.
            alto (int, optional): El alto del anuncio. Por defecto, se asigna 1 si no es válido.
        """
        self._subtipo = subtipo
        self._ancho = ancho if ancho and ancho > 0 else 1
        self._alto = alto if alto and alto > 0 else 1

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

    @property
    def ancho(self):
        """Obtiene el ancho del anuncio.

        Returns:
            int: El ancho del anuncio.
        """
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        """Establece el ancho del anuncio.

        Args:
            value (int): El nuevo ancho del anuncio. Si el valor es menor o igual a 0, se asigna 1.
        """
        self._ancho = value if value > 0 else 1

    @property
    def alto(self):
        """Obtiene el alto del anuncio.

        Returns:
            int: El alto del anuncio.
        """
        return self._alto

    @alto.setter
    def alto(self, value):
        """Establece el alto del anuncio.

        Args:
            value (int): El nuevo alto del anuncio. Si el valor es menor o igual a 0, se asigna 1.
        """
        self._alto = value if value > 0 else 1

    @staticmethod
    def mostrar_formatos():
        """Muestra los formatos y sus subtipos asociados."""
        formatos = {
            "Video": Video.SUB_TIPOS,
            "Display": Display.SUB_TIPOS,
            "Social": Social.SUB_TIPOS,
        }

        for i, (formato, subtipos) in enumerate(formatos.items(), start=1):
            print(f"FORMATO {i}:")
            print("=" * 10)
            for subtipo in subtipos:
                print(f"- {subtipo}")
            print()


class Video(Anuncio):
    """Clase que representa un anuncio de tipo Video.

    Args:
        subtipo (str): El subtipo del anuncio de video. Debe estar en la lista SUB_TIPOS.
        duracion (int): La duración del video en segundos.

    Attributes:
        duracion (int): La duración del video en segundos.
        SUB_TIPOS (list): Lista de subtipos válidos para el anuncio de tipo Video.
    """

    SUB_TIPOS = ["instream", "outstream"]

    def __init__(self, subtipo, duracion):
        """Inicializa un objeto de la clase Video.

        Args:
            subtipo (str): El subtipo del anuncio de video.
            duracion (int): La duración del video en segundos.

        Raises:
            SubTipoInvalidoError: Si el subtipo no es válido.
        """
        super().__init__(subtipo, ancho=1, alto=1)
        if subtipo not in Video.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {subtipo} no es válido para Video")

        self.duracion = duracion if duracion > 0 else 5

    def comprimir_anuncio(self):
        """Muestra un mensaje indicando que la compresión no está implementada."""
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Muestra un mensaje indicando que el redimensionamiento no está implementado."""
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

    @property
    def duracion(self):
        """Obtiene la duración del video.

        Returns:
            int: La duración del video en segundos.
        """
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        """Establece la duración del video.

        Args:
            value (int): La nueva duración del video en segundos.
        """
        self._duracion = value if value > 0 else 5

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

    def comprimir_anuncio(self):
        """Muestra un mensaje indicando que la compresión no está implementada."""
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Muestra un mensaje indicando que el redimensionamiento no está implementado."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

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

    def comprimir_anuncio(self):
        """Muestra un mensaje indicando que la compresión no está implementada."""
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Muestra un mensaje indicando que el redimensionamiento no está implementado."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

    def __str__(self):
        """Devuelve una representación en cadena del anuncio de social.

        Returns:
            str: Representación en cadena del anuncio de social.
        """
        return f"Social subtipo: {self.subtipo}"
