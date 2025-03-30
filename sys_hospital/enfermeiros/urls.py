from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnfermeiroViewSet

router = DefaultRouter()
router.register(r'enfermeiros', EnfermeiroViewSet, basename='enfermeiro')

urlpatterns = [
    path('', include(router.urls))
]