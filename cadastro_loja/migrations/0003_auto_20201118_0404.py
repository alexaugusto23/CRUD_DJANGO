# Generated by Django 3.1.3 on 2020-11-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_loja', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbpessoa',
            name='celular',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='tbpessoa',
            name='cep',
            field=models.CharField(max_length=8),
        ),
    ]
