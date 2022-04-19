from rest_framework.viewsets import ModelViewSet
from .models import MySetup, DailyUses
from .serializers import MySetupSerializers, DailyUsesSerializer


class MySetupViewSetup(ModelViewSet):
    queryset = MySetup.objects.filter(active=True)
    serializer_class = MySetupSerializers


class DailyUsesViewSet(ModelViewSet):
    queryset = DailyUses.objects.filter(active=True)
    serializer_class = DailyUsesSerializer
