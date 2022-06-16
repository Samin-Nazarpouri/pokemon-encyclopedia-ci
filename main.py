import requests
import random

pokemon_ids = random.sample(range(1, 152), 6)

for pokemon_id in pokemon_ids:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    # Converts from JavaScript Object Notation into Python lists and dictionaries
    pokemon_data = response.json()

    print(f"You got pokemon number {pokemon_data['id']}, {pokemon_data['name'].capitalize()}!")
    print(f"Height: {pokemon_data['height']} • Weight: {pokemon_data['weight']}")

    pokemon_types = []
    for type_data in pokemon_data['types']:
        pokemon_types.append(type_data['type']['name'])

    print(f"Type(s): {' and '.join(pokemon_types)}")

    pokemon_abilities = []
    for ability_data in pokemon_data['abilities']:
        pokemon_abilities.append(ability_data['ability']['name'])

    print(f"Abilities: {', '.join(pokemon_abilities)}")
    print()
