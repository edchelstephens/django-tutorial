# Generated by Django 3.1.7 on 2021-07-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='characteristics',
            field=models.JSONField(default=dict),
        ),
    ]
