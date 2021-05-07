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
            except AuthenticationFailed:
                return JsonResponse({"result": "Error Authentification Failed", "status":"error", "code": 3})

            if len(user_auth_tuple) >= 1 and str(user_auth_tuple[1]) == token_request:
                oldfunction = func(*args, **kwargs)
                return oldfunction
            else:
                return JsonResponse({"result": "Error Authentification Failed", "status":"error", "code": 3})

        return wrapper
    return real_decorator