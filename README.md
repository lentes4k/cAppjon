# cAppjón de sastre
Al estilo post-it, vamos dejando muchas notas digitales por aquí y por allá. Desde el mítico grupo contigo mismo a un `.txt` en tu ordenador pasando por los mensajes guardados de Twitter o Instagram.
Básicamente somos unos Diógenes digitales. Porque, ¿a quién no le ha pasado eso de abrir la aplicación de notas de nuestro móvil y ver un mensaje super críptico? ¿qué queríamos hacer recordar a nuestro yo del futuro?
Esto se acaba con la llegada de *cAppjón de sastre* o *cAppjón* para nuestros usuarios más cercanos.
*cAppjón* va a dedicarse a almacenar por nosotros toda la info que queremos dejar por ahí.
Para ello se va a servir de varios de *cajones* (~~una suerte de sistema de carpetas como hemos almacenado cosas de toda la vida vaya~~) prediseñados para almacenar las notas que tomamos rapidísmo sin preocuparnos por donde las dejamos, puesto que la super inteligencia de la aplicación sabrá a que *cajón* debe de ir.


### Instalación y uso
Para comenzar, será necesario clonar el repositorio en su máquina. (git clone "")


Una vez lo tengamos en nuestra máquina tendremos que [instalar *poetry*](https://python-poetry.org/docs/) 


Ahora tendremos que lanzar 
~~~
poetry install
~~~
Si tenemos un archivo `.lock` nos instalará las dependencias que el programador (o jefe de proyecto) ha usado.
En caso contrario instalará las que la herramienta opine y generará el archivo `.lock`.


Vamos a verificar que el archivo `pyproject.toml` es correcto con:
~~~
poetry check
~~~


Ahora podemos correr los tests. En nuestro caso se encuentran incluídos `pytest` y `pylint`.


Para lanzarlos ejecutar lo siguiente:
~~~
poetry run pytest
~~~
~~~
poetry run pylint
~~~


Podremos añadir nuevos tests al directorio `test` y lanzarlos con:
~~~
poetry run /test/"nombre.py"
~~~


Finalmente podremos lanzar la aplicación con 
~~~
poetry run nombre_app.py
~~~
