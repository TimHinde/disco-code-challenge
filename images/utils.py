import sys

from .models import Image
from authapp.models import User, Subscription, Thumbnail
from PIL import Image as img
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import requests
import os


# Create util to take an image, determine the user's subscription, and create the appropriate thumbnails
def create_resized_image(image_id, user):
    obj = Image.objects.get(image_id=image_id)
    image = img.open(obj.image)
    subscription = user.subscription
    print(subscription)
    try:
        subscription_object = Subscription.objects.get(name=subscription)
    except Subscription.DoesNotExist:
        subscription_object = Subscription.objects.first()

    thumbnails = subscription_object.thumbnails.all()

    if thumbnails:
        thumbnail_array = []
        thumbnail_names = []
        for thumb in thumbnails:
            x_size = Thumbnail.objects.get(name=thumb.name).x_size
            y_size = Thumbnail.objects.get(name=thumb.name).y_size
            size = (x_size, y_size)
            thumbnail_array.append(size)
            thumbnail_names.append(thumb.name)

        thumb_dict = zip(thumbnail_names, thumbnail_array)
        for name, size in thumb_dict:
            # Resize the image
            new_img = image.resize(size)
            # Create a new name for the image
            new_name = ''.join([obj.name, '_', name])
            # Create a new image_id for the image
            new_image_id = ''.join([obj.image_id, '_', name])
            # Create a new user for the image
            ### Issue here - blocker - unable to get user assinged to image object.  Need to figure out how to get
            # the username passed correctly.
            new_user = user.username
            # Create the new image
            image = Image(name=new_name, image_id=new_image_id, image=new_img, user=new_user,
                          description=obj.description)
            image.save()
    else:
        print('No thumbnails found')

    # Return success message
    return 'success'
