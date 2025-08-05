# Geração de Diagramas UML - Classes de Domínio

Este projeto inclui geração automática de diagramas UML das classes de domínio usando Django Extensions.

## 🎯 Objetivo

Gerar diagramas UML que representam visualmente a estrutura das classes de domínio do sistema de acervo, incluindo:
- Modelos de dados (Item, Livro, Contato, Emprestimo)
- Relacionamentos entre as classes
- Campos e tipos de dados

## 🛠️ Ferramentas Utilizadas

- **django-extensions**: Extensão do Django para geração de diagramas
- **pygraphviz**: Biblioteca para renderização de gráficos
- **pydot**: Interface Python para Graphviz
- **graphviz**: Software de visualização de gráficos

## 📋 Pré-requisitos

### Dependências Python (já incluídas no requirements.txt)
```
django-extensions==3.2.3
pygraphviz==1.11
pydot==1.4.2
pyparsing==3.1.1
```

### Dependências do Sistema
```bash
# Ubuntu/Debian
sudo apt-get install graphviz graphviz-dev pkg-config

# macOS
brew install graphviz

# Windows
# Baixar e instalar Graphviz de: https://graphviz.org/download/
```

## 🚀 Como Usar

### 1. Instalação Local
```bash
# Instalar dependências do sistema
sudo apt-get update
sudo apt-get install -y graphviz graphviz-dev pkg-config

# Instalar dependências Python
pip install -r requirements.txt
```

### 2. Gerar Diagrama Manualmente
```bash
# Comando simples para gerar o diagrama
cd mysite
python manage.py graph_models acervo enquetes \
  --output=../domain_class_diagram.png \
  --exclude-models=User \
  --group-models \
  --arrow-shape=normal \
  --layout=dot \
  --rankdir=TB \
  --theme=original
```

### 3. Geração Automática no Pipeline
O diagrama é gerado automaticamente a cada push/PR através do pipeline OWASP (`owasp.yml`).

## 📊 Diagrama Gerado

### Diagrama das Classes de Domínio (`domain_class_diagram.png`)
- Mostra as classes dos apps `acervo` e `enquetes`
- Exclui o modelo `User` do Django para focar no domínio da aplicação
- Layout hierárquico (top-bottom) para melhor visualização
- Tema original com cores claras e linhas definidas

## 🔧 Personalização do Comando

```bash
# Incluir todos os campos (mais detalhado)
python manage.py graph_models acervo enquetes --verbose-names --output=detailed.png

# Diferentes layouts
python manage.py graph_models acervo --layout=circo --output=circular.png

# Diferentes temas
python manage.py graph_models acervo --theme=django2018 --output=modern.png

# Formato SVG (vetorial)
python manage.py graph_models acervo enquetes --output=diagram.svg
```

## 📁 Localização dos Arquivos

- **Diagrama gerado**: `domain_class_diagram.png` (raiz do projeto)
- **Pipeline**: `.github/workflows/owasp.yml`
- **Configuração**: `mysite/mysite/settings.py` (django_extensions habilitado)

## 🔄 Integração com Pipeline

O diagrama é automaticamente:
- Gerado a cada build do pipeline OWASP
- Salvo como artefato por 30 dias
- Disponibilizado para download na aba "Actions" do GitHub
- Incluído nos relatórios de qualidade

### Estrutura no Pipeline:
1. **Instalar dependências do sistema** (Graphviz)
2. **Instalar dependências Python** (requirements.txt)
3. **Gerar diagrama UML** (comando Django direto)
4. **Upload do artefato** (disponível para download)
5. **Exibir resumo** (status da geração)

## 🔍 Verificação Local

Para verificar se o diagrama foi gerado corretamente:

```bash
# Verificar se o arquivo existe
ls -la domain_class_diagram.png

# Verificar tamanho do arquivo
du -h domain_class_diagram.png

# Visualizar (Linux com visualizador de imagens)
xdg-open domain_class_diagram.png
```

## 📈 Benefícios

1. **Simplicidade**: Comando direto, sem scripts auxiliares
2. **Automação**: Geração automática no pipeline CI/CD
3. **Documentação Visual**: Facilita entendimento da arquitetura
4. **Manutenção**: Diagrama sempre atualizado com o código
5. **Qualidade**: Integrado com verificações OWASP

## 🐛 Solução de Problemas

### Erro: "graph_models command not found"
```bash
# Verificar se django_extensions está instalado
pip show django-extensions

# Verificar se está em INSTALLED_APPS
grep -r "django_extensions" mysite/mysite/settings.py
```

### Erro: "pygraphviz installation failed"
```bash
# Instalar dependências do sistema primeiro
sudo apt-get install graphviz-dev pkg-config
pip install --force-reinstall pygraphviz
```

### Diagrama não é gerado
```bash
# Testar se Graphviz está instalado
dot -V

# Verificar permissões de escrita
touch test_write && rm test_write

# Executar com debug
python manage.py graph_models acervo --verbosity=2
```

## 🎨 Exemplo de Uso no GitHub Actions

O pipeline executará automaticamente:
```yaml
- name: Generate UML Class Diagram
  run: |
    cd mysite
    python manage.py graph_models acervo enquetes \
      --output=../domain_class_diagram.png \
      --exclude-models=User \
      --group-models \
      --arrow-shape=normal \
      --layout=dot \
      --rankdir=TB \
      --theme=original
```

Resultado disponível em: **Actions → Workflow → Artifacts → uml-class-diagram**