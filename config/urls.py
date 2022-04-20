from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .routers import urlpatterns as router_urls

scheme_view = get_swagger_view(title="Abdusamad Malikov API")

# 3rd party and Django default
urlpatterns = [
    path("admin/", admin.site.urls),  # admin panel
    path("api/", scheme_view),  # api swagger view
    path("api-auth/", include("rest_framework.urls")),  # api registration
    path("ckeditor/", include('ckeditor_uploader.urls'))  # ckeditor url
]

# local apps include
urlpatterns += router_urls

# media and static urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)
