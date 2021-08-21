from django.db import models

class Lobby(models.Model):
    lobby_id = models.CharField(max_length=6, primary_key=True)

    def list_all_players(self):
        return Player.objects.filter(lobby__pk=self.lobby_id).values_list('nickname', flat=True)

class Player(models.Model):
    nickname = models.CharField(max_length=32)
    lobby = models.ForeignKey('Lobby', on_delete=models.CASCADE, null=True)
    points = models.PositiveIntegerField(default=0)

    def update_like(self, like):
        Card.objects.get(player=self).update(like=like)

    def update_dislike(self, dislike):
        Card.objects.get(player=self).update(dislike=dislike)

    def increment_points(self):
        self.points = points + 1
    
    def assign_lobby(self, lobby):
        self.lobby = lobby

    def get_all_guesses(self):
        return Guess.objects.filter(player=self).all()#.values_list('card__like', 'card__dislike', 'guessed_player__nickname')

    class Meta:
        ordering = ['points', 'nickname']

class Card(models.Model):
    player = models.OneToOneField('Player', related_name="card", on_delete=models.CASCADE)
    like = models.CharField(max_length=64, blank=True, null=True)
    dislike = models.CharField(max_length=64, blank=True, null=True)

class Guess(models.Model):
    player = models.ForeignKey('Player', related_name="guess", on_delete=models.CASCADE)
    card = models.OneToOneField('Card', on_delete=models.CASCADE)
    guessed_player = models.ForeignKey('Player', related_name="guessed_as", on_delete=models.CASCADE)
