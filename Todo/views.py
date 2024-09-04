from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Todo,CheckListItem
from .serializers import TodoSerializer,CheckListItemSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



# class CheckListItemViewSet(viewsets.ModelViewSet):
#     queryset = CheckListItem.objects.all()
#     serializer_class = CheckListItemSerializer



class CheckListItemViewSet(viewsets.ModelViewSet):
    serializer_class = CheckListItemSerializer

    def get_queryset(self):
        # Get the `todo_id` from the URL
        todo_id = self.kwargs['todo_pk']
        
        # Filter the checklist items by the `todo_id`
        return CheckListItem.objects.filter(todo_id=todo_id)
