# serializers.py

from rest_framework import serializers
from .models import Todo, CheckListItem


class CheckListItemSerializer(serializers.ModelSerializer):
    # Include the check list items as nested data
    class Meta:
        model = CheckListItem
        fields = ['id', 'title', 'completed']

    

class TodoSerializer(serializers.ModelSerializer):
    checklist_items = CheckListItemSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'checklist_items']
        read_only_fields = ['id', 'created_at']

