# Generated by Django 2.0.13 on 2020-04-13 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comentario',
        ),
    ]
