class Vacancy:
    def __init__(self, job_id, job_url, name, salary_from, requirements, city):
        self.job_id = job_id
        self.job_url = job_url
        self.name = name
        self.salary_from = salary_from
        self.requirements = requirements
        self.city = city

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        return self.salary_from != other.salary_from

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    def __str__(self):
        return f'id: {self.job_id}\n' \
               f'ссылка: {self.job_url}\n' \
               f'профессия: {self.name}\n' \
               f'зарплата от: {self.salary_from}\n' \
               f'требования:  {self.requirements}\n' \
               f'город: {self.city}\n'


class Vacancies:
    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    def filter_vacancies(self):
        self.__all_vacancies.sort(reverse=True)

    @property
    def all_vacancies(self):
        return self.__all_vacancies
