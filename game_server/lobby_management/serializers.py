from rest_framework import serializers

from .models import Lobby

class LobbySerializer(serializers.HyperlinkedModelSerializer):
	name = serializers.CharField(read_only=True, source="name")
	max_players = serializers.IntegerField(read_only=True, source="max_players")
	game_map = serializers.CharField(read_only=True, source="game_map")
	server_ip = serializers.GenericIPAddressField(read_only=True, source="server_ip")
	server_port = serializers.IntegerField(read_only=True, source="server_port")
    class Meta:
        model = Lobby
        fields = ('curr_players')
        #fields = ('name', 'curr_players', 'max_players', 'game_map', 'server_ip', 'server_port')