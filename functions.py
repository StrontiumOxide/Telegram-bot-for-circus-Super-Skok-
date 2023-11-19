import variable as v
import csv
from pprint import pprint
from classes import Application, Participant, Worker, Administrator, Creator
from telebot.types import Message, CallbackQuery

    # Должностной сепаратор
def starting_loads() -> None:
    """
    Должностной сепаратор.

    Данная функция производит перегрузку переменных, в которых
    содержатся экземпляры классов в соотвествующих ключах.

    Данные в программе хранятся в виде словарей. Ключами являются 
    id-пользователей, а значениям экземпляры классов 
    """

    v.list_creators = {}
    v.list_administrators = {}
    v.list_participants = {}
    v.list_applications = {}
    
    with open(file="files/list_user.csv", mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")

        for user in reader:

            if user["status"] == "Заявка":
                v.list_applications[user["user_id"]] = Application(
                    user_id=user["user_id"],
                    t_name=user["t_name"],
                    t_surname=user["t_surname"],
                    name=user["name"],
                    surname=user["surname"],
                    status=user["status"],
                    role=user["role"]
                )

            elif user["status"] == "Участник":
                v.list_participants[user["user_id"]] = Participant(
                    user_id=user["user_id"],
                    t_name=user["t_name"],
                    t_surname=user["t_surname"],
                    name=user["name"],
                    surname=user["surname"],
                    status=user["status"],
                    role=user["role"]
                )

            elif user["status"] == "Администратор":

                v.list_administrators[user["user_id"]] = Administrator(
                    user_id=user["user_id"],
                    t_name=user["t_name"],
                    t_surname=user["t_surname"],
                    name=user["name"],
                    surname=user["surname"],
                    status=user["status"],
                    role=user["role"]
                )

            elif user["status"] == "Создатель":

                v.list_creators[user["user_id"]] = Creator(
                    user_id=user["user_id"],
                    t_name=user["t_name"],
                    t_surname=user["t_surname"],
                    name=user["name"],
                    surname=user["surname"],
                    status=user["status"],
                    role=user["role"]
                )


def update_info(user_dict: dict) -> None:
    """
    Читатель из файла.

    Данная функция добавляет информация в CSV-файл.
    Далее информация обновляется в должностном сепараторе.
    """

    fields = ["user_id", "t_name", "t_surname", "name", "surname", "status", "role"]
    with open(file="files/list_user.csv", mode="a", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fields, delimiter=";")
        writer.writerows([user_dict])

    starting_loads()


def role(message: Message) -> str:
    """
    Дефиниция статуса.

    Данная функция среди всех словарей ищет информацию
    о пользователе и возвращает его статус и роль.
    """

    chat_id = str(message.chat.id)

    for list_post in [v.list_creators, v.list_administrators, v.list_participants]:
        for user in list_post.values():
            if user.user_id == chat_id:
                return user.status, user.role

    # Должностной сепаратор запускается при первом запуске программы.
    # Для следующих обновлений, пользователей из классов руководства
    # должен нажать кнопку "Обновить данные"
starting_loads()
print(
    v.list_applications,
    v.list_participants,
    v.list_administrators,
    v.list_creators,
    sep="\n"
)
