import random, string
from likes_and_dislikes.models import Lobby

def generate_lobby_id():
    id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    while(Lobby.objects.filter(lobby_id=id).exists()):
        id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return id

def is_valid_lobby(lobby_id):
    return Lobby.objects.filter(lobby_id=lobby_id).exists()