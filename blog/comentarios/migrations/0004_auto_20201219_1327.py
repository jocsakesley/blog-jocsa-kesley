# Generated by Django 3.1.4 on 2020-12-19 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_auto_20201219_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='publicado_comentario',
            field=models.BooleanField(default=True, verbose_name='Publicado'),
        ),
    ]
