# Generated by Django 4.2.6 on 2023-11-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='description',
        ),
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.AddField(
            model_name='location',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
