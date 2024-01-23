from django.contrib import admin
from .models import Todo


# registering todo model to admin site
admin.site.register(Todo)