from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from likes_and_dislikes.models import Card, Guess, Lobby, Player
from likes_and_dislikes.serializers import CardSerializer, GuessSerializer, PlayerSerializer
from likes_and_dislikes.utils import generate_lobby_id, is_valid_lobby

@api_view(['POST'])
def create_lobby_and_host(request):
    lobby_id = generate_lobby_id()
    lobby = Lobby.objects.create(lobby_id=lobby_id)
    
    player_data = {**request.data, "lobby": lobby.pk}
    player_serializer = PlayerSerializer(data=player_data)
    if player_serializer.is_valid():
        player_serializer.save()
    return Response(data={"lobby_code": lobby_id}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def join_lobby(request):
    if not is_valid_lobby(request.data["lobby_id"]):
        return 
    lobby = Lobby.objects.get(lobby_id=request.data["lobby_id"])
    player_data = {**request.data, "lobby": lobby.pk}
    player_serializer = PlayerSerializer(data=player_data)
    if player_serializer.is_valid():
        player_serializer.save()
    print(lobby.list_all_players())
    print(type(lobby.list_all_players()))
    return Response(data={"players_in_lobby": lobby.list_all_players()}, status=status.HTTP_201_CREATED)
