from .models import Image
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status, views
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from . import utils


# Create API view to return list of all images belonging to user by ensuring that the user is authenticated
@method_decorator(csrf_exempt, name='dispatch')
class ImageView(views.APIView):
    # This view should be accessible only for authenticated users.
    permission_classes = (permissions.IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ImageView, self).dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def get(self, request, format=None):
        """Return a list of all images belonging to the user."""
        images = Image.objects.filter(user=request.user)
        # Created this to list the names of the users images to be quickly displayed in the frontend
        names = [image.name for image in images]
        ids = [image.image_id for image in images]
        # Return the names of the images belonging to the user for now
        return Response({'names': names, 'id': ids}, status=status.HTTP_200_OK)
        # return Response({'names': names, 'images': images}, status=status.HTTP_200_OK)


# Create API for authenticated users to upload images
@method_decorator(csrf_exempt, name='dispatch')
class UploadImageView(views.APIView):
    # This view should be accessible only for authenticated users.
    permission_classes = (permissions.IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UploadImageView, self).dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        # Get the user who uploaded the image from session id
        user = request.user

        # create name variable
        if not request.data['name']:
            name = request.data['file'].name
        else:
            name = request.data['name']

        # Check if image already exists
        if Image.objects.filter(name=name, user=user).exists():
            return Response({'status': 'Image already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create varaibles for the image file and the file path and save with django media storage
        file = request.data['file']
        file_name = file.name
        media_storage = FileSystemStorage()
        file_path = media_storage.save(file_name, file)

        # Create the ImageModel instance with the required fields
        image_id = ''.join([str(file_name), '_', str(request.user)])  # function to generate unique image id

        # Create description variable
        if not request.data['description']:
            description = 'No description'
        else:
            description = request.data['description']

        image = Image(name=file_name, image=file_path, image_id=image_id, user=user, description=description)

        image.save()

        utils.create_resized_image(image_id, user)

        return Response({'status': 'success'})


# Create API view to return link to image
@method_decorator(csrf_exempt, name='dispatch')
class ImageLinkView(views.APIView):
    # This view should be accessible only for authenticated users.
    permission_classes = (permissions.IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ImageLinkView, self).dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def get(self, request, image_id, format=None):
        """Return a link to the image."""
        # Get the image id from the request
        image_name = request.GET.get('name')
        user = request.user
        # Filter to get the image object
        target_image = Image.objects.filter(user=user, image_id=image_id)
        # Get the image file path
        image_path = target_image.get().image.url
        # Return the image path
        return Response({'image_path': image_path}, status=status.HTTP_200_OK)

        # target_image = Image.objects.filter(user=user, name=image_name)
        # # Get the image file path
        #
        # image_path = target_image.get().image.url
        # # Return the image path
        # return Response({'image_path': image_path}, status=status.HTTP_200_OK)
