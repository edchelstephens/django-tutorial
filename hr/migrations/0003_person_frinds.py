# Generated by Django 3.1.7 on 2021-06-28 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_person_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='frinds',
            field=models.ManyToManyField(related_name='_person_frinds_+', to='hr.Person'),
        ),
    ]