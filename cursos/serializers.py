from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        # Cadastro de configurações extra da classe
        extra_kwargs = {
            # write_only não será apresentado quando alguem consultar a avaliação mantendo ele em segredo a terceiros
             'email': {'write_only': True},
        }
        # Esse model é importado la em cima, esse se refere a Avaliacao
        model = Avaliacao
        # Campos que irão aparecer para usuario quando ele pesquisar
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        #extra_kwargs = {}
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        )
