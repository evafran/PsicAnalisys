# Generated by Django 2.2.6 on 2020-01-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario',
            name='pergunta',
            field=models.CharField(blank=True, max_length=100, verbose_name='pergunta'),
        ),
    ]