from telebot import TeleBot
from telebot.types import Message, CallbackQuery
import variable as v
import keyboards as kb
import functions as func

bot = TeleBot(v.token)

    # Дефиниция команды "старт"
@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    str_chat_id = str(chat_id)

    if str(chat_id) in v.list_creators:
        text = f"""
Добрый день, Создатель - {v.list_creators[str_chat_id].name} {v.list_creators[str_chat_id].surname}!🎆

Вы можете делать, что пожелаете нужным в данном боте!☠️
Вам доступны все функции!😍
Идите же и вершите важные дела!😎
"""
        bot.send_photo(chat_id, photo=v.photo_creator, caption=text)
        menu(message)

    elif str(chat_id) in v.list_administrators:
        text = f"""

Добрый день, администратор - {v.list_administrators[str_chat_id].name} {v.list_administrators[str_chat_id].surname}!👮🏻‍♂️

Ваша основная задача поддерживать порядок в данной организации!👁
Будьте справедливы и внимательны ко всем и вся!👶🏻👧🏻🧒🏼👩🏻‍🦰
Дерзайте! Вперёд!👊🏻
"""
        bot.send_photo(chat_id, photo=v.photo_administrator, caption=text)
        menu(message)

    elif str(chat_id) in v.list_participants:
        text = f"""
Добрый день, участник - {v.list_participants[str_chat_id].name} {v.list_participants[str_chat_id].surname}!🖐

Вы являетесь участником цирка "Супер-Скок"!🎪
Вы можете пользоваться моими функциями и обращаться за помощью к руководителям!🙏🏻
Проводите время с пользой!🕔
"""
        bot.send_photo(chat_id, photo=v.photo_participiant, caption=text)
        menu(message)

    elif str(chat_id) in v.list_applications:
        text = f"""
{v.list_applications[str_chat_id].name} {v.list_applications[str_chat_id].surname}, вы уже оставили заявку!😅
Извините, но администратор ещё не проверял входящие заявки.😔
"""
        bot.send_photo(chat_id, photo=v.photo_application, caption=text)

    else:
        text = """
Добрый день, незнакомец!🥸

Я являюсь помощником участников цирка "Супер-Скок"!🎪
К сожалению, у вас нет права пользования данным ботом!😒
Если вы являетесь участником данной организации, то подайте заявку!😜
"""
        bot.send_photo(chat_id, photo=v.photo_intro, caption=text, reply_markup=kb.kb_start_ing)


# @bot.message_handler(commands=["menu"])
def menu(message: Message):
    chat_id = message.chat.id

    if str(chat_id) in v.list_creators:
        bot.send_message(chat_id, "Создатель, выберите пожалуйста функцию!🛠", 
                         reply_markup=kb.kb_administator)

    if str(chat_id) in v.list_administrators:
        bot.send_message(chat_id, "Администратор, выберите пожалуйста функцию!🛠", 
                         reply_markup=kb.kb_administator)

    if str(chat_id) in v.list_participants or chat_id in v.list_applications:
        bot.send_message(chat_id, "Участник, выберите пожалуйста функцию!🛠",
                         reply_markup=kb.kb_participiant)


@bot.callback_query_handler(lambda call: call.data in ["ing_yes", "ing_no"])
def status(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)
    if callback.data == "ing_yes":
        text = f"""
У вас действительно имя: "{callback.message.chat.first_name}" и фамилия: "{callback.message.chat.last_name}"?🧐
Если это так, то нажмите кнопку "Да". Если нет, то введите по русски имя и фамилию через пробел.🙂
(Пример: Иван Иванов).😜
"""
        bot.send_message(chat_id, text, reply_markup=kb.kb_yes_reply)
        bot.register_next_step_handler(callback.message, status_2)

    elif callback.data == "ing_no":
        bot.send_message(chat_id, "Всего хорошего!🤨")


def status_reload(message: Message):
    chat_id = message.chat.id
    text = f"""
У вас действительно имя: "{message.chat.first_name}" и фамилия: "{message.chat.last_name}"?🧐
Если это так, то нажмите кнопку "Да". Если нет, то введите имя и фамилия через пробел.🙂
(Пример: Иван Иванов).😜
"""
    bot.send_message(chat_id, text, reply_markup=kb.kb_yes_reply)
    bot.register_next_step_handler(message, status_2)


def status_2(message: Message):     
    chat_id = message.chat.id

    if message.text == "Да":
        name = message.chat.first_name
        surname = message.chat.last_name
    else:
        try: 
            name, surname= message.text.split()
        except ValueError:
            bot.send_message(chat_id, "ОШИБКА!❌\nНеправильный ввод данных!")
            status_reload(message)
            return
        except AttributeError:
            bot.send_message(chat_id, "ОШИБКА!❌\nНеправильный ввод данных!")
            status_reload(message)
            return
    text = f"""
Хорошо, {surname} {name}, информация добавлена!😁
Теперь напишите какой статус вы имеете в данной организации.👦🏼
"""
    bot.send_message(chat_id, text, reply_markup=kb.kb_remove)
    bot.register_next_step_handler(message, status_3, name, surname)
    

def status_3(message: Message, name: str, surname: str):
    chat_id = message.chat.id
    text = f"""
Информация добавлена и сохранена!👍
Ждите ответа администратора!🤡
/start
"""
    
    user_dict = {
            "user_id": str(chat_id),
            "t_name": message.chat.first_name,
            "t_surname": message.chat.last_name,
            "name": name,
            "surname": surname,
            "status": "Заявка",
            "role": message.text
        }

    func.update_info(user_dict)

    text_app = f"Новая заявка от пользователя {name} {surname}!😅\n Скорее обновите данные!😎"
    for list_manager in [v.list_administrators, v.list_creators]:
        for user_id in list_manager:
            bot.send_message(user_id, text=text_app)

    bot.send_message(chat_id, text)
    

