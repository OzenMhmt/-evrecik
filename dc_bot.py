import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

# bot-yardım

@bot.command()
async def yardım(ctx):
    await ctx.send(f'GeriDönüşüm Yazarak bilgi alabilirsin: !GeriDönüşüm')
    await ctx.send(f'Merhaba yazarak bottan selam alabilirsin:  !merhaba')

# bot-merhaba

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhabana Merhaba Kardeeeş') 

# bot-katılım

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

# bot-GeriDönüşüm

@bot.command()
async def GeriDönüşüm(ctx):
    with open('images\Geri_d kutulari.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    await ctx.send(f'Yukarida bulunan kutular ile sende geri dönüşüm yaparak evinde oluşan atiklari kirliliğe dönüştürmezsin!!!')


















# bot-token

bot.run("")







