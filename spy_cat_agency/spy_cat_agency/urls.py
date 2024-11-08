from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cats.views import CatViewSet
from missions.views import MissionViewSet

router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'missions', MissionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]