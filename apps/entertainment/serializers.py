from rest_framework import serializers
from .models import Music, Gallery


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'name', 'author', 'image', 'length', 'uzunligi', 'link', 'added')


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'name', 'image', 'download_link', 'image_size', 'time')
