from django.shortcuts import render
from rest_framework import viewsets

from .serializers import LobbySerializer
from .models import Lobby

class LobbyViewSet(viewsets.ModelViewSet):
    queryset = Lobby.objects.all().order_by('name')
    serializer_class = LobbySerializer