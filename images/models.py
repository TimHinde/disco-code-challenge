from django.db import models
from django.core.files import File
import urllib
import os


# Create your models here.
# Create image model
class Image(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    image_id = models.CharField(max_length=100, unique=True, blank=False, null=False, primary_key=True)
    user = models.ForeignKey('authapp.User', on_delete=models.CASCADE, null=False, blank=False, to_field='username')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    perm_link = models.URLField(max_length=1000, blank=True, null=True, auto_created=True)
    temp_link = models.ForeignKey('TempLink', on_delete=models.CASCADE, blank=True, null=True, to_field=id)

    def __str__(self):
        return self.name

    # Function to create permanent link
    def create_perm_link(self):
        if self.perm_link and not self.image:
            result = urllib.urlretrieve(self.image_url)
            self.image_file.save(
                os.path.basename(self.image_url),
                File(open(result[0]))
            )
            self.save()


# Create temporary link model
class TempLink(models.Model):
    link = models.URLField(max_length=1000, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    lifespan = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.link