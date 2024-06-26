# Generated by Django 5.0.6 on 2024-05-20 05:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scootsapp', '0003_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_set',
        ),
        migrations.RemoveField(
            model_name='questionset',
            name='user',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='question',
            name='question_sets',
            field=models.ManyToManyField(related_name='questions', to='scootsapp.questionset'),
        ),
        migrations.AddField(
            model_name='questionset',
            name='owner',
            field=models.ManyToManyField(related_name='questionsets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='student', max_length=255),
        ),
        migrations.CreateModel(
            name='WrongAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('question', models.ManyToManyField(related_name='wrong_answers', to='scootsapp.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='possible_wrong_answers',
            field=models.ManyToManyField(related_name='questions', to='scootsapp.wronganswer'),
        ),
    ]
