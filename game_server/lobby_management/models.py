from django.db import models

class Lobby(models.Model):
	name = models.CharField(max_length=60, primary_key=True)
	curr_players = models.IntegerField()
	max_players = models.IntegerField()
	game_map = models.CharField(max_length=148)
	server_ip = models.GenericIPAddressField()
	server_port = models.IntegerField() 

	def __str__(self):
		return self.name