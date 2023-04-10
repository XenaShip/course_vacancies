from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def add_vacancy(self):
        pass

    def delete_vacancy(self):
        pass

    def get_by_salary(self):
        pass




class JSONSaver(Saver):
    vacancies = []
