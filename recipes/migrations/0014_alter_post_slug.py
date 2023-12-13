# Generated by Django 3.2.22 on 2023-12-12 20:05

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
