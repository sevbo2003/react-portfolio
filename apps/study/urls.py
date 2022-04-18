from .views import BookViewSet, BookCategoryViewSet, ReadingViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
# Routers
router.register("books", BookViewSet)
router.register("bookCategories", BookCategoryViewSet)
router.register("readings", ReadingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
