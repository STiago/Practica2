Practica 2 Copyright (C) 2013 María Victoria Santiago Alcalá. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see .

Practica2. Aislamiento de una aplicación web usando una jaula chroot
=========
### INTRODUCCION
En esta práctica vamos a crear una aplicación web en Python de una pagina web donde se pueden registrar usuarios, modificar y visualizar sus datos. Seguidamente vamos a aislar dicha aplicación en una jaula chroot con Wheezy.
Para ello, lo instalaremos todo con permisos de superusuario para no tener problemas.

###Nota
El template usado en la aplicación es una plantilla gratuita descargada de la siguente página:

http://www.freewebsitetemplates.com/

### Creación de la jaula
En primer lugar instalamos el sistema operativo y lo aislamos en una jaula con la linea de comandos siguiente:
sudo debootstrap --arch=i386 wheezy /seguro/jaulas/p2 http://ftp.us.debian.org/debian

![Practica2](https://dl.dropbox.com/s/et14umdakwmx2bb/algo1.png)

Con ello tendriamos creada la jaula. 

Tras realizar la instalación del sistema hacemos un chroot para accecer a la jaula y comprobar que esta todo correcto como muestra la siguiente captura.
![Practica2](https://dl.dropbox.com/s/poz0wxkew2bfekc/algo2.png)

A continuación, creamos el usuario con adduser seguido del nombre que le queramos dar al usuario y una vez ahi, introducimos sus datos (opcional) y la contraseña con su correspondiente confirmación.

![Practica2](https://dl.dropbox.com/s/ftbvvbfmoxncqch/algo3usuario.png)


Ahora, vamos al fichero de configuración para asegurar que a la jaula solo acceden el usuario que acabamos de crear y el root.
A continuación en el siguiente volcado de pantalla muestro el fichero de configuración de wheezy en el cual e introducido en el campo user el nombre de mi usuario creado anterior mente, en mi caso "pepe"

![Practica2](https://dl.dropbox.com/s/960e0o1shi1hvrz/algo4config.png)


Para ver que todo lo realizado se ha aplicado correctamente, accedemos a la jaula con nuestro usuario haciendo lo siguiente:

![Practica2](https://dl.dropbox.com/s/leirtk2bep507uh/algo5pruebadeloanterior.png)


Realizado todo lo anterior, procedemos a instalar todos los paquetes y bibliotecas necesarias para el funcionamiento de nuestra aplicación web en nuestro sistema.

Primero montamos los sistemas de ficheros proc y devpts con "mount -t proc proc /proc", "mount devpts /dev/pts -t devpts" e instalamos python 2.7 con "apt-get install python" como se muestra a continuación:

![Practica2](https://dl.dropbox.com/s/4c0r0e6a3nfe7sy/algo6montareinstallpython.png)










