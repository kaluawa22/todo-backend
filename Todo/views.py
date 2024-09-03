from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Todo,CheckListItem
from .serializers import TodoSerializer,CheckListItemSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



class CheckListItemViewSet(viewsets.ModelViewSet):
    queryset = CheckListItem.objects.all()
    serializer_class = CheckListItemSerializer