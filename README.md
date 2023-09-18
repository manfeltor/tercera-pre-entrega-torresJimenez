# tercera-pre-entrega-TorresJimenez

Este proyecto es la tercer pre entrega del curso de python orientado a desarrollo web, de la comision 43880 dictado por la plataforma CoderHouse.

su principal componente es la aplicacion e3app del proyecto E3 de django, y su objetivo principal es tanto almacenar con entradas de tipo formulario y exponer como listados, las ventas, clientes y proveedores de un
negocio de venta minorista, principalmente administrado mediante URL's.

reporte bugs y sugerencias a manfeltor@live.com

## requerimientos

*Django
para instalar use en la terminal: pip install django

*Python
Recomendado version 3.11

## instalacion (con terminal)

clona este repositorio con el siguiente comando en la terminal, ubicandote en la carpeta en la que deseas clonar:
>>> git clone https://github.com/manfeltor/tercera-pre-entrega-torresJimenez

instala las dependencias necesarias desde terminal listadas antes.
>>> pip instal django

ejecuta la migracion de las bases de datos
>>> python manage.py make migrations
>>> python manage.py maigrate

inicia el servidor de desarrollo:
>>> python manage.py runserver

Tu aplicación debería estar funcionando en http://localhost:8000/.

## funcionamiento

la APP se administra principalmente por URLs, siendo el host*: http://127.0.0.1:8000/e3app

a continuacion las URL y su funcionamiento:

host*/

esta es la url nativa del host, con el template de la landing page para la app

host*/proveedores

esta URL lista los proveedores creados en la base de datos o un mensaje si no hay registros en su base de datos

host*/formproveedores

genera un formulario de carga para el registro de nuevos proveedores en la BD. retorna a <host>/proveedores si la carga es exitosa

host*/clientes

esta URL lista los proveedores clientes en la base de datos o un mensaje si no hay registros en su base de datos

host*/formclientes

genera un formulario de carga para el registro de nuevos clientes en la BD. retorna a <host>/clientes si la carga es exitosa

host*/ventas

esta URL lista las ventas en la base de datos o un mensaje si no hay registros en su base de datos

host*/formventas

genera un formulario de carga para el registro de nuevas ventas en la BD. retorna a <host>/ventas si la carga es exitosa

host*/buquedaproveedor

genera un formulario para la busqueda de proveedores cargados. utiliza el nombre como argumento y el tipo es busqueda aproximada (contiene...). renderiza a <host>/buscar con los argumentos y retorna la lista de coincidencias.

## licencia

El proyecto aun no cuenta con una licencia definida

