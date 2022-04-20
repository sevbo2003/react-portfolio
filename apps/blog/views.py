from .serializers import PostSerializer, CategorySerializer, ProjectSerializer
from .models import Post, Category, Project
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
