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
En primer lugar, pytest, que nos lanzará una ejecución de los archivos que tenemos. En la carpeta `test` tenemos 4 archivos. Sólo uno de ellos ejecuta de manera correcta. Los demás arrojarán el error que comprobará el funcionamiento correcto de la clase `nota`. 
~~~
poetry run pytest
~~~
También podemos hacer uso de `pylint` con esta línea de comando
~~~
poetry run pylint
~~~

Podremos comprobar la compilación correcta de nuestra clase con 
~~~
poetry run check
~~~


Para hacerlo aún más fácil, se incluye un `script` que nos lanzará todos los tests programados. Para hacer uso del mismo basta con lanzar
~~~
poetry run test
~~~


Podremos añadir nuevos tests al directorio `test` y lanzarlos con:
~~~
poetry run /test/"nombre.py"
~~~
O al introducir `taskipy` podemos añadir lanzamientos de tareas en `[tool.taskipy.tasks]`


Finalmente podremos lanzar la aplicación con 
~~~
poetry run nombre_app.py
~~~
