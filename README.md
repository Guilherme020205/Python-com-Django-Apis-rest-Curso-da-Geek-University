# Python-com-Django-Apis-rest-Curso-da-Geek-University

senha forte usuario feliz: uGetS@PXW2cMLue

Primeiro de tudo baixar o Django, ir no site e ver a versão LTS mais recente. 
https://www.djangoproject.com/download/

Iniciar um projeto com o comando `python -m django startproject meu_projeto . `
_**no comando é usado um ponto no final para que não sejá criado um sub diretorio.**_

Iniciar uma aplicação com o comando `python -m django startapp cursos`

Algumas configurações dentro do projeto **escola** entre em **settings.py** ir até 
**INSTALLED_APPS** escrever o nome da aplicação criada `'cursos'`, 
mudar a `LANGUAGE_CODE = 'en-us'` para `LANGUAGE_CODE = 'pt-br'` e a 
`TIME_ZONE = 'UTC'` para `TIME_ZONE = 'America/Sao_Paulo'`.

Importa  os no topo do projeto `import os`

Em baixo de `STATIC_URL = 'static/'` acrescentar 
`STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`
`MEDIA_URL = 'media/'`
`MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`

Para criação de models ir para o arquivo `model.py` explicação no arquivo

Após criar os models registrar no `admin.py` 

Toda vez que você mudar algo nos models (ex: adicionar campo novo), precisa:
`python manage.py makemigrations`
`python manage.py migrate`

Agora criar um usuário administrador (ou “superusuário”) que tem 
acesso total ao painel administrativo do Django com o 
comando `python manage.py createsuperuser`


Para rodar o servidor usar o comando `python manage.py runserver`

# Criar a API

Rodar o comando `pip install djangorestframework markdown django-filter`

Criar um arquivo de requerimentos com o comando `pip freeze > requirements.txt`

Adicionar algumas configurações de novo dentro do projeto escola 
entre em settings.py ir até INSTALLED_APPS escrever o nome das bibliotecas
adicioandas `django_filters` e `rest_framework`

Adicionar no arquivo settings ao fim da página o codigo a baixo que 
serve como autenticação
`#DRF
REST_FRAMEWORK = {
    # Autenticacao
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    # Autorizacao
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}`

Entrar no arquivo urls.py e importar o include `from django.urls import path, include`
e adicionar no urlpattens o `path('auth/', include('rest_framework.urls'))`
(Serve para você testar a autenticação diretamente na interface do DRF, sem precisar criar uma tela de login ainda.)

### Model Serializers
Serve para transformar o django model em estrutura json para lidar com as requisições da api 
Criar o arquivo `cursos/serializers.py`

### Views
Implementar as views para acessar a api quando as req https forem feitas, fazer em `cursos/views.py` 
(esse modelo ficou no arquivo old_views.py após utilizarmos do generic views, metodo mais rapido de escrever)

### Rotas 
Criar o arquivo de rotas dentro de `cursos/` com o nome `/urls.py`
Após criar as rotas adicionar elas em `/escola/urls.py` dentro de `urlpatterns`

### Status http
Importar `from rest_framework import status` no arquivo para poder devolver respostas ao usuario 

### Generic views
Ele melhora a criação dos crud, fazer em `cursos/views.py`, o que foi feito em 39 linhas se resume em 15
com ele será adicionado também os outros crud então tem de adicionar as urls em `urls.py`

### Sobrescrevendo as views
As vezes poderar ter condições ao fazer uma requisição, podemos buscar todos os cursos ou apenas o curso com id 2 
para fazer isso sobrescrevemos a view, na pagina `urls.py` percebece o uso de curso_pk ou avaliacoes_pk que seriam
os id, por padrao ele não faz isso corretamente, então temos de ir na pasta `views.py` e implementar essas condições

### V2
Criando uma nova versão começamos criando as views novas com view set e depois mudando as urls.

### View set
Recurso que permite agrupar toda logica de um recurso em uma class que é o view set 

### Routers
Ele cria os caminhos das apis as urls 

De pois que fazer os view set no `views.py` e o routers no `urls.py` entramos no `escola/urls.py` 
e configuramos a rota da api v2

### Relações 
Criar uma relação entre modelos, no exemplo ele ira mostrar todas as avaliações do curso no arquivo 
`serializers.py` estão comentados no código igual à tabela abaixo

    # Nested Relationshipe
    Ele retorna todos os dados de avaliação que cada curso tem
    
    # HyperLinked Related Field
    Ele retorna um link que leva para os dados de avaliação de cada curso
    
    # Primary Key Related Field
    Ele retorna apenas o id de todas avaliações do curso

### Paginação 
Ir em REST_FRAMEWORK no arquivo `escola.settings.py` e adicionar o `DEFAULT_PAGINATION_CLASS`

Quando colocar paginação, vamos nos models e escrever que a ordem de listar deve ser pelo id `ordering = ['id']`
dentro de `class Meta` de cada uma das class, se quiser na ordem decrescente colocar `-id` ficando assim `ordering = ['-id']`

    Metodos extras tem que ser adicionado a paginação manualmente, exemplo no arquivo 
    `cursos/views.py` no CursoViewSet dentro de action na 'V2' colocar dentro do def
    algo assim:     
    {
     self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
    }

### Utilizando autenticação via Token
Lá no começo foi colocado uma autenticação para ser acessado na web do django, mas para outros serviços tem de
ter uma melhor autenticação. Para isso entrar no `escola/settings.py` ir até `INSTALLED_APPS` 
e adicionar `rest_framework.authtoken`, com isso ir no mesmo arquivo no `REST_FRAMEWORK` mudar no 
`DEFAULT_AUTHENTICATION_CLASSES` de `rest_framework.authentication.SessionAuthentication` para 
`rest_framework.authentication.TokenAuthentication`

Feito isso rodar o comando `python manage.py migrate` para atualizar as tabelas.

Está pronto! 

    Testando o token 
    Dentro do terminar digite alguns comandos para consegui cadastrar um tokem pro usuario
    
    # Comando para abrir o shell
    `python manage.py shell`

    # Importar a class token e User
    `from rest_framework.authtoken.models import Token`
    `from django.contrib.auth.models import User`
    
    # Pegar o usuario
    guilherme = User.objects.get(id=1)
    se ecrever o nome do usuario ele tem que retornar <User: guilherme>    
    se ecrever guilherme.email ele tem que retornar o email cadastrado     
    
    # Comando para criar o token 
    `token = Token.objects.create(user=guilherme)`

    # Comando para receber o token 
    `token.key`
    
    Para testar entra no insomnia cria o request e usando post,put ou del va em headers, clicar em add
    no campo header escrever `Authorization` no campo value `Token xxxx` o xxx representa o seu token  

### Permissões
Permissões do uso do sistema para os usuarios
importar na `cursos/views.py` `from rest_framework import permissions`
foi adicionado na versão `v2` na class Curso o codigo`permission_classes = (permissions.DjangoModelPermissions, )`
com isso ele altera qual a permissão os usuarios vão ter nessa view especifica


### Validando dados recebidos 
Podemos criar dentro de `serializers.py` um metodo novo `def validate_avaliacao`
