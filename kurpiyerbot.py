import discord
from discord.ext import commands
import rulett

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def rulet(ctx,renk: str,sayi: int ,tc: int,rd: int,to: int,bet: int ):
    await ctx.send(rulett.rulet(renk,sayi,tc,rd,to,bet))

bot.run("")
