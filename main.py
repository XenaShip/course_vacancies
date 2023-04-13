from src.vacancy import Vacancy, Vacancies
from src.savers import JSONSaver
from src.jop_api import HeadHunterAPI


# def user_interaction():
    # platforms = ["HeadHunter", "SuperJob"]
    # search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)


if __name__ == '__main__':
    # user_interaction()
    k_word = 'Python'
    help1 = HeadHunterAPI()
    a = help1.get_vacancies(k_word)
    c = JSONSaver()
    c.add_vacancies(a)
    for i in c.all_vacancies:
       print(i)
    print('_________________________')
    c.sort_vacancies_by_salary()
    # for i in c.all_vacancies:
      #   print(i)
    d = a[0:1]
    c.delete_vacancies(d)
    c.save_vacancies()
    print('=================')
    c.read_vacancies()
#     c.delete_vacancies(d)
    print('____________________________')
    for i in c.all_vacancies:
        print(i)
