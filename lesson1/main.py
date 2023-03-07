import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

import string
import random

load_dotenv()

TOKEN_API = os.environ.get('BOT_TOKEN')

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>/картинка</b> - <em>пиписька</em>
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

count = 0


async def on_startup(_):
    print('Я РОДИВСЯ')



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


# # для групп
# @dp.message_handler(commands=['help'])
# async def start_command(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text=HELP_COMMAND,
#                            parse_mode='html')
#     await message.delete()
#
#
# @dp.message_handler(commands=['картинка'])
# async def send_image(message: types.Message):
#     await bot.send_photo(chat_id=message.from_user.id,
#                         photo='https://2ch.hk/b/src/266160769/16492546145510.png')
#     await message.delete()
#
#
# @dp.message_handler(commands=['location'])
# async def send_point(message: types.Message):
#     await bot.send_location(chat_id=message.from_user.id,
#                             latitude=55,
#                             longitude=74)
#     await message.delete()


# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.answer('<em>скучное приветствие</em>', parse_mode='html')
#
#
# @dp.message_handler(content_types=['sticker'])
# async def get_sticker_id(message: types.Message):
#     await message.answer(message.sticker.file_id)
#
#
# @dp.message_handler(commands=['give'])
# async def give_command(message: types.Message):
#     # @idstickerbot
#     # await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEH-YtkAe_WYGManU_Vc5TDLUOpQpKw7wACpSAAArnlcEskT9sMLTkXCC4E')
#     await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAOFZAH8nkhd1UDiBLyYqabDLIe_jg0AAjIAAwXOwi1jNg8IvD8ecC4E')
#     await message.delete()

#
# @dp.message_handler()
# async def give_emoji(message: types.Message):
#     await message.reply(f'{message.text}' ' 🥳')

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






