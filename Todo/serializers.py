# serializers.py

from rest_framework import serializers
from .models import Todo, CheckListItem, Label


class CheckListItemSerializer(serializers.ModelSerializer):
    # Include the check list items as nested data
    class Meta:
        model = CheckListItem
        fields = ['id', 'title', 'completed']

class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = ['id', 'title']

class TodoSerializer(serializers.ModelSerializer):
    checklist_items = CheckListItemSerializer(many=True, read_only=True)
    
    labels = LabelSerializer(many=True, required=False, read_only=True)

     # Make description optional
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'checklist_items', 'labels']
        read_only_fields = ['id', 'created_at']



