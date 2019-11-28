# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from time import sleep

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    lol_quotes = ['A Marcos todo campeon del top le hace counter', 'Si Toni juega a KogMaw, salvese quien pueda',
                  'No os olvideis que hacer objetivos en el Lol es muy importante', '¿Quereis que os cuente un chiste? El farm de Marcos.',
                  'Un dragon al dia te da alegria', 'Un buen surrender a tiempo quita mucha tonteria', 'Si al Lol quereis ganar, al Yasuo debeis banear.', 'Cuidado con el flash asesino, que lo carga el diablo.',
                  'Toni, divear no es siempre la mejor de las decisiones, vete a base, venga va.']

    if 'lol' in message.content:
        response = random.choice(lol_quotes)
        sleep(2)
        await message.channel.send(response)

    tft_quotes = ['Si al TFT quieres ganar a Carly debes escuchar.', 'Si al TFT quieres perder al Marcos debes creer.', 'Si al TFT quieres sufrir al Toni has de seguir.',
                  'Si en el TFT quieres triunfar, Predator debes jugar.','Cuidado con los rolleos asesinos que llevan al lado oscuro.', 'Con Blademaster, no vas a ninguna parte.']

    if 'tft' in message.content:
        response = random.choice(tft_quotes)
        sleep(2)
        await message.channel.send(response)
           
                                   
client.run('MY TOKEN')    
