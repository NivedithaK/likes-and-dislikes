from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('create-lobby-and-host/', views.create_lobby_and_host, name='create_lobby_and_host'),
    path('join-lobby/', views.join_lobby, name='join_lobby'),
]

urlpatterns = format_suffix_patterns(urlpatterns)