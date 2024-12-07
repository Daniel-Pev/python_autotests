import requests

from common.conf import Cgf


class ApiPokemon:
    url = Cgf.URL + '/pokemons'

    def __init__(self):
        self.response = None
        self.pokemon_id = None

    def create_pokemon(self, json_body=None, url=url):
        if json_body is None:
            json_body = Cgf.CREATE_POKEMON_BODY
        self.response = requests.post(url=url, headers=Cgf.HEADERS,
                                      json=json_body)
        self.pokemon_id = self.response.json()['id']
        print('Создаю покемона...')
        print(f'Сообщение сервера: {self.response.json()['message']}\nАйди покемона: {self.response.json()['id']}\n'
              f'Статус код ответа: {self.response.status_code}')
        return self

    def change_pokemon(self,new_pokemon_name, new_photo_id, url=url, pokemon_id=None):
        if pokemon_id is None:
            pokemon_id = self.pokemon_id
        self.response = requests.put(url=url, headers=Cgf.HEADERS, json={
            "pokemon_id": pokemon_id,
            "name": new_pokemon_name,
            "photo_id": new_photo_id
        })
        print('Меняю покемона...')
        print(f'Сообщение сервера: {self.response.json()['message']}\nАйди покемона: {self.response.json()['id']}\n'
              f'Статус код ответа: {self.response.status_code}')
        return self

    def catch_pokemon(self, pokemon_id=None, url=Cgf.URL + '/trainers/add_pokeball'):
        if pokemon_id is None:
            pokemon_id = self.pokemon_id
        self.response = requests.post(url=url, headers=Cgf.HEADERS, json={
            "pokemon_id": pokemon_id
        })
        print('Ловлю покемона в покебол...')
        print(f'Сообщение сервера: {self.response.json()['message']}\nАйди покемона: {self.response.json()['id']}\n'
              f'Статус код ответа: {self.response.status_code}')
        return self


pokemon = ApiPokemon()
pokemon.create_pokemon()
pokemon.change_pokemon(new_pokemon_name='Новая сабака', new_photo_id=2)
pokemon.catch_pokemon()
