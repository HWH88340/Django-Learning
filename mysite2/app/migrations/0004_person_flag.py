# Generated by Django 3.1.2 on 2020-10-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201030_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='flag',
            field=models.BooleanField(default=True),
        ),
    ]
