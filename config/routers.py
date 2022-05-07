from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.blog.views import (
    PostViewSet,
    CategoryViewSet,
    ProjectViewSet,
    ChallengeNameViewSet,
    Day30ViewSet,
    ThanksViewSet
)
from apps.devices.views import (
    MySetupViewSetup,
    DailyUsesViewSet,
    AccessoriesViewSet,
    DevelopmentViewSet,
    KeyboardViewSet,
    LinkViewSet,
)
from apps.entertainment.views import MusicViewSet, DesignViewSet
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
router.register("design", DesignViewSet)

# devices
router.register("my-setup", MySetupViewSetup)
router.register("daily-uses", DailyUsesViewSet)
router.register("accessories", AccessoriesViewSet)
router.register("development-tools", DevelopmentViewSet)
router.register("keyboards", KeyboardViewSet)
router.register("links", LinkViewSet)

# blog
router.register("posts", PostViewSet)
router.register("post-categories", CategoryViewSet)

# projects
router.register("projects", ProjectViewSet)

# 30 Day Challenge
router.register('challenge-name', ChallengeNameViewSet)
router.register('day-30', Day30ViewSet)

# other
router.register('thanks', ThanksViewSet)

urlpatterns = [path("", include(router.urls))]
