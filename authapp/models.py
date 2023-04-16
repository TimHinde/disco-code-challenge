from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    subscription = models.ForeignKey('authapp.Subscription', to_field='name', on_delete=models.CASCADE, null=True,
                                     blank=True)


class Subscription(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False, primary_key=True)
    # thumbnails = models.ForeignKey('subscriptions.Thumbnail', on_delete=models.CASCADE, null=False, blank=False)
    link_to_original = models.BooleanField()
    expiring_links = models.BooleanField()


class Thumbnail(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    x_size = models.PositiveIntegerField()
    y_size = models.PositiveIntegerField()
