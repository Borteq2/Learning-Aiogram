import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

import string
import random

load_dotenv()

TOKEN_API = os.environ.get('BOT_TOKEN')

HELP_COMMAND = \
    """
    /help - список команд
/start - начать работу с ботом
    """

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

count = 0


async def on_startup(_):
    print('Я РОДИВСЯ')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<em>скучное приветствие</em>', parse_mode='html')


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    # @idstickerbot
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEH-YtkAe_WYGManU_Vc5TDLUOpQpKw7wACpSAAArnlcEskT9sMLTkXCC4E')
    await message.delete()


@dp.message_handler()
async def give_emoji(message: types.Message):
    await message.reply(f'{message.text}' ' 🥳')

# @dp.message_handler(commands=['description'])
# async def description_command(message: types.Message):
#     await message.answer('Хороший бот, красивый, мощный')
#     await message.delete()


# @dp.message_handler(commands=['count'])
# async def check_count(message: types.Message):
#     global count
#     await message.answer(f'This button was pressed {count} time/s')
#     count += 1




# @dp.message_handler()
# async def send_check_zero(message: types.Message):
#     if '0' in message.text:
#         return await message.answer('YES')
#     await message.reply('NO')


# @dp.message_handler(commands=['help'])
# async def help_command(message: types.Message):
#     await message.reply(text=HELP_COMMAND)
#
#
# @dp.message_handler(commands=['start'])
# async def help_command(message: types.Message):
#     await message.answer(text='Приветствую')
#     await message.delete()
#
#
# @dp.message_handler()  # ASCII
# async def send_random_message(message: types.Message):
#     await message.reply(random.choice(string.ascii_letters))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

