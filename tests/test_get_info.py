import pytest
import requests
from pytest_voluptuous import S

from const import RAPID_KEY_CORRECT, MESSAGE_INCORRECT_KEY, MESSAGE_WITHOUT_KEY, BASE_URL
from schemas.get_info import InfoResponseSchema, InfoErrorResponseSchema


def test_get_info_validation_schema():
    """Успешное получение информации о патчах, классах, наборов, локациях, локализациях, фракциях,
    качествах, расах и локализациях и валидация ответа по схеме"""
    response = requests.get(url=BASE_URL + "/info",
                            headers={'X-RapidAPI-Key': RAPID_KEY_CORRECT})

    assert response.status_code == 200
    assert response.json() == S(InfoResponseSchema)


@pytest.mark.parametrize('token', ["1", "2061bb4d51msh0af114688494336p17c2fajsnaf485760b16b"])
def test_get_info_with_incorrect_key_validation_schema(token):
    """Неуспешное получение информации взято минимальное не корректный 'X-RapidAPI-Key' из одного
    символа и измененный в одном символе корректный ключ и валидация ответа по схеме """
    response = requests.get(url=BASE_URL + "/info",
                            headers={'X-RapidAPI-Key': token})

    response_json = response.json()

    assert response.status_code == 403
    assert response_json == S(InfoErrorResponseSchema)
    assert response_json['message'] == MESSAGE_INCORRECT_KEY


@pytest.mark.parametrize('token', [None, ""])
def test_get_info_without_key_validation_schema(token):
    """Неуспешное получение информации взято минимальное не корректный 'X-RapidAPI-Key'
    с пустым ключем и без него и валидация ответа по схеме """
    response = requests.get(url="https://omgvamp-hearthstone-v1.p.rapidapi.com/info",
                            headers={'X-RapidAPI-Key': token})

    response_json = response.json()

    assert response.status_code == 401
    assert response_json == S(InfoErrorResponseSchema)
    assert response_json['message'] == MESSAGE_WITHOUT_KEY
