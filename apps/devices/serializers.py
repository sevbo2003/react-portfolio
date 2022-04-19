from rest_framework import serializers
from .models import MySetup, DailyUses, Accessories, Development


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
