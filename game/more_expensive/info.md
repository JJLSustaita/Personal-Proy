# Juego de Comparación de Objetos

## Descripción
Este es un juego interactivo donde los jugadores deben adivinar cuál de dos objetos tiene un mayor valor monetario. A través de rondas de comparación, el jugador acumula puntos al hacer las elecciones correctas. El juego es educativo, divertido y está diseñado para desafiar el conocimiento de los jugadores sobre el valor de los objetos cotidianos.

## Características
- **Interfaz Visual:** El juego presenta imágenes de los objetos junto a botones para facilitar la selección.
- **Contador de Nivel:** Cada vez que el jugador adivina correctamente, se suma un punto al contador de nivel.
- **Aleatoriedad en las Comparaciones:** Las comparaciones de objetos son seleccionadas de manera aleatoria, y no se repiten en la misma sesión de juego.
- **Pantalla de Inicio:** Incluye una pantalla inicial con la opción de jugar y regresar si se pierde.
- **Manejo de Resultados:** Si el jugador elige incorrectamente, se le muestra la respuesta correcta y se regresa a la pantalla de inicio.
- **Soporte de Archivos:** Los datos de los objetos y sus precios se cargan desde un archivo Excel.

## Estructura del Proyecto

La estructura de archivos es la siguiente:

mi_juego/
│
├── data/
│   └── objetos.xlsx           # Archivo Excel con datos de los objetos
│
├── images/                    # Carpeta para las imágenes de los objetos
│   ├── objeto1.png
│   ├── objeto2.png
│   ├── objeto3.png
│   └── ...                    # Otras imágenes de objetos
│
├── sounds/                    # Carpeta para los sonidos (si decides incluir)
│   ├── correcto.wav           # Sonido para respuesta correcta
│   ├── incorrecto.wav         # Sonido para respuesta incorrecta
│   └── fondo_musica.mp3       # Música de fondo (opcional)
│
├── src/                       # Carpeta para el código fuente del juego
│   ├── main.py                # Archivo principal del juego
│   ├── game.py                # Lógica principal del juego
│   ├── ui.py                  # Manejo de la interfaz de usuario
│   ├── data_handler.py        # Carga y manejo de datos (Excel)
│   └── utils.py               # Funciones útiles (como la aleatoriedad)
│
└── README.md                  # Archivo README con información del proyecto

