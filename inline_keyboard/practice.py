import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from random import randrange

import string
import random

from keyboards import kb, ikb


load_dotenv()

TOKEN_API = os.environ.get('BOT_TOKEN')

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начать работу с ботом</em>

"""


async def on_startup(_):
    print('Я РОДИВСЯ')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Здарова дед',
                         reply_markup=kb)


@dp.message_handler(commands=['links'])
async def links_commands(message: types.Message):
    await message.answer(text='Выберите опцию',
                         reply_markup=ikb)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
