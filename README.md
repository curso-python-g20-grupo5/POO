# Prueba de Programación orientada a objetos con python

## 1. Introducción a la Programación Orientada a Objetos (POO)
La POO es un paradigma que organiza el software en "objetos" que contienen tanto datos como comportamientos. Cada objeto es una instancia de una clase. Vamos a profundizar en los pilares clave:
- **Clases y Objetos**: las clases son plantillas para crear objetos. Por ejemplo, la clase ```Campania``` es una plantilla que define cómo deben ser las campañas (nombre, fechas, anuncios). Cada objeto de tipo ```Campania``` es una campaña con datos específicos.
- **Encapsulamiento**: es una técnica que protege los datos de un objeto, limitando el acceso directo a ellos. Esto es clave en el proyecto, ya que la clase ```Campania``` usa ```@property``` y ```@setter``` para validar el nombre antes de permitir cambios.
- **Herencia**: permite a las clases compartir código. En este proyecto, las clases ```Video```, ```Social``` y ```Display``` heredan de la clase base ```Anuncio```, lo que significa que comparten características comunes como ```ancho``` y ```alto```.
- **Polimorfismo**: se refiere a la capacidad de tratar a diferentes clases de manera uniforme, a pesar de que tengan comportamientos diferentes. En este código, se puede tratar cualquier tipo de anuncio (ya sea ```Video```, ```Display``` o ```Social```) como si fuera del tipo ```Anuncio```, pero cada uno tiene su propia implementación de métodos como ```comprimir_anuncio```.
- **Abstracción**: simplifica la interacción con objetos complejos. En este código, la clase abstracta ```Anuncio``` define métodos como ```comprimir_anuncio```, que deben ser implementados por las subclases (Video, Social, Display), simplificando el manejo de anuncios.
  
## 2. Explicación detallada de los archivos
a) ```anuncio.py```: este archivo contiene la clase base ```Anuncio``` y sus subclases ```Video```, ```Display```, y ```Social```. Aquí se hace uso del principio de **herencia** para evitar duplicación de código. Cada subclase representa un tipo específico de anuncio, pero todas comparten atributos comunes como `ancho` y `alto` que son definidos en ```Anuncio```.
_**Métodos abstractos**: `Anuncio` define algunos métodos abstractos que las subclases deben implementar, como```comprimir_anuncio```. Este es un ejemplo de cómo la **abstracción** simplifica el diseño, permitiendo que las subclases solo implementen los detalles específicos.
_**Getters y Setters**: son esenciales para encapsular los datos, asegurando que se validen correctamente antes de modificar atributos. Esto se puede ver en la validación del tamaño del anuncio.
b) ```campania.py```: esta clase representa una campaña que contiene una colección de anuncios. Al usar **composición**, la clase ```Campania``` contiene anuncios dentro de ella, pero no hereda de ```Anuncio```. La clase utiliza encapsulamiento para validar los nombres de las campañas y asegurarse de que no excedan los 250 caracteres.
- **Composición**: los anuncios dentro de `Campania` son instancias de diferentes clases (`Video`, `Display`, `Social`). Esto muestra cómo los objetos pueden estar formados por otros objetos, permitiendo una estructura flexible.
- **Excepciones**: si el nombre de la campaña es muy largo, se lanza una excepción personalizada ```LargoExcedidoError```. Este es un ejemplo de cómo manejar errores específicos de negocio dentro del código.
c) ```error.py```: este archivo define excepciones personalizadas que manejan errores específicos del negocio, como ```LargoExcedidoError``` o ```SubTipoInvalidoError```. Definir excepciones específicas hace que sea más fácil depurar y manejar errores en tiempo de ejecución.
d) ```demo.py```: este archivo es un ejemplo de cómo interactuar con las clases ```Campania``` y ```Anuncio```. Usa ```try/except``` para capturar y manejar excepciones. Si ocurre un error, como un nombre de campaña inválido o un subtipo incorrecto, el programa lo captura y registra en ```error.log```, en lugar de detenerse.

## 3. Detalles adicionales de la prueba de Programación Avanzada
Se solicita implementar la API de una aplicación de campañas publicitarias. Cada clase en el presente código representa una parte esencial de esta API. Algunas reglas clave de esta aplicación son:
- **Validaciones de los atributos**: el nombre de la campaña debe exceder los 250 caracteres y el subtipo de anuncio debe ser válido para el tipo de anuncio que se crea (Video, Display, Social).
- **Excepciones personalizadas**: se debe hacer uso de las excepciones personalizadas para manejar errores específicos, como ```SubTipoInvalidoError``` cuando un subtipo de anuncio no sea válido.
- **Composición**: las campañas deben contener múltiples anuncios, y el método ```__obtener_instancia_anuncio``` se encarga de crear los objetos correctos basados en los datos proporcionados.
- **Sobrecarga de métodos**: implementar métodos como ```__str__``` para mostrar los detalles de la campaña y sus anuncios de manera clara.

## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)

⌨️ con ❤️ por el Grupo 5 - G20 😊
