from aiogram import types
from loader import dp
from keyboards.inline.choicebuttons import choice

from aiogram.dispatcher.filters import Command

@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text='Выберите подходящую для вас опцию', reply_markup=choice)