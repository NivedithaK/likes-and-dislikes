from rest_framework import serializers
from likes_and_dislikes.models import Card, Guess, Lobby, Player

class PlayerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update_likes(self, player, likes):
        player.update_likes(likes)

    def update_dislikes(self, player, dislikes):
        player.update_dislikes(dislikes)

    def update_points(self, player):
        player.increment_points()
    
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