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
    serializer_class = TodoSerializer
    # queryset = Todo.objects.all()

    def get_queryset(self):
        # Only return todos for the authenticated user
        return Todo.objects.filter(created_by=self.request.user)


    # Automatically set the 'created_by' field to the currently authenticated user
    # when a new Todo is created via the API.
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


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

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @action(detail=True, methods=['post'], url_path='associate', url_name='associate')
    def associate_label_with_todo(self, request, todo_pk=None, pk=None):
        todo_id = todo_pk  # The parent lookup from the nested router
        label_id = pk      # The label's ID from the URL
        try:
            todo = Todo.objects.get(id=todo_id)
            label = Label.objects.get(id=label_id)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
        except Label.DoesNotExist:
            return Response({"error": "Label not found"}, status=status.HTTP_404_NOT_FOUND)

        todo.labels.add(label)
        return Response({"message": "Label associated with Todo"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='todos')
    def todos(self, request, pk=None):
        label = self.get_object()
        todos = label.todos.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        todo_id = self.kwargs.get('todo_pk')
        if todo_id:
            return Label.objects.filter(todos__id=todo_id)
        return Label.objects.all()