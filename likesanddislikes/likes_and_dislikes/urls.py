from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('create-lobby-and-host/', views.create_lobby_and_host, name='create_lobby_and_host'),
    path('join-lobby/', views.join_lobby, name='join_lobby'),
    path('set-like-dislike/', views.set_like_dislike, name='set_like_dislike'),
    path('game-list/', views.get_game_list, name='get_game_list'),
    path('enter-guess/', views.enter_guess, name='enter_guess'),
    path('guess-history/', views.get_guess_history, name='get_guess_history'),
]

urlpatterns = format_suffix_patterns(urlpatterns)