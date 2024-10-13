import discord
import requests
from discord.ext import commands, tasks
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
intents.message_content = True

# Crear un bot en la variable bot y transferirle los privilegios
bot = commands.Bot(command_prefix='!', intents=intents)

# Los eco consejos
eco_consejos = [
    "Apaga las luces cuando salgas de una habitación.", 
    "Lleva una botella de agua reutilizable para reducir el uso de plásticos.", 
    "Usa transporte público o bicicleta en lugar de conducir.", 
    "Recicla adecuadamente tus desechos para disminuir la basura.", 
    "Evita comprar productos con exceso de empaques plásticos."
]

# Evento para cuando el bot esté listo
@bot.event
async def on_ready():
    print(f'Bot {bot.user} está conectado.')
    eco_consejo_diario.start()  # Inicia la tarea diaria cuando el bot se conecta

# Función !eco_consejo
@bot.command()
async def eco_consejo(ctx):
    consejo = random.choice(eco_consejos)  # Corrección: 'eco_consejo' -> 'eco_consejos'
    await ctx.send(consejo)
    
# Mensaje diario
@tasks.loop(hours=24)
async def eco_consejo_diario():
    canal = bot.get_channel("id de tu canal de discord")  # Asegúrate de tener el ID correcto del canal
    if canal:
        consejo = random.choice(eco_consejos)
        await canal.send(f"🌱 Consejo ecológico del día: {consejo}")

# Función !calcular_huella
@bot.command()
async def calcular_huella(ctx):
    '''Calcula una estimación básica de huella de carbono con preguntas sencillas'''
    preguntas = [
        "¿Cuántos kilómetros conduces por semana?",
        "¿Cuántas veces comes carne a la semana?",
        "¿Cuántas horas por día dejas las luces encendidas?"
    ]
    respuestas = []
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
        
    for pregunta in preguntas:
        await ctx.send(pregunta)
        respuesta = await bot.wait_for('message', check=check)
        respuestas.append(respuesta.content)

    # Suma de respuestas para una aproximación estimada
    huella = sum(map(int, respuestas)) * random.randint(10, 20)
    await ctx.send(f"Tu huella de carbono aproximada es de {huella} kg de CO2 por mes.")

# Función !recordatorio_eco
@bot.command()
async def recordatorio_eco(ctx):
    '''Envía un recordatorio ecológico para promover hábitos sostenibles'''
    recordatorios = [
        "🌱 Recuerda apagar las luces cuando no las necesites.",
        "♻️ ¡No olvides reciclar el plástico, papel y vidrio!",
        "🌍 Usa productos reutilizables siempre que puedas."
    ]
    recordatorio = random.choice(recordatorios)
    await ctx.send(recordatorio)

# Función !noticias_eco
@bot.command()
async def noticias_eco(ctx):
    '''Obtiene una noticia aleatoria sobre el medio ambiente'''
    noticias = [
        "Un nuevo acuerdo global sobre la reducción de CO2 ha sido firmado.",
        "Se han plantado más de 1 millón de árboles en todo el mundo este mes.",
        "Estudios recientes muestran que el uso de energías renovables ha aumentado un 30%."
    ]
    noticia = random.choice(noticias)
    await ctx.send(f"📰 {noticia}")

bot.run("tu token aqui")