# Generated by Django 3.0.8 on 2020-10-07 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Levip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='CLIE_PASSWORD',
            field=models.TextField(default=None),
        ),
    ]
