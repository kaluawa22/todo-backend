from django.db import models

# Create your models here.



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

    # returns title which is used as model identifier 
    def __str__(self):
        return self.title 
    
