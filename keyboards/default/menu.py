from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мужской')
        ],
        [
            KeyboardButton(text='Женский')
        ],
    ],
    resize_keyboard=True
)

menu1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Сухой'),
            KeyboardButton(text='Жирный')
        ],
        [
            KeyboardButton(text='Комбинированный'),
            KeyboardButton(text='Нормальный')
        ],
    ],
    resize_keyboard=True
)

menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пигментация'),
            KeyboardButton(text='Пятна')
        ],
        [
            KeyboardButton(text='Веснушки'),
            KeyboardButton(text='Акне')
        ],
    ],
    resize_keyboard=True
)

menu3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
        ],
        [
            KeyboardButton(text='Нет'),
        ],
    ],
    resize_keyboard=True
)

geolocation = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отправить свою геолокацию', request_location=True))

menu4 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Маска для лица'),
        ],
        [
            KeyboardButton(text='Крем для лица')
        ],
    ],
    resize_keyboard=True
)
rating = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='5')
        ],
    ],
    resize_keyboard=True
)