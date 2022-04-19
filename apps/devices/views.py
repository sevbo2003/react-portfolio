from rest_framework.viewsets import ModelViewSet
from .models import MySetup, DailyUses, Accessories
from .serializers import MySetupSerializers, DailyUsesSerializer, AccessoriesSerializer


class MySetupViewSetup(ModelViewSet):
    queryset = MySetup.objects.filter(active=True)
    serializer_class = MySetupSerializers


class DailyUsesViewSet(ModelViewSet):
    queryset = DailyUses.objects.filter(active=True)
    serializer_class = DailyUsesSerializer


class AccessoriesViewSet(ModelViewSet):
    queryset = Accessories.objects.filter(active=True)
    serializer_class = AccessoriesSerializer
