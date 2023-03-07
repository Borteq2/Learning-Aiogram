import os
import string
import random

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from random import randrange

load_dotenv()

TOKEN_API = os.environ.get('BOT_TOKEN')

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начать работу с ботом</em>

"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=False)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/vote')
kb.add(b1, b2)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Здарова дед',
                           reply_markup=kb)

@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):

    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='Кайф ежжи ♥️',
                               callback_data='like')
    ib2 = InlineKeyboardButton(text='кг/ам 💩',
                               callback_data='dislike')
    ikb.add(ib1, ib2)

    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://klike.net/uploads/posts/2020-04/1587719791_1.jpg',
                         caption='Ништяк?',
                         reply_markup=ikb)


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='Ага попався звездолюб')  # если б был message.answer то надо было бы перед await ставить return
    await callback.answer(text='Фу быдло')


async def on_startup(_):
    print('Я РОДИВСЯ')





if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)

