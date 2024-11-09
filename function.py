from json import loads
import random
from dotenv import load_dotenv
from os import getenv
load_dotenv()
TOkEN=getenv("token")
Capteur=getenv("capteur")
def info(function):
 def analyse(*param):
  try:
   json=loads(open('config.json',"r").read())["guilds"].get(str(param[0].guild.id),"{}")
   print(json)
  except FileExistsError:
   print("config.js déplacé ou renomée")
   return
  except:
   print("config.json synthase error")
   return
  option=json.get(function.__name__)
  if  option==None:
    return
  return function(*param+(option,))
 return analyse

@info
def censure(message,json):
 print("l") 
 insultes=json.get("insulte",["merde","fdp","pute","tg","nazi"])
 if message.channel.id in json.get("channel",[]):
   return
 if message.author.id in json.get("user",[]):
   return
 print(insultes)
 print(json)
 for mot in  message.content.split(" "):
  content=mot.upper()
  for insulte in insultes:
   print(content+insulte.upper())
   if content==insulte.upper(): 
     return message.content,mot
@info
def join(member,json):
 channel=json.get("channel")
 if channel==None:
  return
 return channel,json.get("content",f"Bienvenue sur le serveur \n on espère que tu viens bien t'amuser🫵😁 ")
 
def génération(a,b):
 return random.randint(a,b)

    