# Generated by Django 5.0.6 on 2024-05-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scootsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='questionset',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='scootsapp.tag'),
        ),
    ]
