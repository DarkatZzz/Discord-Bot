# Bot de Música en Discord

Este proyecto es un bot de música en Discord, diseñado para permitir a los usuarios reproducir, pausar, reanudar, saltar y detener canciones de YouTube en un servidor de Discord. El bot también admite la administración de una cola de reproducción para una experiencia de escucha ininterrumpida.

  ## Características

    - Reproducir canciones de YouTube a través de URL o términos de búsqueda
    - Cola de canciones para la reproducción continua
    - Comandos para pausar, reanudar, saltar y detener la reproducción de canciones
    - Eliminación automática de archivos de canciones después de la reproducción
    - Limitación de tamaño de archivo para evitar la descarga de archivos de audio demasiado grandes

  ## Requisitos

    - Python 3.6+
    - Un token de bot de Discord
    - Bibliotecas de Python enumeradas en `requirements.txt`

 Uso
  Para usar el bot de música en Discord, invita al bot a tu servidor e ingresa los siguientes comandos:

    #play <URL de YouTube o término de búsqueda>: Reproduce una canción de YouTube o añade una canción a la cola.
    #pause: Pausa la reproducción de la canción actual.
    #resume: Reanuda la reproducción de la canción actual.
    #skip: Salta a la siguiente canción en la cola.
    #stop: Detiene la reproducción y limpia la cola.
