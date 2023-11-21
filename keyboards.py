from telebot.types import (
    ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton,
    InlineKeyboardButton, InlineKeyboardMarkup
)

kb_yes_reply = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Да")
)

kb_back_reply = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Отмена❌")
)

kb_remove = ReplyKeyboardRemove()

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
            InlineKeyboardButton("Почта✉️", callback_data="send_letter_admin"),
            InlineKeyboardButton("Заказать справку📨", callback_data="order_sertificate")
        ],
        [
            InlineKeyboardButton("Документация📄", callback_data="documente"),
            InlineKeyboardButton("Ваш статус🫵🏻", callback_data="role")
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
            InlineKeyboardButton("Почта✉️", callback_data="mail"),
            InlineKeyboardButton("Документация📄", callback_data="documente")
        ],
        [
            InlineKeyboardButton("Данные💭", callback_data="data"),
            InlineKeyboardButton("Ваш статус🫵🏻", callback_data="role")
        ],
        [
            InlineKeyboardButton("Поделиться❤️", switch_inline_query='- Телеграм бот цирка "Супер-Скок"🎪')
        ]
    ]
)

kb_administator_speech = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton("Мои выступления🏟", callback_data="my_show"),
            InlineKeyboardButton("Назначить выступления🛠", callback_data="set_show"),
        ],
        [
            InlineKeyboardButton("Вернуться в главное меню🖥", callback_data="back")
        ]
    ]
)

kb_administator_calendar = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton("Календарь🌄", callback_data="show_calendar"),
            InlineKeyboardButton("Изменить график🛠", callback_data="set_calendar")
        ],
        [
            InlineKeyboardButton("Вернуться в главное меню🖥", callback_data="back")
        ]
    ]
)

kb_data = InlineKeyboardMarkup(
    keyboard= [
        [
            InlineKeyboardButton("Статистика📈", callback_data="statistics")
        ],
        [
            InlineKeyboardButton("Загрузить данные⬆️", callback_data="loading"),
            InlineKeyboardButton("Скачать данные⬇️", callback_data="download")
        ],
        [
            InlineKeyboardButton("Вернуться в главное меню🖥", callback_data="back")
        ]
    ]
)
