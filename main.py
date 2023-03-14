import requests
import random


def fetch_pokemon(pokemon_id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    return response.json()


def output_pokemon_data(pokemon, file):
    print(f"\n{pokemon['name'].capitalize()} (Pokemon number {pokemon['id']})", file=file)
    print(f"Height: {pokemon['height']} • Weight: {pokemon['weight']}", file=file)

    pokemon_types = []
    for type_data in pokemon['types']:
        pokemon_types.append(type_data['type']['name'])
    print(f"Type{'s' if len(pokemon_types) != 1 else ''}: {' and '.join(pokemon_types)}", file=file)

    pokemon_abilities = []
    for ability_data in pokemon['abilities']:
        pokemon_abilities.append(ability_data['ability']['name'])
    print(f"Abilit{'ies' if len(pokemon_abilities) != 1 else 'y'}: {', '.join(pokemon_abilities)}", file=file)

    pokemon_moves = []
    for move_data in pokemon['moves'][:10]:
        pokemon_moves.append(move_data['move']['name'])
    print(f"Some moves: {', '.join(pokemon_moves)}", file=file)


if __name__ == '__main__':
    pokemon_ids = random.sample(range(1, 152), 6)
    with open('encyclopedia.txt', 'w') as file:
        print("""-----\nHere are some Pokemon for your perusal.\n-----""", file=file)
        for pokemon_id in pokemon_ids:
            pokemon = fetch_pokemon(pokemon_id)
            output_pokemon_data(pokemon, file)
