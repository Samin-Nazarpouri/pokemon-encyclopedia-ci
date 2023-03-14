import unittest
import unittest.mock
import re
from main import fetch_pokemon


class ResponseMock:

    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def requests_get_mock(*args, **kwargs):
    pokemon_id = int(re.match('https://pokeapi.co/api/v2/pokemon/(.+)', args[0]).group(1))
    if pokemon_id:
        return ResponseMock({'id': pokemon_id}, 200)
    else:
        return ResponseMock(None, 404)


class TestEncyclopedia(unittest.TestCase):

    def test_get_pokemon_data_with_real_api(self):
        pokemon = fetch_pokemon(pokemon_id=12)
        self.assertEqual(pokemon['name'], 'butterfree')

    def test_get_pokemon_data_with_mock_api(self):
        with unittest.mock.patch('requests.get', side_effect=requests_get_mock):
            pokemon = fetch_pokemon(pokemon_id=12)
            self.assertEqual(pokemon['id'], 12)


if __name__ == '__main__':
    unittest.main()
