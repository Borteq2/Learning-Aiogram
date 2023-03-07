import os
import string
import random

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from random import randrange


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='github',
                           url='https://github.com/Borteq2')
ib2 = InlineKeyboardButton(text='this repo',
                           url='https://github.com/Borteq2/Learning-Aiogram')

ikb.add(ib1).add(ib2)  # column
# ikb.add(ib1, ib2)  # single row


kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
b = KeyboardButton(text='/links')
kb.add(b)