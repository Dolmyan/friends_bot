from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main= ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Валод'),KeyboardButton(text='Мартин')],
    [KeyboardButton(text='Валера')]
], resize_keyboard=True,
input_field_placeholder='Выбери кента')

