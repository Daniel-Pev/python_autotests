from sens_inf import MyData


class Cgf:
    TOKEN = MyData.my_token  # Enter your token
    TRAINER_ID = MyData.my_trainer_id  # Enter your trainer id
    URL = 'https://api.pokemonbattle.ru/v2'
    HEADERS = {'trainer_token': TOKEN, 'Content-Type': 'application/json'}
    CREATE_POKEMON_BODY = {
        "name": "Собакен",
        "photo_id": 1
    }
    VALID = {
        'email': MyData.my_email,  # Enter valid mail
        'password': MyData.me_password  # Enter valid password
    }
