class User:
    def __init__(self, user_id: int, t_name: str, t_surname: str, name: str, surname: str, status: str, role: str) -> None:
        self.user_id = user_id # id пользователя
        self.t_name = t_name # имя в телеграме
        self.t_surname = t_surname # фамилия в телеграме
        self.name = name # реальное имя
        self.surname = surname # реальная фамилия
        self.status = status # занимаемая должность
        self.role = role # сфера деятельности

    def __dict__(self) -> dict:
        return {
            "user_id": self.user_id,
            "t_name": self.t_name,
            "t_surname": self.t_surname,
            "name": self.name,
            "surname": self.surname,
            "status": self.status,
            "role": self.role
        }

    def __str__(self) -> str:
        return (f"id-пользователя: {self.user_id}\n"
                f"Имя в Телеграм: {self.t_name}\n" 
                f"Имя в Телеграм: {self.t_surname}\n" 
                f"Реальное имя: {self.name}\n" 
                f"Реальная фамилия: {self.surname}\n" 
                f"Статус: {self.status}\n"
                f"Роль: {self.role}") 

class BlackList(User):
    pass

class Application(User):
    pass

class Participant(User):
    pass
    
class Worker(User):
    pass

class Administrator(User):
    pass

class Creator(User):
    pass

