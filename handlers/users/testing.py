from aiogram.dispatcher.filters import Command, Text
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import Test
from keyboards.default import menu, menu1, menu2, menu3, geolocation, menu4, rating
from aiogram.types import ReplyKeyboardRemove

from loader import dp

@dp.message_handler(Command('test'))
async def testing(message: types.Message):
    await message.answer(text='Вы начали опрос \n'
                         "Какой у вас пол/гендер?", reply_markup=menu)

    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def skintype(message: types.Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)

    await message.answer(text='Какой у вас тип кожи?', reply_markup=menu1)

    await Test.Q2.set()

@dp.message_handler(state=Test.Q2)
async def skinfeatures(message: types.Message, state: FSMContext):
    skintype = message.text
    await state.update_data(skintype=skintype)

    await message.answer(text='Какие особенности кожи у вас есть?', reply_markup=menu2)

    await Test.Q3.set()

@dp.message_handler(state=Test.Q3)
async def allergy(message: types.Message, state: FSMContext):
    skinfeatures = message.text
    await state.update_data(skinfeatures=skinfeatures)

    await message.answer(text='У вас есть аллергия на какие-то средства?', reply_markup=menu3)

    await Test.Q4.set()

@dp.message_handler(state=Test.Q4)
async def geoinfo(message: types.Message, state: FSMContext):
    allergy = message.text
    await state.update_data(allergy=allergy)

    await message.answer(text='Скиньте свою геолокацию', reply_markup=geolocation)

    await Test.Q5.set()

@dp.message_handler(state=Test.Q5)
async def searching(message: types.Message, state: FSMContext):

    await message.answer(text='Какую продукцию вы ищете?', reply_markup=menu4)

    await Test.Q6.set()


@dp.message_handler(state=Test.Q6)
async def last(message: types.Message, state: FSMContext):
    searching = message.text
    await state.update_data(searching=searching)

    data = await state.get_data()
    gender = data.get('gender')
    global skintype
    skintype = data.get('skintype')
    skinfeatures = data.get('skinfeatures')
    allergy = data.get('allergy')
    searching = data.get('searching')

    await message.answer(text = f'Ваш пол: {gender}\n\nВаш тип кожи: {skintype}\n\nОсобенности вашей кожи: {skinfeatures}\n\nПрисутствует ли аллергия: {allergy}\n\nКосметика, которую вы ищете: {searching}'
                                '\n\n\nКакую продукцию вы использовали?')

    await state.finish()

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def accept_photo(message: types.Message):
    await message.answer(text='Отлично, теперь поставьте оценку от 1-5\n\nЗатем пропишите /recommendations, чтобы посмотреть ваши рекомендации', reply_markup=rating)
