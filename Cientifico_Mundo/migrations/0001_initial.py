# Generated by Django 5.1.2 on 2024-10-13 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupaçao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=255)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='usuarios')),
                ('ocupacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cientifico_Mundo.ocupacao')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cientifico_Mundo.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Validacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cientifico_Mundo.instituicao')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('introducao', models.TextField()),
                ('objetivo', models.TextField()),
                ('metodologia', models.TextField()),
                ('resultados', models.TextField()),
                ('conclusao', models.TextField()),
                ('imagem', models.ImageField(upload_to='capas/')),
                ('orientador', models.CharField(max_length=150)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cientifico_Mundo.usuario')),
                ('validacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cientifico_Mundo.validacao')),
            ],
        ),
    ]
