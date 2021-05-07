import requests


class PokeAPI():

    def __init__(self):
        self.requests = requests.Session()

    def allPokemon(self):
        list_pokemon = []
        MAX_POKEMON = 1000

        for i in range(1, MAX_POKEMON):
            pokemon = self.requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(i)).text
            list_pokemon.append(pokemon)

            if pokemon == "Not Found":
                break

        if len(list_pokemon) >= 1:
            return list_pokemon
        else:
            return []

    def getPokemon(self, id):
        list_pokemon = []
        MAX_POKEMON = 1000

        pokemon = self.requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(id)).json()

        if pokemon != "Not Found":
            list_pokemon.append(pokemon)


        if len(list_pokemon) >= 1:
            return list_pokemon
        else:
            return []
