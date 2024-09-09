
from anuncio import Video, Display, Social
from POO.error import LargoExcedidoError

class Campaña:
    def __init__(self, nombre, anuncios):
        self._nombre = nombre
        self._anuncios = anuncios

    # Sobrecarga de __str__ para mostrar el formato correctamente
    def __str__(self):
        video_count = sum(1 for anuncio in self._anuncios if isinstance(anuncio, Video))
        display_count = sum(1 for anuncio in self._anuncios if isinstance(anuncio, Display))
        social_count = sum(1 for anuncio in self._anuncios if isinstance(anuncio, Social))

        return (f"Nombre de la campaña: {self._nombre}\n"
                f"Anuncios: {video_count} Video, {display_count} Display, {social_count} Social")

    # Propiedades con getter y setter
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) > 250:
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres.")
        self._nombre = value

    @property
    def anuncios(self):
        return self._anuncios

    @anuncios.setter
    def anuncios(self, value):
        self._anuncios = value
