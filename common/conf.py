class Cgf:
    TOKEN = '471a6700525e0d0c32cff970cb441077'
    TRAINER_ID = 21298
    URL = 'https://api.pokemonbattle.ru/v2'
    HEADERS = {'trainer_token': TOKEN, 'Content-Type': 'application/json'}
    CREATE_POKEMON_BODY = {
        "name": "Собакен",
        "photo_id": 1
    }
    VALID = {
        'email': 'pelevin.d99@yandex.ru',
        'password': 'Parolotpokemon1'
    }