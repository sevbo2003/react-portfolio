from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

scheme_view = get_swagger_view(title='Abdusamad Malikov API')


# 3rd party and Django default
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', scheme_view),
    path('api-auth/', include('rest_framework.urls')),
]

# local apps include
urlpatterns += [
    path('', include('apps.books.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)
