from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import *

router = DefaultRouter(trailing_slash=False)
router.register(prefix='estudantes',viewset=EstudantesViewSet,basename='Estudantes')
router.register(prefix='curso',viewset=CursoViewSet,basename='Cursos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))

]
