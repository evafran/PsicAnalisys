# Generated by Django 2.2.6 on 2020-01-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200103_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='nome')),
                ('senha', models.IntegerField(verbose_name='senha')),
                ('confirmarSenha', models.IntegerField(verbose_name='confirmarSenha')),
            ],
        ),
    ]