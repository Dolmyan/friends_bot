from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог кентов', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='basket'),
     InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])

settings=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube',
                          url='https://www.youtube.com/watch?v=V3QBdkaH6GM&t=5s')]])

frs = ['Жяма', 'Валод', 'Мартини']

async def inline_frs():
    keyboard=InlineKeyboardBuilder()
    for i in frs:
        keyboard.add(InlineKeyboardButton(text=i,
                     url='https://www.youtube.com/watch?v=V3QBdkaH6GM&t=5s'))
    return keyboard.adjust(2).as_markup()