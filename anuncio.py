
from abc import ABC, abstractmethod
from POO.error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, subtipo):
        self._subtipo = subtipo
    
    @abstractmethod
    def __str__(self):
        pass
    
    # Getter y Setter para subtipo
    @property
    def subtipo(self):
        return self._subtipo
    
    @subtipo.setter
    def subtipo(self, value):
        self._subtipo = value


class Video(Anuncio):
    SUB_TIPOS = ["instream", "outstream"]
    
    def __init__(self, ancho, alto, subtipo, duracion):
        super().__init__(subtipo)
        if subtipo not in Video.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {subtipo} no es válido para Video")
        
        self.ancho = ancho if ancho > 0 else 1
        self.alto = alto if alto > 0 else 1
        self.duracion = duracion
    
    def __str__(self):
        return f"Video subtipo: {self.subtipo}, dimensiones: {self.ancho}x{self.alto}, duración: {self.duracion} seg"


class Display(Anuncio):
    SUB_TIPOS = ["tradicional", "native"]
    
    def __init__(self, subtipo):
        super().__init__(subtipo)
        if subtipo not in Display.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {subtipo} no es válido para Display")
    
    def __str__(self):
        return f"Display subtipo: {self.subtipo}"


class Social(Anuncio):
    SUB_TIPOS = ["facebook", "linkedin"]
    
    def __init__(self, subtipo):
        super().__init__(subtipo)
        if subtipo not in Social.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {subtipo} no es válido para Social")
    
    def __str__(self):
        return f"Social subtipo: {self.subtipo}"

