# Generated by Django 4.2.4 on 2023-09-04 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_videomodel_uploaded_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videomodel',
            name='uploaded_on',
        ),
    ]