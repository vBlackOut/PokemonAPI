# Generated by Django 3.1 on 2021-05-07 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pokemon',
            new_name='PokemonUser',
        ),
    ]
