import requests
from src.vacancy import Vacancy


class JobAPI:
    def __init__(self):
        pass

    def get_vacancies(self, name_job):
        pass


class HeadHunterAPI(JobAPI):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name_job):
        url = self.url
        ans = []
        for i in range(2):
            par = {'text': name_job, 'per_page': '3', 'page': i}
            r = requests.get(url, params=par)
            e = r.json()
            for j in e['items']:
                job_id = j['id']
                job_url = j['alternate_url']
                name = j['name']
                if not((j['salary'] is None) or (j['salary']['from'] is None)):
                    salary_from = j['salary']['from']
                else:
                    salary_from = 0
                requirements = j['snippet']['requirement']
                if not(j['address'] is None):
                    city = j['address']['city']
                else:
                    city = None
                vacanc = Vacancy(job_id, job_url, name, salary_from, requirements, city)
                ans.append(vacanc)
        return ans
