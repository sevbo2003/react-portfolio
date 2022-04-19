from rest_framework import serializers
from .models import MySetup, DailyUses


class MySetupSerializers(serializers.ModelSerializer):
    class Meta:
        model = MySetup
        fields = "__all__"


class DailyUsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyUses
        fields = '__all__'
