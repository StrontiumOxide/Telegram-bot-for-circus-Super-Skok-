import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from pprint import pprint

import variable as v
import keyboards as kb


bot = Bot(token=v.token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):

    await message.delete()
    await bot.send_message(chat_id=message.chat.id, text=str(message.chat.id))

    if message.chat.id in v.list_admin:
        await message.answer(f"Приветcтвую вас, администратор {message.chat.first_name} {message.chat.last_name}! Выберите функцию, которой хотите воспользоваться!",
                              reply_markup=kb.kb_admin)
        
    elif message.chat.id in v.list_parts:
        await message.answer(f"Приветcтвую вас, участник {message.chat.first_name} {message.chat.last_name}! Выберите функцию, которой хотите воспользоваться!",
                              reply_markup=kb.kb_parts)

    elif message.chat.id in v.list_app:
        await message.answer(f"Приветcтвую вас, {message.chat.first_name} {message.chat.last_name}! Вы уже подали заявку! Ждите ответа администратора!")

    else:
        await message.answer(f"Приветcтвую вас, {message.chat.first_name} {message.chat.last_name}! Я Assistant circus 'Super-Skok'. У вас нет доступа!",
                            reply_markup=kb.kb_app)


@dp.callback_query(lambda callback_query: callback_query.data in ["add_app", "no_app"])
async def query_app(callback_query: CallbackQuery):

    if callback_query.data == "add_app":
        await callback_query.message.delete()
        await callback_query.message.answer(text="Напишите пожалуйста кем вы приходитесь. Пример ввода: 'Статус: Директор цирка'")
        
    elif callback_query.data == "no_app":
        await callback_query.answer(text="Всего хорошего!")


@dp.message(lambda message: "Статус:" in message.text)
async def character(message: Message):
    await message.answer("Ваши данные добавлены!")
    v.list_parts[message.chat.id] = [f"{message.chat.first_name} {message.chat.last_name}", message.text.split(maxsplit=1)[1]]
    pprint(v.list_parts)


@dp.callback_query(lambda callback_query: callback_query.data in ["event", "show_calendar"])
async def query_parts(callback_query: CallbackQuery):
    await callback_query.message.delete()

    if callback_query.data == "event":
        await callback_query.message.answer(text=f"{callback_query.message.chat.first_name}, у вас запланировано на 17.10.2023 выступление с номером 'Колесо Сира'")

    elif callback_query.data == "show_calendar":
        await callback_query.message.answer_photo(photo=v.photo_event, caption="График занятий цирка 'Супер-Скок'")


@dp.callback_query(lambda callback_query: callback_query.data in ["app_show", "app_calendar"])
async def query_admin(callback_query: CallbackQuery):
    await callback_query.message.delete()

    if callback_query.data == "app_show":
        await callback_query.answer(text="Функция не работает")

    elif callback_query.data == "app_calendar":
        await callback_query.message.answer(text="Отправьте URL фотографиb расписания с сообщением фото")

@dp.message(lambda message: "Фото:" in message.text)
async def character(message: Message):

    if message.text.split(maxsplit=1)[1] == "0":
        pass
    else:
        v.photo_event = message.text.split(maxsplit=1)[1]
        await message.answer("Расписание обновлено!")

    await message.answer_photo(photo=v.photo_event, caption="График занятий цирка 'Супер-Скок'")


@dp.message(lambda message: "admin:" in message.text)
async def add_admin(message: Message):
    v.list_admin[message.text.split(maxsplit=1)[1]] = [f"{message.chat.first_name} {message.chat.last_name}"]
    print(v.list_admin)
    await message.answer(text="Администратор добавлен!")


@dp.message()
async def echo(message: Message):
    await message.answer("Я вас не понимаю! Введите команду /start")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
