import os
import discord
from discord.ext import commands

# Configura as permissões do bot
intents = discord.Intents.default()
intents.members = True          # Permissão para ver quando alguém entra
intents.message_content = True  # Permissão para ler mensagens

bot = commands.Bot(command_name="!", intents=intents)

# Evento: Quando o bot liga e fica online
@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está online e pronto!')

# Evento: Quando alguém ENTRA no servidor
@bot.event
async def on_member_join(member):
    # Procura um canal chamado 'notificações' ou 'boas-vindas'
    channel = discord.utils.get(member.guild.text_channels, name="notificações")
    
    if channel:
        # Envia a mensagem marcando a pessoa
        await channel.send(f'Seja muito bem-vindo(a) ao Sem Emprego, {member.mention}! 🎉')

# Pega o Token secreto que vamos configurar abaixo
bot.run(os.environ['DISCORD_TOKEN'])

