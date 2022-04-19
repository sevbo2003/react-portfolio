from rest_framework import serializers
from .models import MySetup, DailyUses, Accessories, Development, Keyboard, Template


class MySetupSerializers(serializers.ModelSerializer):
    class Meta:
        model = MySetup
        fields = "__all__"


class DailyUsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyUses
        fields = '__all__'


class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'


class DevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Development
        fields = '__all__'


class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = ('id', 'name', 'description', 'image_url', 'image', 'url',)


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id', 'name', 'description', 'image_url', 'image', 'url',)
