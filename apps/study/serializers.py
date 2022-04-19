from rest_framework import serializers
from .models import BookCategory, Book, Reading, Podcast


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'


class PodcastSerializers(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = "__all__"
