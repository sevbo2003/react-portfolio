from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.entertainment.views import MusicViewSet
from apps.study.views import BookViewSet, BookCategoryViewSet, ReadingViewSet, PodcastViewSet, TalkViewSet

router = DefaultRouter()
router.register("books", BookViewSet)
router.register("bookCategories", BookCategoryViewSet)
router.register("readings", ReadingViewSet)
router.register("podcasts", PodcastViewSet)
router.register('talks', TalkViewSet)
router.register('musics', MusicViewSet)

urlpatterns = [
    path('', include(router.urls))
]
