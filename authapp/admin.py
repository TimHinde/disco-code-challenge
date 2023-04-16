from django.contrib import admin
from .models import User, Subscription, Thumbnail

admin.site.register(User)
admin.site.register(Subscription)
admin.site.register(Thumbnail)
