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

### 1. Construir la Imagen
```bash
docker build -t voice-greeter .