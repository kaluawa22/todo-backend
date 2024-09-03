from django.contrib import admin
from .models import Todo
from .models import CheckListItem


# registering todo model to admin site
admin.site.register(Todo)
admin.site.register(CheckListItem)