@bot.callback_query_handler(lambda call: call.data in ["my_show", "show_calendar", "send_letter_admin", "order_sertificate", "documente"])
def def_participiant(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)
    if callback.data == "my_show":
        bot.send_message(chat_id, "У вас нет запланированных мероприятияй❌", reply_markup=kb.kb_back)

    elif callback.data == "show_calendar":
        bot.send_photo(chat_id, photo=v.photo_calendar, caption="Расписание на месяц💬", reply_markup=kb.kb_back)

    elif callback.data == "send_letter_admin":
        bot.send_message(chat_id, "Данная функция в разработке❌", reply_markup=kb.kb_back)

    elif callback.data == "order_sertificate":
        bot.send_message(chat_id, "Данная функция в разработке❌", reply_markup=kb.kb_back)

    elif callback.data == "documente":

        text = f"""
Документ в формате pptx📄

В данном файле находится руководство по использованию данного бота📑

Прочитайте внимательно❗️
"""
        try:
            with open(file="files/documente.pptx", mode='rb') as f:
                file_info = f.read()
        except Exception:
            bot.send_message(chat_id, "Извините, файл не найден или администратор его не выложил❌", 
                             reply_markup=kb.kb_back)
        else:
            bot.send_document(chat_id=chat_id, document=file_info, caption=text, 
                              visible_file_name="Документация.pptx", reply_markup=kb.kb_back)
    

@bot.callback_query_handler(lambda call: call.data == "back")
def back(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)
    menu(callback.message)
    

@bot.callback_query_handler(lambda call: call.data in ["speech", "calendar", "mail", "data", "role"])
def def_administration(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)
    if callback.data == "speech":
        bot.send_message(chat_id, "Выберите, что вы хотите сделать💭", reply_markup=kb.kb_administator_speech)

    elif callback.data == "calendar":
        bot.send_message(chat_id, "Выберите, что вы хотите сделать💭", reply_markup=kb.kb_administator_calendar)

    elif callback.data == "mail":
        bot.send_message(chat_id, "Данная функция в разработке❌", reply_markup=kb.kb_back)

    elif callback.data == "data":
        bot.send_message(chat_id, "Выберите что вы хотите сделать с данными🛠", reply_markup=kb.kb_data)

    elif callback.data == "role":
        status, role = func.role(chat_id)
        text = f"""
Ваш статус: {status}😎
Ваша роль: {role}🤩
"""
        bot.send_message(chat_id, text, reply_markup=kb.kb_back)


@bot.callback_query_handler(lambda call: call.data in ["loading", "download", "statistics"])
def data_func(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)

    if callback.data == "loading":
        text = f"""
Загрузите файл в формате csv📊
Имя файла должно называться "Список пользователей.csv"
"""
        bot.send_message(chat_id, text)
        bot.register_next_step_handler(callback.message, loading_doc)

    elif callback.data == "download":
        text = f"""
Документ в формате csv. Можно открыть в Excel📊

В данном файле содержится информация о всех пользователях данного Телеграм бота📑

Неизменяйте имя файла при обратной загрузке!❌
"""

        with open(file="files/Список пользователей.csv", mode="rb") as f:
            file_info = f.read()

        bot.send_document(chat_id, document=file_info, caption=text,
                          visible_file_name="Список пользователей.csv", reply_markup=kb.kb_back)
        
    elif callback.data == "statistics":
        text = f"""
⚪️ Количество заявок: {len(v.list_applications)}
🟡 Количество участников: {len(v.list_participants)}
🔴 Количество администраторов: {len(v.list_administrators)}
⚫️ Количество создателей: {len(v.list_creators)}
"""
        bot.send_message(chat_id, text, reply_markup=kb.kb_back)


def loading_doc(message: Message):
    chat_id = message.chat.id
    
    if message.document == None:
        bot.send_message(chat_id, "Ваше сообщение не содержит файл!❌")

    else:

        if message.document.file_name != "Список пользователей.csv":
            bot.send_message(chat_id, "Неверное имя файла!❌")

        else:

            file_path = bot.get_file(message.document.file_id).file_path
            dowload_file = bot.download_file(file_path)

            with open("files/Список пользователей.csv", mode="wb") as f:
                f.write(dowload_file)

            func.starting_loads()

            bot.send_message(chat_id, "Данные обновлены!☑️")

    menu(message)


@bot.callback_query_handler(lambda call: call.data in ["set_show", "set_calendar"])
def def_administration_2(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    bot.delete_message(chat_id, callback.message.message_id)

    if callback.data == "set_show":
        bot.send_message(chat_id, "Данная функция не доступна❌", reply_markup=kb.kb_back)

    elif callback.data == "set_calendar":
        bot.send_message(chat_id, "Загрузите пожалуйста фотографию расписания📷")
        bot.register_next_step_handler(callback.message, def_photo)


def def_photo(message: Message):
    chat_id = message.chat.id

    try:
        message.photo[0].file_id
    except TypeError:
        bot.send_message(chat_id, "Ошибка! Расписание не обновлено!❌")
    else:
        v.photo_calendar = message.photo[0].file_id
        bot.send_message(chat_id, "Расписание обновлено!☑️")

    menu(message)


@bot.message_handler(content_types=["text"])
def echo(message: Message):
    bot.send_message(message.chat.id, "Я вас не понимаю!❌\nВведите команду /start")


bot.polling(non_stop=True)
