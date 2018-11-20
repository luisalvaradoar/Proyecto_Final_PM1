---------------- ventana de "Inicio de sesión" ---------------------
En ella podrá ingresar a la plataforma si cuenta con un usuario y 
contraseña existentes en la base de datos de usuarios y contraseñas 
(archivo "usuarios.pas").

En la ventana hay tres botones:
- Ingresar: ingresa a la plataforma si el usuario y contraseña son 
validos
- Crear usuario: abre la ventana "Nuevo usuario"
- Recuperar mi contraseña: envía un correo al correo que se encuentra
en el campo 'usuario' con la contraseña de este mismo

---------------- ventana de "Nuevo usuario" ------------------------
En esta ventana podrá crear un nuevo usuario el cual se agregara a
la base de datos de usuarios y contraseñas (archivo "usuarios.pas").


---------------- ventana de "Guatecompras" -------------------------
Acá existen tres pestañas:
- Compras 2016
- Compras 2017
- Compras 2018
- Gráficas y análisis

En las primeras tres existe un panel de selección con las siguientes
cuatro opciones:
- Compras más grandes
- Compra más grande realizada por mes
- Compras más grandes realizas por la USAC
- Top 10 de los proveedores que más vendieron

Al seleccionar una de estas y presionar el botón "Generar" el programa
analizara los datos y después de cierto tiempo (durante el cual el
programa se bloqueara) se creara una gráfica y una tabla en la pestaña
"Gráficas y análisis".

En las primeras tres pestañas se encuentra el botón "Ingresar datos"
el cual abre la ventana "Agregar datos de compra".

En la pestaña Gráficas y análisis hay un botón con el nombre "Generar
reporte en PDF" el cual al ser presionado genera un PDF con los
resultados de un reporte previamente generado.

---------------- ventana de "Agregar datos de compra" --------------
Esta ventana permite ingresar una nueva compra al json del  año de
la pestaña en la que se abrió.

---------------- menú "Archivo" ------------------------------------
Este menú se encuentra en la ventana "Guatecompras", este tiene tres
opciones:
- Guardar sesión
- Abrir sesión 
- Salir del programa

La primera opción funciona luego de haber generado un reporte. La
segunda opción abre la ventana "Cargar sesión". La ultima opción
cierra la ventana "Guatecompras"

---------------- ventana de "Cargar sesión" ------------------------
En esta ventana podrá tener acceso a las sesiones guardadas del
usuario. En ella podrá encontrar un combobox donde se despliegan
todas las sesiones guardadas, luego de seleccionar uno y presionar
el botón "Aceptar" carga dicha sesión.

---------------- detalles de la lectura de datos -------------------
El programa verifica la conexión a internet a la hora de generar los
reportes. Si hay acceso a internet, el programa se conectará al API
del ministerio de finanzas en caso contrario obtendrá los datos de
los json's.