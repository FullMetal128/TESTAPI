import requests
import pytest
from constants import const
import basic_func.read_file


@pytest.mark.parametrize("name, job", [
    ("olig", "starlord"),
    ("dima", "iron man"),
    ("jorjio", "raccoon")
])

@pytest.fixture()
def create_user(name: str, job: str) -> int:
    data = const.data_create_user(name, job)
    response = requests.post(url = 'https://reqres.in/api/users', json= data)
    assert response.status_code == 201
    file = open(r'C:\Users\dima-\PycharmProjects\TESTAPI\data\id.txt')
    file.write(response.json()['id'])
    file.close()
    return response.json()['id']

@pytest.fixture()
def delete_user():
    id = basic_func.read_file.read_txt()
    response = requests.get(url= f'https://reqres.in/api/users{id}')
    assert response.status_code == 200
    yield
    response_delete = requests.delete(url = f'https://reqres.in/api/users{id}')
    assert response_delete.status_code == 204
