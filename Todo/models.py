from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Label(models.Model):
    # label title name
    title = models.CharField(max_length=50, unique=True)

    # returns label title which is used as model identifier 

    def __str__(self):
        return self.title


# Todo Model

class Todo(models.Model):
    # Todo item title
    title = models.CharField(max_length=200)
    # Todo item description 
    description = models.TextField()
    # Todo item completion boolean
    completed = models.BooleanField(default=False)
    # Todo item created at 
    created_at = models.DateField(auto_now_add=True)

    # todo item due date 
    due_date = models.DateField(null=True, blank=True)

    
    labels = models.ManyToManyField('Label', related_name='todos', blank=True)
   
   # Link specific Todo to User
    created_by = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)

    # returns title which is used as model identifier 
    def __str__(self):
        return self.title 
    


# Check List Item Model

class CheckListItem(models.Model):
    # Link specific Todo to CheckList Item
    todo = models.ForeignKey(Todo, related_name='checklist_items', on_delete=models.CASCADE)

    # Title of the checklist Item
    title = models.CharField(max_length=200)

    # Completion Status of the checklist Item
    completed = models.BooleanField(default=False)

    # returns title which is used as model identifier 
    def __str__(self):
        return self.title
    
