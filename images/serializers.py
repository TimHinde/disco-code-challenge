from .models import Image
from rest_framework import serializers
from . import utils
# create image serializer
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'name',
            'image',
            'image_id',
            'user',
            'date',
            'description',
        ]
        read_only_fields = ['user', 'date']

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

    def create_thumbnails(self, validated_data, request):
        # use the validated data to create the required thumbnails for the users subscription plan with the create_resized_image function in utils
        user = request.user
        image_id = validated_data['image_id']
        utils.create_resized_image(image_id, user)
        return
        # Create the required thumbnails for the users subscription plan and save them to the database
        pass
