# Generated by Django 4.2 on 2023-04-16 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('image_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
