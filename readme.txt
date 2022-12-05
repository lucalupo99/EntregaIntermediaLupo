Informacion sobre el trabajo:
--------------------------------------------------------------------------------------------------------------------------
- En la carpeta templates/Peluqueria encontraremos los html que se visualizan a travez del localhost, los mismos tienen herencia del codigo padre, a su vez llamado "Padre.html".

- En la carpeta admin.py encontraremos los datos de admin, los mismos se visualizan en el localhost apartado admin en el cual para ingresar deberemos de usar el | username: admin, contraseña: admin123 |, dentro de este podremos encontrar los registros hechos a traves de la pagina o mismo crearlos desde este lugar.

- En la carpeta forms.py encontraremos los formularios basicas de ingreso de datos que se encontraran de forma visual en nuestro servidor/pagina, en estos incluye datos ya sea nombre, telefono, email, apellido, etc.

- En la carpeta models.py encontraremos los modelos de los mismos datos mencionados en el anterior punto.

- En la carpeta urls.py encontraremos las urls de nuestro servidor, los mismos se basan principalmente con el llamado "Peluqueria/" que a su vez esta es mi app.

- En la carpeta views.py encontraremos nuestro codigo de back, el mismo se encargar de automatizar el proceso de formularios automatizando lo mismo, y guardando el registro de datos, apartado de esto tambien encontraremos el codigo de "Buscar" lo cual en un futuro servira para poder buscar productos deseados en la pagina/server cuando los mismos se encuentren registrados por nuestros clientes o mismo por nosotros.

--------------------------------------------------------------------------------------------------------------------------

Para iniciar el mismo programa deberemos de seguir los siguientes pasos:
1- Chequear que nos encontramos en la carpeta donde se encuentra el manage.py, para lo mismo deberemos de ingresar en la terminal de VSCode "dir", al darnos los resultados si se encuentra el archivo mencionado estamos en el lugar correcto, de lo contrario deberiamos de escribir "cd EntregaUno".
2- Ya encontrado el archivo manage.py, procedemos a ingresar en la terminal "py manage.py runserver" o "python manage.py runserver", en este momento comenzara a correr el programa.
3- Procedemos a ingresar a google y poner la url "localhost:8000", aqui entraremos en la pagina principal de nuestro programa, la misma nos mostrara las urls adyacentes de la app.
4- Procedemos a agregar a nuestra url el llamado que queremos hacer, ya sea para ir a admin "localhost:8000/admin" o para ingresar a nuestra app "localhost:8000/Peluqueria".
5- En el menu de admin, podremos administrar, revisar, eliminar o agregar datos ya sea de nuestros Clientes, Productos o mismo revisar los turnos pendientes o por dar.
6- En el menu de Peluqueria podremos ver nuestra pagina funcional con todas las opciones antes mencionadas las cuales podran ser utilizadas por cualquier persona que ingrese a la misma.

--------------------------------------------------------------------------------------------------------------------------

¿Por que decidi crear y llamar a la aplicacion Peluqueria?
La aplicacion se llama Peluqueria y me inspire en que mi mamá trabaja de esto y no tiene un sistema facil de agendado de clientes o turnos entonces se me ocurrio como idea en mi comienzo de progación intentar generar una pagina para ella que pueda utilizar en un futuro, este es mi primer proyecto es y espero que sea agradable a la vista y no un desastre de por si. Desde ya muchas gracias y un cordial saludo. Luca
