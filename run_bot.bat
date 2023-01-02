@echo off

call %~dp0BotTelegram\venv\Scripts\activate

cd %~dp0BotTelegram

set TOKEN=5643252941:AAHoV2xY3TMMJkQtPqu04U508ATpKhwTdqE

python telebot.py

pause