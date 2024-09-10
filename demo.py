from campaña import Campaña
from anuncio import Video, SubTipoInvalidoError
from error import LargoExcedidoError


def log_error(error_message):
    """Registra un mensaje de error en un archivo log.

    Args:
        error_message (str): El mensaje de error que será escrito en el archivo de log.
    """
    with open("error.log", "a") as log_file:
        log_file.write(f"Error: {error_message}\n")


def main():
    """Función principal que modifica los valores de los atributos de una campaña ya creada."""
    # Crear una instancia de Campaña con un solo anuncio de tipo Video
    anuncio_video = Video(subtipo="instream", duracion=10)
    campaña = Campaña(nombre="Campaña Inicial", anuncios=[anuncio_video])

    try:
        # Solicitar un nuevo nombre para la campaña
        nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
        campaña.nombre = nuevo_nombre

        # Solicitar un nuevo subtipo para el anuncio
        nuevo_subtipo = input(
            "Ingrese el nuevo subtipo para el anuncio de video (instream/outstream): "
        ).lower()
        campaña.anuncios[0].subtipo = nuevo_subtipo

    except (LargoExcedidoError, SubTipoInvalidoError) as e:
        log_error(str(e))
        print(f"Error: {str(e)}")

    # Mostrar la campaña actualizada
    print(campaña)


if __name__ == "__main__":
    main()
