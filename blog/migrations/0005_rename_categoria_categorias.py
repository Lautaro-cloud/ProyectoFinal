# Generated by Django 4.0.4 on 2022-06-05 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_autor_categoria'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Categorias',
        ),
    ]