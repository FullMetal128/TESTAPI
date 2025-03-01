import requests
def read_txt():
    try:
        with open(r'C:\Users\dima-\PycharmProjects\TESTAPI\data\id.txt', "r", encoding="utf-8") as file:
            return  file.readlines()[0]
    except:
        return None

def get():
    response = requests.get(url='https://reqres.in/api/users/975')
    return response.status_code

