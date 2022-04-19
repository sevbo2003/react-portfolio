from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.devices.views import MySetupViewSetup, DailyUsesViewSet
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
router.register("mysetup", MySetupViewSetup)
router.register("daily-uses", DailyUsesViewSet)

urlpatterns = [path("", include(router.urls))]
