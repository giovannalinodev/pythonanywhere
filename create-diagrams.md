# 1. Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# 2. Instalar pacotes necessários
pip install django django-extensions Pillow
sudo apt-get install graphviz graphviz-dev
pip install pygraphviz

# 3. Adicionar 'django_extensions' ao INSTALLED_APPS em settings.py
# (Já está adicionado no seu projeto)

# 4. Comandos para gerar diagramas de modelos
# Gerar diagrama para o app enquetes
python manage.py graph_models enquetes --output enquetes_models.png

# Gerar diagrama para o app acervo
python manage.py graph_models acervo --output acervo_models.png

# Gerar diagrama para múltiplos apps simultaneamente
python manage.py graph_models enquetes acervo --output meus_apps.png

# Gerar diagrama para todos os apps (incluindo os do Django)
python manage.py graph_models --all --output all_models.png

# Gerar diagrama com configurações específicas
python manage.py graph_models --all --group-models --exclude-models=User,Group,Session --output models_custom.png

# Gerar diagrama sem mostrar campos
python manage.py graph_models --all --disable-fields --output models_simplified.png

# Gerar diagrama mostrando apenas relações de herança
python manage.py graph_models --all --inheritance --output inheritance.png