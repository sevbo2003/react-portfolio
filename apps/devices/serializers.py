from rest_framework import serializers
from .models import MySetup


class MySetupSerializers(serializers.ModelSerializer):
    class Meta:
        model = MySetup
        fields = "__all__"
