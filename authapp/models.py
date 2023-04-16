from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    subscription = models.ForeignKey('authapp.Subscription', to_field='name', on_delete=models.CASCADE, null=True,
                                     blank=True)


class Subscription(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False, primary_key=True)
    thumbnails = models.ManyToManyField('Thumbnail', null=False, blank=False)
    link_to_original = models.BooleanField()
    expiring_links = models.BooleanField()


class Thumbnail(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    x_size = models.PositiveIntegerField()
    y_size = models.PositiveIntegerField()
