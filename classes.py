class Participant:
    def __init__(self, user_id, name, surname, status):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.status = status

    def __str__(self) -> str:
        return self.user_id

class Worker(Participant):
    pass

class Administrator(Worker):
    pass

class Creator(Administrator):
    pass

