# Generated by Django 2.2.6 on 2020-01-03 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_alunos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionario',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='testes',
            name='aluno',
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
    ]