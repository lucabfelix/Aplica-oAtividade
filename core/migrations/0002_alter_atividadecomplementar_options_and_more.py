# Generated by Django 4.2.2 on 2023-06-16 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atividadecomplementar',
            options={'verbose_name': 'Atividade Complementar', 'verbose_name_plural': 'Atividades Complementares'},
        ),
        migrations.AlterModelOptions(
            name='tipoatividade',
            options={'verbose_name': 'Tipo de Atividade', 'verbose_name_plural': 'Tipos de Atividades'},
        ),
    ]
