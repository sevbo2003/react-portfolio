from .serializers import PostSerializer, CategorySerializer, ProjectSerializer, ChallengeNameSerializer, \
    Day30Serializer, ThanksSerializer
from .models import Post, Category, Project, ChallengeName, Day30, Thanks
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ChallengeNameViewSet(ModelViewSet):
    queryset = ChallengeName.objects.all()
    serializer_class = ChallengeNameSerializer


class Day30ViewSet(ModelViewSet):
    queryset = Day30.objects.all()
    serializer_class = Day30Serializer


class ThanksViewSet(ModelViewSet):
    queryset = Thanks.objects.all()
    serializer_class = ThanksSerializer
