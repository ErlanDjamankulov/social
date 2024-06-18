from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="Social API",
        default_version="v1",
        description="""
      """,
        terms_of_service="https://github.com/ErlanDjamankulov/social",
        license=openapi.License(name="↑ GitHub ↑"),
    ),
    public=True,
    permission_classes=[
        permissions.IsAdminUser,
    ],

)


urlpatterns = [
    path("docs<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redocs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

]
