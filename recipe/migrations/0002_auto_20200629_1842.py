# Generated by Django 3.0.7 on 2020-06-29 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instruction',
            options={'ordering': ['priority']},
        ),
    ]
