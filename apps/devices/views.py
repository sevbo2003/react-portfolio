from rest_framework.viewsets import ModelViewSet
from .models import MySetup, DailyUses, Accessories, Development, Keyboard, Template
from .serializers import (
    MySetupSerializers,
    DailyUsesSerializer,
    AccessoriesSerializer,
    DevelopmentSerializer,
    KeyboardSerializer,
    TemplateSerializer,
)


class MySetupViewSetup(ModelViewSet):
    queryset = MySetup.objects.filter(active=True)
    serializer_class = MySetupSerializers


class DailyUsesViewSet(ModelViewSet):
    queryset = DailyUses.objects.filter(active=True)
    serializer_class = DailyUsesSerializer


class AccessoriesViewSet(ModelViewSet):
    queryset = Accessories.objects.filter(active=True)
    serializer_class = AccessoriesSerializer


class DevelopmentViewSet(ModelViewSet):
    queryset = Development.objects.filter(active=True)
    serializer_class = DevelopmentSerializer


class KeyboardViewSet(ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer


class TemplateViewSet(ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
