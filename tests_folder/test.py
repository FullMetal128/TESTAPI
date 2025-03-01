import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
from constants import const
import requests

def test_create_users(delete_user, name, job):
    data = const.data_create_user(name, job)
    response = requests.post(url = 'https://reqres.in/api/users', json= data)
    assert response.status_code == 201
    assert response.json() == data