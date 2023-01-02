from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqllite_db

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Bon appetit', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Communication with the bot through private messages, write to him:\nhttps://t.me/Pizza_HerrBot')

# @dp.message_handler(commands=['Working_mode'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Mo-Th from 9:00 to 20:00, Fr-Sa from 10:00 to 23:00')

# @dp.message_handler(commands=['Location'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'st. Rockefeller Center, Midtown Manhattan', reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['Menu'])
async def pizza_menu_command(message: types.Message):
    await sqllite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Working_mode'])
    dp.register_message_handler(pizza_place_command, commands=['Location'])
    dp.register_message_handler(pizza_menu_command, commands=['Menu'])