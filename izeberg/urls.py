"""izeberg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from api.views import Pokemon

urlpatterns = [
    path('admin/', admin.site.urls),

    # management
    path('api/login', obtain_auth_token, name='api_token_auth'),
    url(r'^api/group/(?P<type>\w+)/add$', Pokemon.addPokemon),
    url(r'^api/group/(?P<type>\w+)/remove$', Pokemon.removePokemon),
    path('api/user/me', obtain_auth_token, name='api_token_auth'),

    # api back
    path('api/pokemon', Pokemon.getAll, name='api_token_auth'),
    url(r'^api/pokemon/(?P<id>\w+)$', Pokemon.getPokemon),
]
