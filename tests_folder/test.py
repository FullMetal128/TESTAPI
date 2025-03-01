import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
from constants import const
import requests
import pytest



@pytest.mark.parametrize("name, job", [
    ("olig", "starlord"),
    ("dima", "iron man"),
    ("RJSONIO", "raccoon")
])
def test_create_users(delete_user, name, job):
    data = const.data_create_user(name, job)
    response = requests.post(url = 'https://reqres.in/api/users', json= data)
    with open(r'C:\Users\dima-\PycharmProjects\TESTAPI\data\id.txt', "w", encoding="utf-8") as file:
        file.write(response.json()['id'])

    assert response.status_code == 201, f'success{response.json()}'
