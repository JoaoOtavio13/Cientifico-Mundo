# Científico Mundo

## Descrição
Este é um projeto de divulgação científica que permite aos usuários visualizar e interagir com artigos e projetos científicos, incluindo a possibilidade de comentar sobre os artigos e visualizar projetos com filtros específicos.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos antes de rodar o projeto:

- Python 3.x
- pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)
- Django 3.x ou superior
- Banco de dados SQLite (já configurado por padrão)

## Passo a passo para rodar o projeto

### 1. Clonar o repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/seuusuario/seu-repositorio.git

### Entre no diretório do projeto:
cd Cientifico-Mundo

## Se você ainda não tem um ambiente virtual configurado, crie um com o comando abaixo:
python -m venv venv

## Ative seu Ambiente Virtual:

### Windows:
venv\Scripts\activate

### Mac/Linux:
source venv/bin/activate

## Instale todas as dependências do projeto com o pip:
pip install -r requirements.txt

## Antes de rodar o projeto, você precisa rodar as migrações do Django para configurar o banco de dados:
python manage.py makemigrations
python manage.py migrate

## Criar um superusuário:
python manage.py createsuperuser

## Rodar o servidor de desenvolvimento
python manage.py runserver

### Acessar o painel administrativo (opcional) Depois de rodar o servidor, você pode acessar o painel de administração do Django em:
http://127.0.0.1:8000/admin/



