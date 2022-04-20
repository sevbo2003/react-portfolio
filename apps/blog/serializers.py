from rest_framework import serializers
from .models import Category, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'name', 'category', 'description', 'body', 'image', 'created', 'time', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
