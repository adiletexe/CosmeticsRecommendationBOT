from aiogram import Dispatcher
from loader import dp
from .privatechat import IsPrivate
# from .is_admin import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)
