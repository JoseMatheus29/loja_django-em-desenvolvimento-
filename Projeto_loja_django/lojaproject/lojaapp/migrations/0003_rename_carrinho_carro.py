# Generated by Django 3.2.7 on 2021-09-11 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lojaapp', '0002_rename_categorias_categoria'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='carrinho',
            new_name='Carro',
        ),
    ]
