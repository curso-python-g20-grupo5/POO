from campaña import Campaña
from anuncio import Video, Display, Social
from error import LargoExcedidoError, SubTipoInvalidoError


def log_error(error_message):
    """Registra un mensaje de error en un archivo log.

    Args:
        error_message (str): El mensaje de error que será escrito en el archivo de log.
    """
    with open("error.log", "a") as log_file:
        log_file.write(f"Error: {error_message}\\n")


def get_campaign_name():
    """Solicita al usuario ingresar el nombre de la campaña.

    Valida que el nombre de la campaña no exceda los 250 caracteres. Si se excede el límite,
    se imprime un mensaje de error y se registra en el log.

    Returns:
        str: El nombre de la campaña ingresado por el usuario.
    """
    while True:
        nombre_campaña = input("Ingrese el nombre de la campaña: ")
        if len(nombre_campaña) > 250:
            print("Error: El nombre de la campaña no puede exceder los 250 caracteres.")
            log_error("El nombre de la campaña excedió los 250 caracteres")
        else:
            return nombre_campaña


def get_anuncio_tipo():
    """Solicita al usuario seleccionar el tipo de anuncio.

    Presenta las opciones de Video, Display y Social, y valida que la selección sea válida.

    Returns:
        str: El tipo de anuncio seleccionado por el usuario.
    """
    while True:
        print("Seleccione el tipo de anuncio:")
        print("1. Video")
        print("2. Display")
        print("3. Social")
        tipo_anuncio = input("Ingrese el número correspondiente al tipo de anuncio: ")
        if tipo_anuncio == "1":
            return "Video"
        elif tipo_anuncio == "2":
            return "Display"
        elif tipo_anuncio == "3":
            return "Social"
        else:
            print("Error: Selección inválida.")
            log_error("Selección inválida de tipo de anuncio")


def get_anuncio_subtipo(tipo_anuncio):
    """Solicita al usuario ingresar el subtipo de anuncio según el tipo seleccionado.

    Valida que el subtipo ingresado sea válido de acuerdo con el tipo de anuncio seleccionado.

    Args:
        tipo_anuncio (str): El tipo de anuncio seleccionado (Video, Display o Social).

    Returns:
        str: El subtipo válido del anuncio ingresado por el usuario.
    """
    while True:
        if tipo_anuncio == "Video":
            subtipo = input("Ingrese el subtipo (instream/outstream): ").lower()
            if subtipo in Video.SUB_TIPOS:
                return subtipo
            else:
                print("Error: Subtipo de Video inválido.")
                log_error(f"Subtipo de Video inválido: {subtipo}")
        elif tipo_anuncio == "Display":
            subtipo = input("Ingrese el subtipo (tradicional/native): ").lower()
            if subtipo in Display.SUB_TIPOS:
                return subtipo
            else:
                print("Error: Subtipo de Display inválido.")
                log_error(f"Subtipo de Display inválido: {subtipo}")
        elif tipo_anuncio == "Social":
            subtipo = input("Ingrese el subtipo (facebook/linkedin): ").lower()
            if subtipo in Social.SUB_TIPOS:
                return subtipo
            else:
                print("Error: Subtipo de Social inválido.")
                log_error(f"Subtipo de Social inválido: {subtipo}")


def get_anuncio_dimensions():
    """Solicita al usuario ingresar las dimensiones del anuncio (ancho y alto).

    Valida que el ancho y el alto del anuncio sean iguales a 1. En caso contrario,
    muestra un error y lo registra en el log.

    Returns:
        tuple: Un par de enteros representando el ancho y el alto del anuncio.
    """
    while True:
        try:
            ancho = int(input("Ingrese el ancho del anuncio (debe ser 1): "))
            if ancho != 1:
                raise ValueError("El ancho debe ser igual a 1")
            alto = int(input("Ingrese el alto del anuncio (debe ser 1): "))
            if alto != 1:
                raise ValueError("El alto debe ser igual a 1")
            return ancho, alto
        except ValueError as e:
            print(f"Error: {e}")
            log_error(str(e))


def main():
    """Función principal que coordina la creación de una campaña publicitaria.

    Solicita al usuario los datos necesarios para crear una campaña con anuncios
    de diferentes tipos y subtipos, y maneja posibles excepciones.

    Raises:
        LargoExcedidoError: Si el nombre de la campaña excede los 250 caracteres.
        SubTipoInvalidoError: Si el subtipo de un anuncio es inválido.
    """
    try:
        # Obtener datos de la campaña
        nombre_campaña = get_campaign_name()
        tipo_anuncio = get_anuncio_tipo()
        subtipo_anuncio = get_anuncio_subtipo(tipo_anuncio)

        # Crear anuncio según el tipo seleccionado
        if tipo_anuncio == "Video":
            ancho, alto = get_anuncio_dimensions()
            duracion = int(input("Ingrese la duración del anuncio en segundos: "))
            anuncio = Video(ancho, alto, subtipo_anuncio, duracion)
        elif tipo_anuncio == "Display":
            anuncio = Display(subtipo_anuncio)
        elif tipo_anuncio == "Social":
            anuncio = Social(subtipo_anuncio)

        # Crear campaña
        campaña = Campaña(nombre_campaña, [anuncio])
        print(campaña)

    except (LargoExcedidoError, SubTipoInvalidoError) as e:
        log_error(str(e))
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
