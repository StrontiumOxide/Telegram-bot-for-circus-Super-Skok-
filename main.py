from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from variable import token, photo_calendar, photo_intro, photo_participiant, photo_creator, photo_administrator, list_creator, list_admin, list_app, list_parts
from classes import Participant, Worker, Administrator, Creator
import keyboards as kb

list_admin.append(Administrator(user_id=1172020269, name="Денис", surname="Дорофеев", status="Творец"))
list_creator.append(Creator(user_id=1172020269, name="Денис", surname="Дорофеев", status="Творец"))

# list_admin.append(Administrator(user_id=1102575118, name="Сергей", surname="Зорин", status="Творец"))
# list_creator.append(Creator(user_id=1102575118, name="Сергей", surname="Зорин", status="Творец"))

bot = TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id

    variable = list(map(lambda x: x.user_id, list_creator))
    if chat_id in variable:
        text = f"""
Добрый день, Создатель - {message.chat.first_name} {message.chat.last_name}!🎆
Вы можете делать, что пожелаете нужным в данном боте!☠️
Вам доступны все функции!😍
Идите же и вершите важные дела!😎
"""
        bot.send_photo(chat_id, photo=photo_creator, caption=text)
        menu(message)
        return

    variable = list(map(lambda x: x.user_id, list_admin))
    if chat_id in variable:
        text = f"""
Добрый день, администратор - {message.chat.first_name} {message.chat.last_name}!👮🏻‍♂️
Ваша основная задача поддерживать порядок в данной организации!👁
Будьте справедливы и внимательны ко всем и вся!👶🏻👧🏻🧒🏼👩🏻‍🦰
Дерзайте! Вперёд!👊🏻
"""
        bot.send_photo(chat_id, photo=photo_administrator, caption=text)
        menu(message)
        return

    variable = list(map(lambda x: x.user_id, list_parts))
    if chat_id in variable:
        text = f"""
Добрый день, участник - {message.chat.first_name} {message.chat.last_name}!🖐
Вы являетесь участником цирка "Супер-Скок"!🎪
Вы можете пользоваться моими функциями и обращаться за помощью к руководителям!🙏🏻
Проводите время с пользой!🕔
"""
        bot.send_photo(chat_id, photo=photo_participiant, caption=text)
        menu(message)
        return

    else:
        text = """
Добрый день, незнакомец!🥸
Я являюсь помощником участников цирка "Супер-Скок"!🎪
К сожалению, у вас нет права пользования данным ботом!😒
Если вы являетесь участником данной организации, то подайте заявку!😜
"""
        bot.send_photo(chat_id, photo=photo_intro, caption=text, reply_markup=kb.kb_start_ing)


# @bot.message_handler(commands=["menu"])
def menu(message: Message):
    chat_id = message.chat.id

    variable = list(map(lambda x: x.user_id, list_creator))
    if chat_id in variable:
        bot.send_message(chat_id, "Создатель, выберите пожалуйста функцию!🛠", reply_markup=kb.kb_administator)
        return

    variable = list(map(lambda x: x.user_id, list_admin))
    if chat_id in variable:
        bot.send_message(chat_id, "Администратор, выберите пожалуйста функцию!🛠", reply_markup=kb.kb_administator)
        return

    variable = list(map(lambda x: x.user_id, list_parts))
    if chat_id in variable:
        bot.send_message(chat_id, "Участник, выберите пожалуйста функцию!🛠",
                         reply_markup=kb.kb_participiant)
        return


@bot.callback_query_handler(lambda call: call.data in ["ing_yes", "ing_no"])
def status(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)
    if callback.data == "ing_yes":
        text = f"""
Уважаемый {callback.message.chat.first_name} {callback.message.chat.last_name}, напишите пожалуйста, какая у вас роль в данной организации!😈
"""
        bot.send_message(chat_id, text)
        bot.register_next_step_handler(callback.message, status_2)

    elif callback.data == "ing_no":
        bot.send_message(chat_id, "Всего хорошего!🤨")


def status_2(message: Message):     
    chat_id = message.chat.id
    bot.send_message(chat_id, "Хорошо, информация добавлена. /start")
    list_parts.append(Participant(
        user_id=chat_id,
        name=message.chat.first_name,
        surname=message.chat.last_name,
        status=message.text))


@bot.callback_query_handler(lambda call: call.data in ["my_show", "show_calendar", "send_letter_admin", "order_sertificate"])
def def_participiant(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)
    if callback.data == "my_show":
        bot.send_message(chat_id, "У вас нет запланированных мероприятияй", reply_markup=kb.kb_back)

    elif callback.data == "show_calendar":
        bot.send_photo(chat_id, photo=photo_calendar, caption="Расписание на месяц", reply_markup=kb.kb_back)

    elif callback.data == "send_letter_admin":
        bot.send_message(chat_id, "Данная функция в разработке", reply_markup=kb.kb_back)

    elif callback.data == "order_sertificate":
        bot.send_message(chat_id, "Данная функция в разработке", reply_markup=kb.kb_back)
    

@bot.callback_query_handler(lambda call: call.data == "back")
def back(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)
    menu(callback.message)
    

@bot.callback_query_handler(lambda call: call.data in ["speech", "calendar", "mail"])
def def_administration(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)
    if callback.data == "speech":
        bot.send_message(chat_id, "Выберите, что вы хотите сделать", reply_markup=kb.kb_administator_speech)

    elif callback.data == "calendar":
        bot.send_message(chat_id, "Выберите, что вы хотите сделать", reply_markup=kb.kb_administator_calendar)

    elif callback.data == "mail":
        bot.send_message(chat_id, "Данная функция в разработке", reply_markup=kb.kb_back)


@bot.callback_query_handler(lambda call: call.data in ["set_show", "set_calendar"])
def def_administration_2(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)
    if callback.data == "set_show":
        bot.send_message(chat_id, "Данная функция не доступна", reply_markup=kb.kb_back)

    elif callback.data == "set_calendar":
        bot.send_message(chat_id, "Загрузите пожалуйста фотографию расписания📷", reply_markup=kb.kb_back)
        bot.register_next_step_handler(callback.message, def_photo)


def def_photo(message: Message):
    chat_id = message.chat.id
    try:
        message.photo[0].file_id
    except TypeError:
        bot.send_message(chat_id, "Ошибка! Расписание не обновлено!", reply_markup=kb.kb_back)
    else:
        global photo_calendar
        photo_calendar = message.photo[0].file_id
        bot.send_message(chat_id, "Расписание обновлено!", reply_markup=kb.kb_back)


@bot.message_handler(content_types=["text"])
def echo(message: Message):
    bot.send_message(message.chat.id, "Я вас не понимаю! /start")


bot.polling(non_stop=True)
