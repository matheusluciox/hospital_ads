from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import statusConsultaViewSet

router = DefaultRouter()
router.register(r'statusConsulta', statusConsultaViewSet, basename='statusConsulta')

urlpatterns = [
    path('', include(router.urls)),
]