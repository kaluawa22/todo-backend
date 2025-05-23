from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Todo,CheckListItem,Label
from .serializers import TodoSerializer,CheckListItemSerializer, LabelSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework import status








# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CheckListItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = LabelSerializer
    queryset = Label.objects.all()

    # Default method for creating a new label

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    # Custom action for associating an existing label with a todo

    @action(detail=True, methods=['post'], url_path='associate', url_name='associate')
    def associate_label_with_todo(self, request, pk=None):
        todo_id = pk  # The `todo_id` from the URL
        label_id = request.data.get("label_id")  # Extract label ID from the payload

        # Validate and fetch the instances
        try:
            todo = Todo.objects.get(id=todo_id)
            label = Label.objects.get(id=label_id)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
        except Label.DoesNotExist:
            return Response({"error": "Label not found"}, status=status.HTTP_404_NOT_FOUND)

        # Associate the label with the todo
        todo.labels.add(label)
        return Response({"message": "Label associated with Todo"}, status=status.HTTP_200_OK)



    def get_queryset(self):
        todo_id = self.kwargs.get('todo_pk')  # Retrieve `todo_id` from the URL kwargs
        if todo_id:
            # Filter labels associated with the specified `todo_id`
            return Label.objects.filter(todos__id=todo_id)
        # If no `todo_id` is provided, return all labels
        return Label.objects.all()