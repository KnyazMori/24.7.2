import requests

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, password):

        headers = {
            'email' : email,
            'password' : password
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code

        result = ""

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code

        result = ""

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def post_add_pet_with_photo(self, auth_key, name, animal_type, age, pet_photo):
        headers = {'auth_key' : auth_key['key']}
        name = {'name' : name}
        animal_type = {'animal_type' : animal_type}
        age = {'age' : age}
        pet_photo = {'pet_photo' : pet_photo}

        headers = {'auth_key' : auth_key['key']}
        file = {'pet_photo' : (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=file)
        status = res.status_code

        result = ""

        try:
            result = res.json()
        except:
            result = res.text

        return status, result