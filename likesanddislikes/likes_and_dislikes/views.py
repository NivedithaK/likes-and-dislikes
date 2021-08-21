from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from likes_and_dislikes.models import Card, Guess, Lobby, Player
from likes_and_dislikes.serializers import CardSerializer, GuessSerializer, PlayerSerializer
from likes_and_dislikes.utils import generate_lobby_id

@api_view(['POST'])
def create_lobby_and_host(request):
    print(request.data)
    lobby_id = generate_lobby_id()
    lobby = Lobby.objects.create(lobby_id=lobby_id)
    
    player_data = {**request.data, "lobby": lobby.pk}
    player_serializer = PlayerSerializer(data=player_data)
    if player_serializer.is_valid():
        print("VALID!!!!")
        player_serializer.save()
    print(player_serializer.errors)
    print(Lobby.objects.all())
    print(Player.objects.all())
    return Response(status=status.HTTP_201_CREATED)
