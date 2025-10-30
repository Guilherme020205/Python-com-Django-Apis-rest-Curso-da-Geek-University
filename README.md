# Python-com-Django-Apis-rest-Curso-da-Geek-University

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

### Rotas 
Criar o arquivo de rotas dentro de `cursos/` com o nome `/urls.py`
Após criar as rotas adicionar elas em `/escola/urls.py` dentro de `urlpatterns`

### Status http
Importar `from rest_framework import status` no arquivo para poder devolver respostas ao usuario 
