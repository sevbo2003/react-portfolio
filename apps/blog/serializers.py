from rest_framework import serializers
from .models import Category, Post, Project, ChallengeName, Day30, Thanks


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'image',
                  'url', 'created', 'time', 'slug')


class ChallengeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeName
        fields = '__all__'


class Day30Serializer(serializers.ModelSerializer):
    day = serializers.IntegerField(max_value=31, min_value=1)

    class Meta:
        model = Day30
        fields = ('id', 'title', 'challenge', 'day', 'description',
                  'body', 'created', 'time', 'slug', 'url')


class ThanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thanks
        fields = '__all__'
