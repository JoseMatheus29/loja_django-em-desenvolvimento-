# Generated by Django 3.2.7 on 2021-09-12 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lojaapp', '0003_rename_carrinho_carro'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='carrinhoproduto',
            new_name='CarroProduto',
        ),
    ]
