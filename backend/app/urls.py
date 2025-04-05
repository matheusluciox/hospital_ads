from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from consultas.views import ConsultaViewSet
from doencas.views import DoencaViewSet
from enderecos.views import EnderecoViewSet
from enfermeiros.views import EnfermeiroViewSet
from especializacoes.views import EspecializacaoViewSet
from medicos.views import MedicoViewSet
from pacientes.views import PacienteViewSet


# Configuração do roteador do DRF
router = DefaultRouter()
router.register(r'api/consultas', ConsultaViewSet)
router.register(r'api/doencas', DoencaViewSet)
router.register(r'api/enderecos', EnderecoViewSet)
router.register(r'api/enfermeiros', EnfermeiroViewSet)
router.register(r'api/especializacoes', EspecializacaoViewSet)
router.register(r'api/medicos', MedicoViewSet)  # Rota para médicos
router.register(r'api/pacientes', PacienteViewSet)  # Rota para pacientes

# Definição das rotas
urlpatterns = [
    path('admin/', admin.site.urls),  

    # Geração do esquema OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Outras rotas
    path('', include(router.urls)),  # Rotas geradas automaticamente pelo roteador
]