from rest_framework import serializers
from .models import Music, Gallery


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('name', 'author', 'length', 'uzunligi', 'link', 'added')


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('name', 'image', 'download_link', 'image_size', 'time')
