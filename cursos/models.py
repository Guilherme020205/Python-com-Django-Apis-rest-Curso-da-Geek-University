# Importa o módulo 'models' do Django, usado para criar classes que viram tabelas no banco
from django.db import models

# Classe base para outras tabelas herdarem campos comuns
class Base(models.Model):
    # Data e hora em que o registro foi criado (gerado automaticamente ao criar)
    criacao = models.DateTimeField(auto_now_add=True)
    # Data e hora da última atualização (atualiza sempre que o registro for salvo)
    atualizacao = models.DateTimeField(auto_now=True)
    # Indica se o registro está ativo ou não
    ativo = models.BooleanField(default=True)

    class Meta:
        # Define que essa classe é abstrata, ou seja, não cria tabela no banco,
        # mas serve de base para outras herdarem os campos acima.
        abstract = True


# Tabela de cursos, herdando os campos da classe Base
class Curso(Base):
    # Campo de texto com limite de 255 caracteres
    titulo = models.CharField(max_length=255)
    # Campo específico para URLs, deve ser único no banco
    url = models.URLField(unique=True)

    class Meta:
        # Define nomes mais legíveis no painel admin do Django
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    # Define o que será mostrado quando o objeto for convertido para string (ex: no admin)
    def __str__(self):
        return self.titulo


# Tabela de avaliações, também herdando os campos da Base
class Avaliacao(Base):
    # Cria uma relação com a tabela Curso (chave estrangeira)
    # related_name permite acessar todas as avaliações de um curso (curso.avaliacao.all())
    # on_delete=models.CASCADE apaga as avaliações se o curso for apagado
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)

    # Nome da pessoa que fez a avaliação
    nome = models.CharField(max_length=255)
    # Email do avaliador
    email = models.EmailField()
    # Comentário (pode ser vazio)
    comentario = models.TextField(blank=True, default='')
    # Nota da avaliação (campo decimal, ex: 4.5)
    avaliacao = models.DecimalField(decimal_places=2, max_digits=3)  # corrigido: max_digits precisa ser maior que decimal_places

    class Meta:
        # Define nomes para exibição no admin
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'
        # Garante que uma mesma pessoa (email) só possa avaliar um curso uma vez
        unique_together = (('email', 'curso'),)

    # Mostra uma descrição legível da avaliação
    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso.titulo} com nota {self.avaliacao}'
