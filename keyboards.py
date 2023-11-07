from telebot.types import (
    ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton,
    InlineKeyboardButton, InlineKeyboardMarkup
)

kb_start_ing = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton("Подать заявку😎", callback_data="ing_yes")
        ],
        [
            InlineKeyboardButton("Отказаться😡", callback_data="ing_no")
        ]
    ]
)



kb_back = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton("Вернуться в главное меню🖥", callback_data="back")
        ]
    ]
)


kb_participiant = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton("Мои выступления🧙🏻‍♂️", callback_data="my_show"),
            InlineKeyboardButton("График занятий🌄", callback_data="show_calendar")
        ],
        [
            InlineKeyboardButton("Написать администраторам✉️", callback_data="send_letter_admin"),
            InlineKeyboardButton("Заказать справку📨", callback_data="order_sertificate")
        ],
        [
            InlineKeyboardButton("Поделиться❤️", switch_inline_query="- перейдите по ссылке")
        ]
    ]
)


kb_administator = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton("Выступления🏟", callback_data="speech"),
            InlineKeyboardButton("График занятий🌄", callback_data="calendar")
        ],
        [
            InlineKeyboardButton("Почта✉️", callback_data="mail")
        ],
        [
            InlineKeyboardButton("Поделиться❤️", switch_inline_query="- перейдите по ссылке")
        ]
    ]
)

kb_administator_speech = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton("Мои выступления🏟", callback_data="my_show"),
            InlineKeyboardButton("Назначить выступления🛠", callback_data="set_show")
        ]
    ]
)

kb_administator_calendar = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton("Календарь🌄", callback_data="show_calendar"),
            InlineKeyboardButton("Изменить график🛠", callback_data="set_calendar")
        ]
    ]
)
