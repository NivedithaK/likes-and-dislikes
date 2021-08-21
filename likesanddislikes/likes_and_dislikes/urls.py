from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('create-lobby-and-host/', views.create_lobby_and_host, name='create_lobby_and_host'),
    path('join-lobby/', views.join_lobby, name='join_lobby'),
    path('set_likes_dislikes/', views.set_likes_dislikes, name='set_likes_dislikes'),
    path('enter_guess/', views.enter_guess, name='enter_guess'),
]

urlpatterns = format_suffix_patterns(urlpatterns)