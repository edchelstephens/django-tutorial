# Generated by Django 3.1.7 on 2021-06-28 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20210628_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(db_column='artister', on_delete=django.db.models.deletion.CASCADE, to='songs.artist'),
        ),
    ]
