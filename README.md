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

```
----

### 2. Entre no diretório do projeto:
```bash
cd Cientifico-Mundo

````
----

## 3. Se você ainda não tem um ambiente virtual configurado, crie um com o comando abaixo:
```bash
python -m venv venv
```
----
## 4. Ative seu Ambiente Virtual:

- Windows:
```bash
venv\Scripts\activate
```

- Mac/Linux:
```bash
source venv/bin/activate
```
----

## 5. Instale todas as dependências do projeto com o pip:
```bash
pip install -r requirements.txt
```
----

## 6. Antes de rodar o projeto, você precisa rodar as migrações do Django para configurar o banco de dados:
```bash
python manage.py makemigrations
python manage.py migrate
```
----

## 7. Criar um superusuário:
```bash
python manage.py createsuperuser
```
----

## 8. Rodar o servidor de desenvolvimento
```bash
python manage.py runserver
```
----
### 9. Acessar o painel administrativo (opcional) Depois de rodar o servidor, você pode acessar o painel de administração do Django em:
```bash
http://127.0.0.1:8000/admin/
```




