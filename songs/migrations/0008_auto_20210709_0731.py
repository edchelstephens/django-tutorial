# Generated by Django 3.1.7 on 2021-07-08 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_auto_20210707_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(blank=True, null=True)),
                ('invite_reason', models.CharField(max_length=120)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_memberships', to='songs.group')),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='songs.musician')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='groups', through='songs.Membership', to='songs.Musician'),
        ),
    ]
