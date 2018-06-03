from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('characters', views.CharacterView)
router.register('origins', views.OriginView)

urlpatterns = [
    path('', include(router.urls))
]
