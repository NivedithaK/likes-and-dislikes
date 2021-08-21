from django.db import models

class Lobby(models.Model):
    lobby_id = models.CharField(max_length=6, primary_key=True)
    game_has_started = models.BooleanField(default=False)
    current_card = models.IntegerField(default=0)

    def list_all_players(self):
        return Player.objects.filter(lobby__pk=self.lobby_id).values_list('nickname', flat=True)

class Player(models.Model):
    nickname = models.CharField(max_length=32)
    lobby = models.ForeignKey('Lobby', related_name="players", on_delete=models.CASCADE, null=True)
    score = models.PositiveIntegerField(default=0)

    def update_like(self, like):
        Card.objects.get(player=self).update(like=like)

    def update_dislike(self, dislike):
        Card.objects.get(player=self).update(dislike=dislike)

    def increment_score(self):
        self.score = score + 1
    
    def assign_lobby(self, lobby):
        self.lobby = lobby

    class Meta:
        ordering = ['score', 'nickname']

class Card(models.Model):
    player = models.OneToOneField('Player', related_name="card", on_delete=models.CASCADE)
    like = models.CharField(max_length=64, blank=True, null=True)
    dislike = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ['pk']

class Guess(models.Model):
    player = models.ForeignKey('Player', related_name="guesses", on_delete=models.CASCADE)
    card = models.OneToOneField('Card', on_delete=models.CASCADE)
    guessed_player = models.ForeignKey('Player', related_name="guessed_as", on_delete=models.CASCADE)
