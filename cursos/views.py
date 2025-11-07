from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


# essa class usando .ListCreateAPIView ela vai listar e vai poder criar Cursos por isso nomeamos no plural CursosApi...
class CursosApiView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# essa class usando .RetrieveUpdateDestroyAPIView ela vai listar, editar e deletar um Curso por isso nomeamos no singular CursoApi...
class CursoApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesApiView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # condições do get, ele vai retornar todas as avaliações que tem o id do curso
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()

class AvaliacaoApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # condição get que vai retornar todas as avaliação do curso com id enviado, e caso tenha enviado o id da avaliação
    # junto ira mostrar apenas essa 
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.queryset, pk=self.kwargs.get('avaliacao_pk'))
