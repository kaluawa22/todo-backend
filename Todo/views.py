from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Todo,CheckListItem,Label
from .serializers import TodoSerializer,CheckListItemSerializer, LabelSerializer

from rest_framework.response import Response
from rest_framework import status


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer





#  Ensure your CheckListItemViewSet correctly handles the todo_id and its data:
class CheckListItemViewSet(viewsets.ModelViewSet):
    serializer_class = CheckListItemSerializer

    def get_queryset(self):
        todo_id = self.kwargs['todo_pk']
        return CheckListItem.objects.filter(todo_id=todo_id)

    def create(self, request, *args, **kwargs):
        todo_id = self.kwargs['todo_pk']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(todo_id=todo_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class LabelViewSet(viewsets.ModelViewSet):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    # def get_queryset(self):
    #     todo_id = self.kwargs.get('todo_pk')  # Retrieve `todo_id` from the URL
    #     # Filter labels associated with the specified `todo_id`
    #     return Label.objects.filter(todos__id=todo_id)  

