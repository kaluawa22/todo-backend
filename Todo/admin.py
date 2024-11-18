from django.contrib import admin
from .models import Todo
from .models import CheckListItem
from .models import Label




# Inline class to display Todos under a Label
class TodoInline(admin.TabularInline):
    model = Todo.labels.through  # This accesses the intermediary table for the ManyToMany relation
    extra = 0  # No extra blank forms for new Todos

# Admin class for Label with the TodoInline to display associated todos
class LabelAdmin(admin.ModelAdmin):
    inlines = [TodoInline]
    list_display = ('title',)  # Display the title of the label
    search_fields = ('title',)  # Add a search box to search by label title


# registering todo model to admin site
admin.site.register(Todo)
admin.site.register(CheckListItem)
admin.site.register(Label, LabelAdmin)