# Integración continua
Para el hito 6 se pedía la configuración de dos sistemas diferentes de CI; y que en cada uno de ellos se hicieran tareas diferentes.
Se pedía que una de estas tareas fuera el testeo del código en diferentes versiones del lenguaje elegido.

### CircleCI
La primera herramienta elegida ha sido CircleCI, por su facilidad de integración y de uso en lo referente al lanzamiento de tests.

En esta herramienta hemos lanzado nuestro contenedor en una máquina para que compruebe que los tests se lanzan de forma correcta.

### GitHub Actions
Esta herramienta ha sido seleccionada tras los requisitos restrictivos que ofrecía [Travis](https://travis-ci.org/) para crear un test que comprobasen el funcionamiento de nuestro código en diferentes versiones del
lenguaje usado, en nuestro caso Python.

Para ello hacemos el uso de la matrix de las GH Actions y definimos un pool con las 3 últimas versiones estables de Python. Una vez creado esto, 
instalamos las correspondientes dependencias de nuestro proyecto y lanzamos los tests programados en nuestro código que comprueban el correcto funcionamiento del mismo.
