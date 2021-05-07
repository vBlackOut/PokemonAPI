from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from api.pokemon import PokeAPI
from api.decorator import check_token
from django.http import JsonResponse
from api.models import userBase, PokemonUser
import requests

# Error Code API
# 1 - No found
# 2 - Error Bad method send
# 3 - Bad communication AuthenticationFailed

class Pokemon(APIView):

    @classmethod
    @check_token()
    def getAll(self, request):
        if request.method == "GET":
            client = PokeAPI()

            all_pokemon = client.allPokemon()

            if isinstance(all_pokemon, list) and len(all_pokemon) >= 1:
                return JsonResponse({"result": all_pokemon, "status": "success"})
            else:
                return JsonResponse({"result": "Error empty list", "status":"error", "code": 1})
        else:
            return JsonResponse({"result": "Error method api", "status":"error", "code": 2})

    @classmethod
    @check_token()
    def getPokemon(self, request, id):
        if request.method == "GET":
            client = PokeAPI()

            thepokemon = client.getPokemon(id)

            if isinstance(thepokemon, list) and len(thepokemon) >= 1:
                return JsonResponse({"result": thepokemon, "status": "success"})
            else:
                return JsonResponse({"result": "Error Pokemon not found", "status":"error", "code": 1})
        else:
            return JsonResponse({"result": "Error method api", "status":"error", "code": 2})

    @classmethod
    @check_token()
    def addPokemon(self, request, type):
        user_auth_tuple = TokenAuthentication().authenticate(request=request)

        if type.isdigit():

            check_pokemon = PokemonUser.objects.filter(pokemon_id=type)
            if check_pokemon:
                id_pokemon = PokemonUser.objects.get(pokemon_id=type)
                userBase.objects.create(user=user_auth_tuple[0], pokemon=id_pokemon)
            else:
                id_pokemon = PokemonUser.objects.create(pokemon_id=type)

            return JsonResponse({"result": "ok", "status": "success"})

        else:
            return JsonResponse({"result": "Error input value", "status": "error", "code": 2})

    @classmethod
    @check_token()
    def removePokemon(self, request, type):
        user_auth_tuple = TokenAuthentication().authenticate(request=request)

        if type.isdigit():

            check_pokemon = PokemonUser.objects.filter(pokemon_id=type)

            if check_pokemon:
                print(dir(userBase.objects.get(user=user_auth_tuple[0], pokemon_id=type).pokemon.delete()))
            else:
                return JsonResponse({"result": "No Pokemon found", "status":"error", "code": 1})

            return JsonResponse({"result": "ok", "status": "success"})

        else:
            return JsonResponse({"result": "Error input value", "status":"error", "code": 2})

    @classmethod
    @check_token()
    ### API user
    def me(self, request):
        # TO DO...
        pass
