# Generated by Django 3.2.9 on 2021-11-18 18:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id_movies', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=512)),
                ('release_year', models.IntegerField()),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
