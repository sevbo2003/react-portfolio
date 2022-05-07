from rest_framework import serializers
from .models import Music, Design


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'name', 'author', 'image', 'link', 'added')


class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = ('id', 'name', 'description', 'author', 'image', 'link', 'time')
