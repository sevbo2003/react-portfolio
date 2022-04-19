from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.devices.views import MySetupViewSetup, DailyUsesViewSet, AccessoriesViewSet, DevelopmentViewSet
from apps.entertainment.views import MusicViewSet, GalleryViewSet
from apps.study.views import (
    BookViewSet,
    BookCategoryViewSet,
    ReadingViewSet,
    PodcastViewSet,
    TalkViewSet,
    TutorialViewSet,
)

router = DefaultRouter()
router.register("books", BookViewSet)
router.register("bookCategories", BookCategoryViewSet)
router.register("readings", ReadingViewSet)
router.register("podcasts", PodcastViewSet)
router.register("talks", TalkViewSet)
router.register("tutorials", TutorialViewSet)
router.register("musics", MusicViewSet)
router.register("gallery", GalleryViewSet)
router.register("my-setup", MySetupViewSetup)
router.register("daily-uses", DailyUsesViewSet)
router.register("accessories", AccessoriesViewSet)
router.register("development-tools", DevelopmentViewSet)

urlpatterns = [path("", include(router.urls))]
