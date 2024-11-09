@echo off
set /P input="Installation ? init/file : "
if %input%== init call :init 
if %input%== file call :fichier
echo Lancement bot 
pause
py ./bot.py

:init
 py -m pip install --upgrade pip
 py -m pip install --upgrade python-dotenv
 py -m  pip install --upgrade discord.py
 call :fichier
:fichier
 set /p token="Token: "
 echo fichier .env add
 echo token="%token%">.env
 echo fichier config.json add
 echo {"user":{},"guilds":{}}>config.json
 


 