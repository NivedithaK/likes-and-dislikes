from django.db import models

class Lobby(models.Model):
    lobby_id = models.CharField(max_length=6, primary_key=True)

class Player(models.Model):
    nickname = models.CharField(max_length=32)
    lobby = models.ForeignKey('Lobby', on_delete=models.CASCADE, null=True)
    points = models.PositiveIntegerField(default=0)

    def update_likes(self, likes):
        Card.objects.get(player=self).update(likes=likes)

    def update_dislikes(self, dislikes):
        Card.objects.get(player=self).update(dislikes=dislikes)

    def increment_points(self):
        self.points = points + 1
    
    def assign_lobby(self, lobby):
        self.lobby = lobby

    class Meta:
        ordering = ['points', 'nickname']

class Card(models.Model):
    player = models.OneToOneField('Player', on_delete=models.CASCADE)
    likes = models.CharField(max_length=64, blank=True, null=True)
    dislike = models.CharField(max_length=64, blank=True, null=True)

class Guess(models.Model):
    player = models.ForeignKey('Player', related_name="guess", on_delete=models.CASCADE)
    card = models.OneToOneField('Card', on_delete=models.CASCADE)
    guessed_player = models.ForeignKey('Player', related_name="guessed_as", on_delete=models.CASCADE)
