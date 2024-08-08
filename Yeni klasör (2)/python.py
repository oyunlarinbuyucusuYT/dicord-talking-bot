import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send("Selam!")
    elif message.content.starswith('adın ne'):
        await message.channel.send('ben sayhan memnun oldum!')
    elif message.content.starswith('5x5?'):
        await message.channel.send('25')
    elif message.content.starswith('tezgah lan bu'):
        await message.channel.send('TEZGAN LAN')
    elif message.content.starswith('roblox kapatıldı :('):
        await message.channel.send('bilimsel olarak eğer roblox açılmazsa türkiye bombalanacak')
    elif message.content.starswith('sa'):
        await message.channel.send('as')
    else:
        message.channel.send('herşeye cevap vermiyorum beynim yerinde değil')

bot.run("MTI3MTE0ODY3NTA0NDg3MjM3NQ.Go8qtN.hqh_bNKKeHldZPKXwG42A97xwiI9IeUmwc8F3U")