# Generated by Django 3.1.7 on 2021-09-08 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okr', '0002_auto_20210908_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='parent_key_result',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_key_result', to='okr.keyresult'),
        ),
    ]