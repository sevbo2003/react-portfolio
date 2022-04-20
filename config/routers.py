from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.blog.views import PostViewSet, CategoryViewSet
from apps.devices.views import (
    MySetupViewSetup,
    DailyUsesViewSet,
    AccessoriesViewSet,
    DevelopmentViewSet,
    KeyboardViewSet,
    TemplateViewSet,
)
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
# study category
router.register("books", BookViewSet)
router.register("bookCategories", BookCategoryViewSet)
router.register("readings", ReadingViewSet)
router.register("podcasts", PodcastViewSet)
router.register("talks", TalkViewSet)
router.register("tutorials", TutorialViewSet)

# entertainment
router.register("musics", MusicViewSet)
router.register("gallery", GalleryViewSet)

# devices
router.register("my-setup", MySetupViewSetup)
router.register("daily-uses", DailyUsesViewSet)
router.register("accessories", AccessoriesViewSet)
router.register("development-tools", DevelopmentViewSet)
router.register("keyboards", KeyboardViewSet)
router.register("website-templates", TemplateViewSet)

# blog
router.register('posts', PostViewSet)
router.register('post-categories', CategoryViewSet)

urlpatterns = [path("", include(router.urls))]
