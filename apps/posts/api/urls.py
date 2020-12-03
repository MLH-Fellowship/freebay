from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.posts.api import views as av

router = DefaultRouter()
router.register(r"items", av.ItemsViewSet)

urlpatterns = [
    path("", include(router.urls)),    
]
