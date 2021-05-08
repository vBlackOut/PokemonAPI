from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from api.pokemon import PokeAPI
from api.decorator import check_token
from api.models import userBase, PokemonUser

# Error Code API
# 1 - No found
# 2 - Error Bad method send
# 3 - Bad communication AuthenticationFailed

class Pokemon(APIView):

    @classmethod
    @check_token()
    def getAll(self, request):
        if request.method != "GET":
            return JsonResponse({"result": "Error method api", "status":"error", "code": 2})

        if not isinstance(all_pokemon, list) or len(all_pokemon) == 0:
            return JsonResponse({"result": "Error empty list", "status":"error", "code": 1})

        all_pokemon = PokeAPI.allPokemon()

        return JsonResponse({"result": all_pokemon, "status": "success"})



    @classmethod
    @check_token()
    def getPokemon(self, request, id):

        if request.method != "GET":
            return JsonResponse({"result": "Error method api", "status":"error", "code": 2})


        if not isinstance(all_pokemon, list) or len(all_pokemon) == 0:
            return JsonResponse({"result": "Error Pokemon not found", "status":"error", "code": 1})

        pokemon = PokeAPI.getPokemon(id)
        return JsonResponse({"result": pokemon, "status": "success"})




    @classmethod
    @check_token()
    def addPokemon(self, request, type):

        if request.method != "POST":
            return JsonResponse({"result": "Error method api", "status":"error", "code": 2})

        if not type.isdigit():
            return JsonResponse({"result": "Error input value", "status":"error", "code": 2})

        check_pokemon = PokemonUser.objects.filter(pokemon_id=type)

        if not check_pokemon:
            id_pokemon = PokemonUser.objects.get(pokemon_id=type)
            userBase.objects.create(user=request.user, pokemon=id_pokemon)

        id_pokemon = PokemonUser.objects.create(pokemon_id=type)

        return JsonResponse({"result": "ok", "status": "success"})


    @classmethod
    @check_token()
    def removePokemon(self, request, type):

        if not type.isdigit():
            return JsonResponse({"result": "Error input value", "status":"error", "code": 2})

        check_pokemon = PokemonUser.objects.filter(pokemon_id=type)

        if not check_pokemon:
            return JsonResponse({"result": "No Pokemon found", "status":"error", "code": 1})

        userBase.objects.get(user=request.user, pokemon_id=type).pokemon.delete()


        return JsonResponse({"result": "ok", "status": "success"})


    @classmethod
    @check_token()
    ### API user
    def me(self, request):
        # TO DO...
        pass

