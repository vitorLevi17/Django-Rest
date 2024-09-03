from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import *
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="Documentação API",
      default_version='v1',
      description="Documentação da API escola",
      terms_of_service="https://www.google.com/policies/terms/", # os 3 abaixo podem ser alterados
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


router = DefaultRouter(trailing_slash=False)
router.register(prefix='estudantes',viewset=EstudantesViewSet,basename='Estudantes')
router.register(prefix='cursos',viewset=CursoViewSet,basename='Cursos')
router.register(prefix='matriculas',viewset=MatriculaViewSet,basename='Matriculas')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('estudantes/<int:pk>/matriculas/',ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
