from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from djangospotifydownloader.quickstart import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"links", views.LinkViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api/spotify/callback/", views.spotify_callback, name="spotify_callback"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 