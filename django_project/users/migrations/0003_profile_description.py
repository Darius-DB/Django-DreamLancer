# Generated by Django 3.0.3 on 2020-10-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201005_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default='None'),
        ),
    ]
