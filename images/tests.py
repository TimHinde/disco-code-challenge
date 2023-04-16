from django.test import TestCase
from authapp.models import User, Subscription, Thumbnail
from django.urls import reverse, reverse_lazy
from django.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Image


class TestViews(TestCase):

    # Test image upload view
    def test_upload_image_view(self):
        test_thumbnail = Thumbnail.objects.create(
            name='Test',
            x_size=100,
            y_size=100
        )
        # Create a test subscription
        test_subscription = Subscription.objects.create(
            name='Test',
            thumbnails=test_thumbnail,
            link_to_original=True,
            expiring_links=True
        )
        # Create a test user
        test_user = User.objects.create(
            username='testuser',
            password='testpassword',
            subscription=test_subscription
        )

        # Create a test client
        client = Client()

        # Log in the test user
        client.login(username='testuser', password='testpassword')

        # Create a test image
        test_image = SimpleUploadedFile(name='test_image.jpg', content=open('test_image.jpg', 'rb').read(),
                                        content_type='image/jpeg')

        # Post the test image to the upload image view
        response = client.post(reverse('upload_image'), {'image': test_image})

        # Assert that the image was uploaded
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(Image.objects.get().name, 'test_image.jpg')
        self.assertEqual(Image.objects.get().image_id, 'test_image.jpg')
        self.assertEqual(Image.objects.get().user, test_user)

        # Delete the test image
        Image.objects.get().delete()

        # Log out the test user
        client.logout()

        # Delete the test user
        test_user.delete()

    # Test image list view
    def test_image_list_view(self):
        test_thumbnail = Thumbnail.objects.create(
            name='Test',
            x_size=100,
            y_size=100
        )
        # Create a test subscription
        test_subscription = Subscription.objects.create(
            name='Test',
            thumbnails=test_thumbnail,
            link_to_original=True,
            expiring_links=True
        )
        # Create a test user
        test_user = User.objects.create(
            username='testuser',
            password='testpassword',
            subscription=test_subscription
        )

        # Create a test client
        client = Client()

        # Log in the test user
        client.login(username='testuser', password='testpassword')

        # Get the image list view
        response = client.get(reverse('image-list'))

        # Assert that the image list view was returned
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'images/image_list.html')

        # Log out the test user
        client.logout()

        # Delete the test user
        test_user.delete()

    # Test image resize util
    def test_image_resize_util(self):
        # Create a test thumbnail
        test_thumbnail = Thumbnail.objects.create(  # Create a test thumbnail
            name='Test',
            x_size=100,
            y_size=100
        )
        # Create a test subscription
        test_subscription = Subscription.objects.create(
            name='Test',
            thumbnails=test_thumbnail,
            link_to_original=True,
            expiring_links=True
        )
        # Create a test user
        test_user = User.objects.create(
            username='testuser',
            password='testpassword',
            subscription=test_subscription
        )
        # Create a test image
        test_image = SimpleUploadedFile(name='test_image.jpg', content=open('test_image.jpg', 'rb').read(),
                                        content_type='image/jpeg')
        # Create a test image object
        test_image_object = Image.objects.create(
            name='test_image.jpg',
            image_id='test_image.jpg',
            image=test_image,
            user=test_user
        )
        # Create a test client
        client = Client()

        # Log in the test user
        client.login(username='testuser', password='testpassword')

        # Get the image resize util
        response = client.get(reverse('image_resize_util', args=[test_image_object.image_id]))

        # Assert that the image resize util was returned
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'images/image_resize_util.html')

        # Log out the test user
        client.logout()

        # Delete the test user
        test_user.delete()

        # Delete the test image object
        test_image_object.delete()

        # Delete the test thumbnail
        test_thumbnail.delete()

        # Delete the test subscription
        test_subscription.delete()

    # Test image resize view
    def test_image_resize_view(self):
        pass