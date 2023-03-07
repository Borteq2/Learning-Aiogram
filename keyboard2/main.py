import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from random import randrange

import string
import random

load_dotenv()

TOKEN_API = os.environ.get('BOT_TOKEN')

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>/random</b> - <em>рандомный геотег</em>
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help')).insert(KeyboardButton('/description'))



async def on_startup(_):
    print('Я РОДИВСЯ')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Здарова дед',
                           reply_markup=kb)


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           parse_mode='html',
                           text=HELP_COMMAND)


@dp.message_handler(commands=['description'])
async def command_description(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Кайфовый бот')


@dp.message_handler(commands=['random'])
async def command_randplace(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            longitude=random.randrange(1, 100),
                            latitude=random.randrange(1, 100))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
