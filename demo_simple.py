from campania import Campania
from datetime import date
from anuncio import Video
from POO.error import SubTipoInvalidoError, LargoExcedidoError

# Crear una instancia de Campania con un solo anuncio de tipo Video
anuncios = [
    {
        "tipo": "video",
        "url_archivo": "https://example.com/video.mp4",
        "url_clic": "https://example.com/click",
        "sub_tipo": "instream",
        "duracion": 30,
    }
]

# Crear la campaña con un anuncio de tipo Video
campania = Campania("Campaña Inicial", date.today(), date.today(), anuncios)

# Mostrar la campaña inicial
print("Campaña creada:")
print(campania)

# Solicitar nuevo nombre y subtipo al usuario
try:
    # Solicitar un nuevo nombre para la campaña
    nuevo_nombre = input("\nIngrese un nuevo nombre para la campaña: ")
    campania.nombre = nuevo_nombre

    # Solicitar un nuevo subtipo para el anuncio de tipo video
    nuevo_sub_tipo = input(
        "Ingrese un nuevo subtipo para el anuncio de tipo video (instream/outstream): "
    ).lower()
    campania.anuncios[0].sub_tipo = nuevo_sub_tipo

except (SubTipoInvalidoError, LargoExcedidoError, ValueError) as e:
    # En caso de excepción, se registra en error.log
    with open("error.log", "a+") as log:
        log.write(f"Error: {e}\n")
    print(f"Ocurrió un error: {e}")

# Mostrar la campaña actualizada
print("\nCampaña actualizada:")
print(campania)
