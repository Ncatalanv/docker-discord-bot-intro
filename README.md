# Dockerized Discord Greeter Bot

Este proyecto es un microservicio en **Python** que monitorea los canales de voz en Discord y reproduce saludos especializados (`.mp3`) automáticamente cuando un usuario específico se conecta al canal. 

Está diseñado para ser desplegado fácilmente mediante **Docker**, eliminando los problemas de compatibilidad de dependencias (tales como `ffmpeg`).

## Tecnologías

* **Lenguaje:** Python 3.9 (Asyncio, discord.py)
* **Infraestructura:** Docker (Containerization)
* **Audio Processing:** FFmpeg

### Prerrequisitos
* Docker instalado
* Un bot token de Discord

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Ncatalanv/docker-discord-bot-intro.git](https://github.com/Ncatalanv/docker-discord-bot-intro.git)
cd docker-discord-bot-intro
```

### 2. Construir la Imagen
```bash
docker build -t voice-greeter .
```

### 3. Ejecutar el contenedor
Hay que ejecutar el contenedor en segundo plano (-d), ingresando tu Token de Discord y conectando tu carpeta de sonidos local:

```
docker run -d \
  --name mi-bot \
  --restart=always \
  -e TOKEN=TU_TOKEN_ACA \
  -v "${PWD}/sounds:/app/sounds" \
  intro-bot
```

### Configuración de sonidos

El bot utiliza el **nombre usuario único** de cada persona para identificar qué sonido reproducir
1. Coloca tus archivos .mp3 en la carpeta sounds/
2. El nombre del archivo debe coincidir con el usuario.

### Ejemplo:
* Usuario: nico99 -> Archivo: sounds/nico99.mp3
* Usuario: ignacio777 -> Archivo: sounds/ignacio777.mp3


Proyecto desarrollado como parte de mi portafolio de Ingeniería de Datos.

