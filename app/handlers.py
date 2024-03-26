from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

from config import vids, mids, valids

router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет!\n\n\n Я Бот-Гриборий.\n\n\n Ты выбираешь человека - я кидаю рандомный мем с ним',
                         reply_markup=kb.main)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

@router.message(F.text== 'Как дела?')
async def gow_ay(message: Message):
    await message.reply('Нормально')

@router.message(F.photo)
async def ph(message: Message):
    await message.answer((f'"{message.photo[-1].file_id}"'))

@router.message(Command('get_jama'))
async def get_jama(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAN0ZgHG1r7J6RL3JgoXOdToye56fpEAAsPWMRtcj-FI8mLX0s1bIG8BAAMCAAN5AAM0BA',
                               caption='Это жямщка')

@router.message(F.text== 'Валод')
async def get_val(message: Message):
    await message.answer_photo(photo=vids,
                               caption='Хочешь еще?\n\n\n Жми на кнопки меню')

@router.message(F.text== 'Мартин')
async def get_val(message: Message):
    await message.answer_photo(photo=mids,
                               caption='Хочешь еще?\n\n\n Жми на кнопки меню')

@router.message(F.text== 'Валера')
async def get_val(message: Message):
    await message.answer_photo(photo=valids,
                               caption='Хочешь еще?\n\n\n Жми на кнопки меню')

@router.callback_query(F.data=='catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Отлично! Теперь выбери своего кента!', show_alert=True)
    await callback.message.edit_text("Выбери своего кента...", reply_markup=await kb.inline_frs())







@router.message(Command('reg'))
async def reg_one(message: Message, state:FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя')

@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона')

@router.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершена. \nИмя: {data["name"]}\nНомер: {data["number"]}')
    await state.clear()
