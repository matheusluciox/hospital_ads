# Generated by Django 5.1.7 on 2025-03-30 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doencas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doencas',
            old_name='descrição',
            new_name='descricao',
        ),
    ]
