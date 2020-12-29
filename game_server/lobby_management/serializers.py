from rest_framework import serializers

from .models import Lobby

class LobbySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lobby
        fields = ('name', 'curr_players', 'max_players', 'game_map', 'server_ip', 'server_port')