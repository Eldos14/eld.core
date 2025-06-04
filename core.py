import requests

class Mystat:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def get_auth(self, login, password):
        url = "https://mapi.itstep.org/v1/mystat/auth/login"
        headers = {"accept": "application/json"}
        data = {"login": login, "password": password}

        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return True, response.json().get("data", {}).get("token")
        else:
            return False, None

    def get_schedule(self, date, week=False):
        result = self.get_auth(self.login, self.password)
        if not result[0]:
            return False

        if week:
            url = f"https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type=week&date_filter={date}"
        else:
            url = f"https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type=month&date_filter={date}"

        headers = {"authorization": f"Bearer {result[1]}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            for i in reesponse.json()['date']:
                print(i['date'],i['teacher_name'])
            return response.json()
        else:
            return False

    def get_marks(self):
        result = self.get_auth(self.login, self.password)
        if not result[0]:
            return False

        url = "https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks"
        headers = {"authorization": f"Bearer {result[1]}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return False
