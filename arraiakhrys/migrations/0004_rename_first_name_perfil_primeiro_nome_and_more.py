# Generated by Django 4.0.5 on 2022-06-08 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arraiakhrys', '0003_alter_perfil_email_alter_perfil_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='first_name',
            new_name='primeiro_nome',
        ),
        migrations.RenameField(
            model_name='perfil',
            old_name='last_name',
            new_name='ultimo_nome',
        ),
    ]
