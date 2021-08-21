import random, string
from likes_and_dislikes.models import Lobby

def generate_lobby_id():
    id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    # while(Lobby.objects.get(lobby_id=id).exists()):
    #     id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return id