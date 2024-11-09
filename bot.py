import function
import discord
from discord.ext import commands
nombre=0
intent=discord.Intents.all()
intent.message_content=True
intent.members=True

bot=commands.Bot(command_prefix=function.Capteur,intents=intent)


@bot.event
async def on_ready():
    global sync
    sync=await bot.tree.sync()
    print(len(sync))
    print(f"Name :{bot.user.name} Id:{bot.user.id} ")
    await bot.get_channel(1304543135891984424).send(f"{bot.user.mention} débarque 😎🫵")
@bot.event
async def on_message(message):
   global nombre
   if message.author.id==bot.user.id:
      return
   nombre+=1
   scan=function.censure(message)
   if scan:
      await bot.get_channel(message.channel.id).send(f"{scan[1]} dit par {message.author.mention} : {message.content}")
      return
   await bot.process_commands(message)
@bot.event
async def on_member_join(member):

   résultat=function.join(member)
   if not résultat:
      return
   channel=bot.get_channel(résultat[0])
   await channel.send(member.mention)
   await channel.send(résultat[1])
   await channel.send(member.display_avatar)
   await member.send(f"Bienvenue sur le serveur {member.guild}\n n'hésite pas à poser des questions 😎")
   


@bot.command(name="test")
async def test(ctx,*arg):
   await ctx.send(arg)
@bot.command(name="info")
async def count(ctx):
      await ctx.send(f"messages envoyés :{nombre} \n commande slash : {len(sync)}")
@bot.command(name="calcul")
async def calcul(ctx,arg):
  for i in arg:
     if i not in ["0","1","2","3","4","5","6","7","8","9","*","+","-","/","(",")"]:
        await ctx.send(f"{ctx.author.mention} caractère non valide 😱")
        return
  try:
   résultat=eval(arg)
   await ctx.send(f"{ctx.author.mention} résultat de {arg} est >>>>")
   await ctx.send(f"{résultat} 📜🤓")
  except:
      await ctx.send(f"{ctx.author.mention} erreur calcul {arg} impossible")



bot.run(function.TOkEN)

