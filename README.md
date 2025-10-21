# Python-com-Django-Apis-rest-Curso-da-Geek-University

Primeiro de tudo baixar o Django, ir no site e ver a versão LTS mais recente. 
https://www.djangoproject.com/download/

Iniciar um projeto com o comando`py -m django startproject meu_projeto . `
_**no comando é usado um ponto no final para que não sejá criado um sub diretorio.**_

Iniciar uma aplicação com o comando `py -m django startapp cursos`

Algumas configurações dentro do projeto **escola** entre em **settings.py** ir até 
**INSTALLED_APPS** escrever o nome da aplicação criada `'cursos'`, 
mudar a `LANGUAGE_CODE = 'en-us'` para `LANGUAGE_CODE = 'pt-br'` e a 
`TIME_ZONE = 'UTC'` para `TIME_ZONE = 'America/Sao_Paulo'`.

Importa o os no topo do projeto `import os`

Em baixo de `STATIC_URL = 'static/'` acrescentar 
`STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`
`MEDIA_URL = 'media/'`
`MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`

Para criação de models ir para o arquivo `model.py` explicação no arquivo

Após criar os models registrar no `admin.py` 