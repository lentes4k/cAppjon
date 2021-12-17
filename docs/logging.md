# Logging
### Elección de la herramienta de logging
Para llevar el registro de logs he tomado la decisión de usar `logging` la herramienta que por defecto trae el lenguaje usado,
`python`.


La justificación, ~~aunque es un poco pobre en fundamento~~, se basa en que es mejor gestionar un proyecto cuanto menor es
el número de sus dependencias.Así, en caso de vulnerabilidades no hay que montar una fiesta para sustituir dicha dependencia.


Otra de las razones por la que se ha usado esta herramienta en el proyecto es por su buena [documentación](https://docs.python.org/3/library/logging.html).


Del mismo modo, si se busca en Google información sobre el regustro de logs es el principal resultado que se obtiene. Igualmente ocurre
si buceamos un poco por las preguntas relacionadas a esta actividad en StackOverFlow.


### Elección de la herramienta de configuración
En este caso la justificación sigue siendo baladí, habiendo usado la herramienta comentada en clase.


Si bien es cierto que a nada que busquemos un poco sobre este tema, la mayoría de usuarios en la red recomiendan el uso de [`dotenv`](https://pypi.org/project/python-dotenv/)
para leer las variables de entorno.
Es por ello que se ha optado por esta herramienta.


Para evitar errores de no existencia de archivos `.env` se crearán en el archivo correspondiente ([`config.py`](https://github.com/lentes4k/cAppjon/blob/objetivo-7/cappjon/config.py)
los archivos por defecto.
