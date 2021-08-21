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
        player = player_serializer.create(player_serializer.validated_data)
    return Response(data={"lobby_code": lobby_id, "player_id": player.id, "players_in_lobby": []}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def join_lobby(request):
    if not is_valid_lobby(request.data["lobby_id"]):
        return Response(status=status.HTTP_404_NOT_FOUND)
    lobby = Lobby.objects.get(lobby_id=request.data["lobby_id"])
    player_data = {**request.data, "lobby": lobby.pk}
    player_serializer = PlayerSerializer(data=player_data)
    if player_serializer.is_valid():
        player = player_serializer.create(player_serializer.validated_data)
    return Response(data={"player_id": player.id, "players_in_lobby": lobby.list_all_players()}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def set_likes_dislikes(request):
    card_data = {**request.data, "player": request.data["player_id"]}
    card_serializer = CardSerializer(data=card_data)
    if card_serializer.is_valid():
        card_serializer.save()
    print(Card.objects.all())
    return Response(data={"IT WORKED"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def enter_guess(request):
    card_data = {**request.data, "player": request.data["player_id"]}
    card_serializer = CardSerializer(data=card_data)
    if card_serializer.is_valid():
        card_serializer.save()
    print(Card.objects.all())
    return Response(data={"IT WORKED"}, status=status.HTTP_201_CREATED)