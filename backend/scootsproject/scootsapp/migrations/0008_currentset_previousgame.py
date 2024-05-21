# Generated by Django 5.0.6 on 2024-05-21 18:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scootsapp', '0007_rename_k_user_pword'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ManyToManyField(related_name='current_set', to='scootsapp.question')),
            ],
        ),
        migrations.CreateModel(
            name='PreviousGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competitive', models.BooleanField(default=False)),
                ('winner', models.CharField(default='', max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ManyToManyField(related_name='previous_games_created', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(related_name='previous_games_played', to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(related_name='previous_game', to='scootsapp.question')),
            ],
        ),
    ]