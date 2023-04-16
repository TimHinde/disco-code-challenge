from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.UploadImageView.as_view(), name='upload_image'),
    path('view/', views.ImageView.as_view(), name='view_images'),
    path('view/link/<str:image_id>', views.ImageLinkView.as_view(), name='view_image_link'),
    ]
