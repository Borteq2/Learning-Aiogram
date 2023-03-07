import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from random import randrange

import string
import random

load_dotenv()

TOKEN_API = os.environ.get('BOT_TOKEN')

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начать работу с ботом</em>

"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Здарова дед',
                           url='https://github.com/Borteq2')
ib2 = InlineKeyboardButton(text='Видос',
                           url='https://www.youtube.com/watch?v=5_EHfHbzUCo')
ikb.add(ib1, ib2)


async def on_startup(_):
    print('Я РОДИВСЯ')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Hello world',
                           reply_markup=ikb)


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           parse_mode='html',
                           text=HELP_COMMAND)


@dp.message_handler(commands=['description'])
async def command_description(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Кайфовый бот')



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)