from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('create-lobby-and-host/', views.create_lobby_and_host, name='create_lobby_and_host'),
    path('join-lobby/', views.join_lobby, name='join_lobby'),
    path('set-likes-dislikes/', views.set_likes_dislikes, name='set_likes_dislikes'),
]

urlpatterns = format_suffix_patterns(urlpatterns)