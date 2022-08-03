from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=
                              [
                                  [
                                      InlineKeyboardButton(text='Kiss an ass', callback_data='buy:apple:5')
                                  ],
                                  [
                                      InlineKeyboardButton(text='Exit', callback_data='cancel')
                                  ],
                              ])

BUY_LINK = 'https://botfather.dev/dashboard/lessons/6-2-inlajn-knopki'
buy_link = InlineKeyboardButton(text='click here', url=BUY_LINK)
choice.insert(buy_link)