
# error.py

class LargoExcedidoError(Exception):
    """Excepción lanzada cuando el nombre de la campaña excede los 250 caracteres."""
    pass

class SubTipoInvalidoError(Exception):
    """Excepción lanzada cuando el subtipo de anuncio no es válido."""
    pass
