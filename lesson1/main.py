import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()

TOKEN_API = os.environ.get('BOT_TOKEN')

HELP_COMMAND = \
    """
    /help - список команд
/start - начать работу с ботом
    """

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='Приветствую')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)

