import requests


class PokeAPI():

    def __init__(self):
        self.requests = requests.Session()

    def allPokemon(self):
        list_pokemon = []
        MAX_POKEMON = 1000

        for i in range(1, MAX_POKEMON):
            if pokemon == "Not Found":
                break
                
            pokemon = self.requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(i)).text
            list_pokemon.append(pokemon)

        if len(list_pokemon) == 0:
            return []
        
        return list_pokemon

    def getPokemon(self, id):

        pokemon = self.requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(id)).json()

        if pokemon != "Not Found":
            list_pokemon.append(pokemon)

        if len(list_pokemon) == 0:
            return []

        return list_pokemon
