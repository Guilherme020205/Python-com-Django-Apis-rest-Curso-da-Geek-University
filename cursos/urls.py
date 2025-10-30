from django.urls import path

from .views import CursoApiView, AvaliacaoApiView

urlpatterns = [
    path('cursos/', CursoApiView.as_view() ,name='cursos'),
    path('avaliacoes/', AvaliacaoApiView.as_view(), name='avaliacoes'),
]