from anuncio import Video, Display, Social
from error import LargoExcedidoError


class Campaña:
    """Clase que representa una campaña publicitaria compuesta por varios anuncios.

    Args:
        nombre (str): El nombre de la campaña.
        anuncios (list): Lista de objetos que representan los anuncios de la campaña.

    Attributes:
        _nombre (str): Nombre de la campaña.
        _anuncios (list): Lista de anuncios asociados a la campaña.

    Methods:
        __str__: Devuelve una representación en cadena de la campaña, incluyendo el nombre y el conteo de anuncios.
        nombre: Propiedad getter y setter para el nombre de la campaña.
        anuncios: Propiedad getter y setter para la lista de anuncios.
    """

    def __init__(self, nombre, anuncios):
        """Inicializa un objeto de la clase Campaña.

        Args:
            nombre (str): El nombre de la campaña.
            anuncios (list): Lista de objetos que representan los anuncios de la campaña.
        """
        self._nombre = nombre
        self._anuncios = anuncios

    def __str__(self):
        """Devuelve una representación en cadena de la campaña.

        Incluye el nombre de la campaña y el número de anuncios de cada tipo (Video, Display, Social).

        Returns:
            str: Información de la campaña con su nombre y la cantidad de anuncios por tipo.
        """
        video_count = sum(1 for anuncio in self._anuncios if isinstance(anuncio, Video))
        display_count = sum(
            1 for anuncio in self._anuncios if isinstance(anuncio, Display)
        )
        social_count = sum(
            1 for anuncio in self._anuncios if isinstance(anuncio, Social)
        )

        return (
            f"Nombre de la campaña: {self._nombre}\n"
            f"Anuncios: {video_count} Video, {display_count} Display, {social_count} Social"
        )

    @property
    def nombre(self):
        """Obtiene el nombre de la campaña.

        Returns:
            str: El nombre de la campaña.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """Establece el nombre de la campaña.

        Args:
            value (str): El nuevo nombre de la campaña.

        Raises:
            LargoExcedidoError: Si el nombre excede los 250 caracteres.
        """
        if len(value) > 250:
            raise LargoExcedidoError(
                "El nombre de la campaña excede los 250 caracteres."
            )
        self._nombre = value

    @property
    def anuncios(self):
        """Obtiene la lista de anuncios de la campaña.

        Returns:
            list: Lista de anuncios asociados a la campaña.
        """
        return self._anuncios

    @anuncios.setter
    def anuncios(self, value):
        """Establece la lista de anuncios de la campaña.

        Args:
            value (list): La nueva lista de anuncios asociados a la campaña.
        """
        self._anuncios = value
