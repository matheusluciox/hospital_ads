from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EspecializacaoViewSet

router = DefaultRouter()
router.register(r'especializacoes', EspecializacaoViewSet, basename='especilizacao')

urlpatterns = [
    path('', include(router.urls))
]