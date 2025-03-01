import constants.constants
import requests
import pytest
def test_create_users(delete_user, name, job):
    data = constants.constants.data_create_user(name, job)
    response = requests.post(url = 'https://reqres.in/api/users', json= data)
    assert response.status_code == 201
    assert response.json() == data