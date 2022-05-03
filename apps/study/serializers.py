from rest_framework import serializers
from .models import BookCategory, Book, Reading, Podcast, Talk, Tutorial


class BookSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.category')

    class Meta:
        model = Book
        fields = ['id', 'category', 'name', 'description', 'status', 'link', 'added']


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


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ('id', 'name', 'description', 'author', 'image', 'link', 'time')


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id', 'name', 'description', 'author', 'category', 'link', 'time')
