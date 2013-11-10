Practica 2 Copyright (C) 2013 María Victoria Santiago Alcalá. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see .

Practica2
=========
### INTRODUCCION
En esta práctica vamos a crear una aplicación web simple y la vamos a aislar en una jaula chroot con Ubuntu 13.10.
Para ello, lo instalaremos todo con permisos de superusuario para no tener problemas.

### Creación de la jaula
En primer lugarcreamos las carpetas y cambiamos el propietario a root, luego creamos la jaula como se muestra a continuacion en el siguiente volcado de pantalla:

![Practica2](https://dl.dropbox.com/s/qwjy488qmrzglq7/pract2IV.png)

Con ello tendriamos creada la jaula. Ahora procedemos a instalar los paquetes, bibliotecas y demás para que la aplicación funcione.
Entramos con chroot e instalamos en nuestro caso python 2.7 que es el lenguage en el que está realizada la aplicación.

![Practica2](https://dl.dropbox.com/s/b1kg8k3ijwy7qu2/p2iv1.png)


De la siguiente forma procedemos a crear el usuario en la jaula con la contraseña:
![Practica2](https://dl.dropbox.com/s/uc17zky8008baup/user.png)
