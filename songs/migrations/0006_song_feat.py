# Generated by Django 3.1.7 on 2021-07-06 23:12

from django.db import migrations, models
import songs.models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_artist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='feat',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(songs.models.get_unkown_artist), related_name='featured_artist', to='songs.artist'),
        ),
    ]