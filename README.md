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
En primer lugarcreamos las carpetas y cambiamos el propietario a root, luego creamos la jaula como se muestra a continuacion en el siguiente volcado de pantalla:

sudo chroot /home/jaulas/quantal
![Practica2](https://dl.dropbox.com/s/qwjy488qmrzglq7/pract2IV.png)

Con ello tendriamos creada la jaula. Ahora procedemos a entrar con chroot.

