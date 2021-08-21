from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from likes_and_dislikes.models import Card, Guess, Lobby, Player
from likes_and_dislikes.serializers import CardSerializer, GuessSerializer, LobbySerializer, PlayerSerializer
from likes_and_dislikes.utils import generate_lobby_id, is_valid_lobby

@api_view(['POST'])
def create_lobby_and_host(request):
    lobby_id = generate_lobby_id()
    lobby = Lobby.objects.create(lobby_id=lobby_id)
    player_data = {**request.data, "lobby": lobby.pk}
    player_serializer = PlayerSerializer(data=player_data)
    if player_serializer.is_valid():
        player = player_serializer.create(player_serializer.validated_data)
    else:
        lobby.delete()
    return Response(data={"lobby_code": lobby_id, "player_id": player.id, "players_in_lobby": lobby.list_all_players()}, status=status.HTTP_201_CREATED)

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
def set_like_dislike(request):
    card_data = {**request.data, "player": request.data["player_id"]}
    if Card.objects.filter(player__pk=card_data["player"]).exists():
        return Response("Error: A card for this player already exists", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    card_serializer = CardSerializer(data=card_data)
    if card_serializer.is_valid():
        card_serializer.save()
    return Response(card_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_game_list(request):
    try:
        lobby = Lobby.objects.get(lobby_id=request.data["lobby_id"])
    except Lobby.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cards = Card.objects.filter(player__lobby=lobby)
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def enter_guess(request):
    try:
        player = Player.objects.get(pk=request.data["player_id"])
    except Player.DoesNotExist:
        return Response("Player (guesser) not found", status=status.HTTP_404_NOT_FOUND)
    try:
        card = Card.objects.get(pk=request.data["card_id"])
    except Card.DoesNotExist:
        return Response("Card not found", status=status.HTTP_404_NOT_FOUND)
    try:
        guessed_player = Player.objects.get(pk=request.data["guess"])
    except Player.DoesNotExist:
        return Response("Guessed player not found", status=status.HTTP_404_NOT_FOUND)

    guess_data = {"guessed_player": guessed_player.pk, "player": player.pk, "card": card.pk}

    guess_serializer = GuessSerializer(data=guess_data)
    if guess_serializer.is_valid():
        guess_serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(guess_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_guess_history(request):
    try:
        player = Player.objects.get(pk=request.data["player_id"])
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    guess_history = [{"like": x.card.like, "dislike": x.card.dislike, "guess": x.player.nickname} for x in player.guesses.all()]
    return Response(data={"guess_history": guess_history})

@api_view(['GET'])
def get_lobby_scores(request):
    try:
        lobby = Lobby.objects.get(pk=request.data["lobby_id"])
    except Lobby.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    player_scores = [{"player": x.nickname, "score": x.score} for x in lobby.players.all()]
    return Response(data={"scoreboard": player_scores})

@api_view(['GET'])
def get_all_likes(request):
    try:
        lobby = Lobby.objects.get(pk=request.data["lobby_id"])
    except Lobby.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cards = Card.objects.filter(player__lobby=lobby).all()
    players_likes = [{"player": x.player.nickname, "like": x.like} for x in cards]
    return Response(data={"likes": players_likes})

@api_view(['GET'])
def get_all_dislikes(request):
    try:
        lobby = Lobby.objects.get(pk=request.data["lobby_id"])
    except Lobby.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cards = Card.objects.filter(player__lobby=lobby).all()
    players_dislikes = [{"player": x.player.nickname, "dislike": x.dislike} for x in cards]
    return Response(data={"dislikes": players_dislikes})
