from aiogram import types
from random import randint
from loader import dp
from ..users.testing import skintype


@dp.message_handler(text='/recommendations')
async def rec(message: types.Message):
    chat_id = message.from_user.id
    number = randint(1, 5)
    if number == 1:
        photo_url = 'https://shop.japonica.ru/upload/iblock/0ee/0eea30a60c79068dcaefc2b67eda9a6d.jpg'
        caption = 'Крем для вашего типа кожи\n\n Средняя оценка которую дали люди с вашим типом кожи - 4 \n\nМожно приобрести по ссылке: ...здесь будет ссылка...'
    elif number == 2:
        photo_url = 'https://www.cosmeticsbulgaria.com/uploads/products/279/bigThumbs/anti-age-sun-protection-cream-spf-50-bodi-beauty.jpg'
        caption = 'Крем для вашего типа кожи\n\n Средняя оценка которую дали люди с вашим типом кожи - 4 \n\nМожно приобрести по ссылке: ...здесь будет ссылка...'
    elif number == 3:
        photo_url = 'https://images.ctfassets.net/9a1evglma7uu/63I2goIGJwoA4MvYiK51Nh/f5829cd8f19a0f2ebbc1ee9b8ab95320/SPF50-Creme-Solaire-Visage-ANTI-AGE-50.png'
        caption = 'Крем для вашего типа кожи\n\n Средняя оценка которую дали люди с вашим типом кожи - 4 \n\nМожно приобрести по ссылке: ...здесь будет ссылка...'
    elif number == 4:
        photo_url = 'https://object.pscloud.io/cms/cms/Photo/img_0_2156_20_0.jpeg'
        caption = 'Крем для вашего типа кожи\n\n Средняя оценка которую дали люди с вашим типом кожи - 4 \n\nМожно приобрести по ссылке: ...здесь будет ссылка...'
    else:
        photo_url = 'https://shop.japonica.ru/upload/iblock/0ee/0eea30a60c79068dcaefc2b67eda9a6d.jpg'
        caption = 'Крем для вашего типа кожи\n\n Средняя оценка которую дали люди с вашим типом кожи - 4 \n\nМожно приобрести по ссылке: ...здесь будет ссылка...'
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=caption)
