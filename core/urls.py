from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .swagger_yasg import urlpatterns as swagger_yasg


api_patterns = [path("", include("apps.social.urls"))]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(api_patterns)),
] + swagger_yasg

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    *i18n_patterns(*urlpatterns,prefix_default_language=False),

]