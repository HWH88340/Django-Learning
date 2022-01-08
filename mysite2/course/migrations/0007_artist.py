# Generated by Django 3.1.2 on 2020-10-15 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20201015_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(choices=[('vinyl', 'Vinyl'), ('cd', 'CD')], max_length=10)),
                ('video', models.CharField(choices=[('vhs', 'VHS Tape'), ('dvd', 'DVD')], max_length=10)),
            ],
        ),
    ]