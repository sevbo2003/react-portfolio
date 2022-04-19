from rest_framework.viewsets import ModelViewSet
from .models import MySetup
from .serializers import MySetupSerializers


class MySetupViewSetup(ModelViewSet):
    queryset = MySetup.objects.filter(active=True)
    serializer_class = MySetupSerializers
