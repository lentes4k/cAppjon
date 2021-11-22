# Documentación del Dockerfile
### Elección del contenedor base
En este caso he optado por elegir el contenedor oficial de `Python` en su versión `alpine` ya que prescinde de muchas librerias innecesarias y ahorramos memoria buscando la livianidad del contenedor.
### Instalación de librerias
Instalamos el paquete `build-base` ya que es el contenedor del compilador `gcc` necesario para `Poetry` mi gestor de dependencias.


Además se instala la librereia `libffi-dev` por un error ocasionado durante la instalación de Poetry y consultado en [stackoverflow](https://stackoverflow.com/questions/31508612/pip-install-unable-to-find-ffi-h-even-though-it-recognizes-libffi)


### Uso del dockerfile
Finalmente crearemos un entorno virtual para trabajar con Python, ahí instalamos Poetry y ya lanzamos nuetro test.
