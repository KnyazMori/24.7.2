import pytest


from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()


def test_add_new_pet_with_negative_age(
        name = 'Барсик',
        animal_type = 'кот',
        age = -5
):

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert 'name' in result


def test_add_new_pet_with_long_name(
        name = 'fhdkvmfivmf486dmsks/vnfjtlvhm4nhujbcfhlmbcswqgbmkp.hvvjkllgjuebftmllhdsaqacvvhjjnllb25863394jhdsvnb',
        animal_type = 'собака',
        age = 2
):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert 'name' in result


def test_unsuccess_animal_type(
        name = 'Кеша',
        animal_type = 'rgr22',
        age = 3
):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert 'name' in result


def test_unsuccess_age(
        name = 'Гоша',
        animal_type = 'кит',
        age = 'бессмертный'
):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert 'name' in result


def test_unsuccess_name(
        name = 1158,
        animal_type = 'тигр',
        age = 8
):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert 'name' in result