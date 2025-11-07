from django.urls import path

from .views import CursoApiView, CursosApiView, AvaliacaoApiView, AvaliacoesApiView

urlpatterns = [
    path('cursos/', CursosApiView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes'),

    path('cursos/<int:pk>/', CursoApiView.as_view() ,name='curso'),
    path('avaliacoes/<int:pk>/', AvaliacaoApiView.as_view(), name='avaliacao')
]