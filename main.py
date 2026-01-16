import discord
import os
import asyncio
from discord.ext import commands

#Configuración
TOKEN = os.getenv('TOKEN')
SOUND_FOLDER = "./sounds"

#Permisos del BotIntro (Intents)
intents = discord.Intents.default()
intents.voice_states = True 

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return
    
    #Detectará si el usuario entró a un canal (antes no estaba, pero ahora si)
    if before.channel is None and after.channel is not None:
        channel = after.channel

        #Buscará si existe un archivo con el nombre del usuario
        sound_file = os.path.join(SOUND_FOLDER, f"{member.name}.mp3")

        if os.path.exists (sound_file):
            print(f"Detectando mandril {member.name}, reproduciendo opening de mandril...")

            try:
                #Que se conecte al canal
                vc = await channel.connect()

                #Que reproduzca el sonido
                source = discord.FFmpegPCMAudio(sound_file)
                vc.play(source)

                #Esperar 1 segundo para que el audio arranque
                await asyncio.sleep(1)
            
                #Que salga al terminar la intro
                while vc.is_playing():
                    await asyncio.sleep(1)

                await vc.disconnect()

            except Exception as e:
                print(f"Error: {e}")
                #Que se desconecte el bot si salta un error
                if 'vc' in locals() and vc.is_connected():
                    await vc.disconnect()

bot.run(TOKEN)