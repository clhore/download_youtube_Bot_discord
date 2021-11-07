# Codigo conalgunas mejoras y en funcionamiento
https://replit.com/@adrianlujan/bot-musica#main.py

# download_youtube_Bot_discord

### Crea un proyecto en https://console.cloud.google.com y habilita la Google Drive API
![](https://i.imgur.com/hmWrrdT.png)

### Añade el correo electronico que usaras luego para logearte al ejecutar el bot
![](https://i.imgur.com/FFM6NaW.png)

### Descarga las credenciales en JSON
![](https://i.imgur.com/KnIT73i.png)

### Renombra el archivo descargado a [client_secret.json]
![](https://i.imgur.com/TaMKGaz.png)

### Ahora con los datos de client_secret.json rellena los datos que faltan en settings.yaml
![](https://i.imgur.com/XEBzLsp.png)

### En la cuenta de drive del proyecto creamos una carpeta con un nombre culaquiera
      Debes de comaprtir la carpeta para que cualquiera con en elnlace pueda verla
    
![](https://i.imgur.com/nUwuwdZ.png)

### Obtener id de la carpeta
      Debes entrar en la carpeta y en la url aparecera la id de la carpeta
      Unavez copiado abrimos el archivo config.json y lo pegamos entre comillas en id_folder
    
![](https://i.imgur.com/mWSoJr5.png)
![](https://i.imgur.com/dkM4gQi.png)

### Añadimos el TOKEN de nuestro bot de discord en el campo [token] del archivo config.json
![](https://i.imgur.com/g0ERkyG.png)

### Y ejecutamos el main.py al ejecutarse nos abrira una pestaña en el navedador sino es asi copia la url que te mustra por terminal y pegela en el navegador
            En el sigiente enlace (https://drive.google.com/file/d/1TDJY77QWMgVOdCgPhC-bBwVYS4wTOKSd/view?usp=sharing) podra descargar un venv.zip que si lo descomprime y ejecuta el programa desde el python.exe que trae notrendra que intalar ninguna libreria en su equipo.
            En caso que deses ejecutralo con el python que tengas intalado en tu pc deberas intalar algunas libreryas para el correcto funcionamiento de la aplicacion.
### Inicie sesion con la cuenta que anteriormente puso como usuario de prueba

# Comandos:
### !commands
      Nosmuestra todos los comandos y como se usan
![](https://i.imgur.com/oEPBaue.png)

### !AU
      [1.0] Indica al bot que el link o los links que le pases, tiene que descargarlos en .mp3
      [1.1] Para descargar varios links solo tienes que poner una coma y sin espaciar poner el otro link
      
      [2.0] Si el archivo sobrepasa los 8MB se subira a Google Drive y te pasara un link
![](https://i.imgur.com/x7GsW4Z.png)
![](https://i.imgur.com/6BOLGTC.png)

### !VD
      [1.0] Indica al bot que el link o los links que le pases, tiene que descargarlos en .mp4
      [1.1] Para descargar varios links solo tienes que poner una coma y sin espaciar poner el otro link
      
      [2.0] Si el archivo sobrepasa los 8MB se subira a Google Drive y te pasara un link
![](https://i.imgur.com/tkbPKeU.png)
![](https://i.imgur.com/CoW7avZ.png)

### !delete [password]
      [1.0] Este comado elimina los videos subidos en Google Drive y los videos guardados en local en la carpeta video 
      
      [2.0] La contraseña default es 123.
      [2.1] Sepuede canviar en el archivo [config.josn]
![](https://i.imgur.com/OcGam28.png)


## Mejoras a implementar
      - Uso de thread en la descarga y la subida de archivos en drive.
      - Optimizar el codico asincrono
