from rest_framework import viewsets
from .models import Music, Design
from .serializers import MusicSerializer, DesignSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class DesignViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
