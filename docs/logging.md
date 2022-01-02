# Logging
### Elección de la herramienta de logging
Para llevar el registro de logs he tomado la decisión de usar `logging` la herramienta que por defecto trae el lenguaje usado,
`python`.


La justificación, ~~aunque es un poco pobre en fundamento~~, se basa en que es mejor gestionar un proyecto cuanto menor es
el número de sus dependencias.Así, en caso de vulnerabilidades no hay que montar una fiesta para sustituir dicha dependencia.


Otra de las razones por la que se ha usado esta herramienta en el proyecto es por su buena [documentación](https://docs.python.org/3/library/logging.html).


Del mismo modo, si se busca en Google información sobre el regustro de logs es el principal resultado que se obtiene. Igualmente ocurre
si buceamos un poco por las preguntas relacionadas a esta actividad en StackOverFlow.

Se han explorado opciones como [Loguru](https://github.com/Delgan/loguru) cuyo branding es curioso.
Además sus funciones facilitan mucho la configuración de formato. Por ejemplo la función `add` aporta bastante en una sola línea. En mi opinión es una muy buena herramienta, podría haber sido la elegida, pero como se comentó
anteriorente esto llevaría la instalación de una nueva dependencia que aumentaría el tamaño del proyecto.
Y en este caso, al ser un proyecto tan pequeño y simple sería añadir una posible vulnerabilidad y el aumento de tamaño
en disco.
Analizado esta herramienta podemos observar que para un proyecto algo más grande y serio sería una excelente opción.


Otra opción explorada ha sido [log.py](https://github.com/SebastiaanBij/log.py). Otra opción minimalista y en desarrollo. Esta herramienta parece ser bastante sencilla y adecuada para proyectos pequeños. Dispone de varias utilidades que permiten customizar las opciones de logging y en definitiva es usable.
Me gusta que el creador aporta ejemplos para ilustrar el potencial de su herramienta.
Como contrapunto nos encontramos que el desarollo es llevado por una sola persona, y aunque mantiene el proyecto vivo corremos el riesgo de que no pueda parchear posibles vulnerabilidades a tiempo.


### Elección de la herramienta de configuración
En este caso la justificación sigue siendo baladí, habiendo usado la herramienta comentada en clase.


Si bien es cierto que a nada que busquemos un poco sobre este tema, la mayoría de usuarios en la red recomiendan el uso de [`dotenv`](https://pypi.org/project/python-dotenv/)
para leer las variables de entorno.
Es por ello que se ha optado por esta herramienta.


Para evitar errores de no existencia de archivos `.env` se crearán en el archivo correspondiente ([`config.py`](https://github.com/lentes4k/cAppjon/blob/objetivo-7/cappjon/config.py)
los archivos por defecto.
