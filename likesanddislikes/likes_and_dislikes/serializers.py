from rest_framework import serializers
from likes_and_dislikes.models import Card, Guess, Lobby, Player

class PlayerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update_like(self, player, like):
        player.update_like(like)

    def update_dislike(self, player, dislike):
        player.update_dislikes(dislike)

    def update_score(self, player):
        player.increment_score()
    
    class Meta:
        model = Player
        fields = '__all__'

class LobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobby
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Card.objects.create(**validated_data)

    class Meta:
        model = Card
        fields = '__all__'

class GuessSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Guess.objects.create(**validated_data)

    class Meta:
        model = Guess
        fields = '__all__'