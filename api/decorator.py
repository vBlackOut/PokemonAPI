from functools import wraps
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse

def check_token():
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            token_request = args[1].headers['Authorization'].split('Token ')[1].strip()

            try:
                user_auth_tuple = TokenAuthentication().authenticate(request=args[1])
                args[1].user = user_auth_tuple[0] # if not implemented return anonymous user
            except AuthenticationFailed:
                return JsonResponse({"result": "Error Authentification Failed", "status":"error", "code": 3})

            if len(user_auth_tuple) == 0 and str(user_auth_tuple[1]) != token_request:
               return JsonResponse({"result": "Error Authentification Failed", "status":"error", "code": 3})

            oldfunction = func(*args, **kwargs)
            return oldfunction

        return wrapper
    return real_decorator
