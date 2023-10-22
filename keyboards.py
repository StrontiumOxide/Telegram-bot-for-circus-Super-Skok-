from aiogram.types import (
    ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)

    # Keyboard for administrations
kb_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Просмотр заявок", callback_data="app_show")
        ],
        [
            InlineKeyboardButton(text="Изменить график занятий", callback_data="app_calendar")
        ]
    ]
)

    # Keyboard for participiant
kb_parts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Мероприятия", callback_data="event")
        ],
        [
            InlineKeyboardButton(text="График занятий", callback_data="show_calendar")
        ]
    ]
)

    # Keyboard for applications
kb_app = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подать заявку", callback_data="add_app")
        ],
        [
            InlineKeyboardButton(text="Я не хочу", callback_data="no_app")
        ]
    ]
)
