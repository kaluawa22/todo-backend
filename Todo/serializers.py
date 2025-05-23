# serializers.py

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Todo, CheckListItem, Label
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

# Serializer for account signup 
class UserSerializer(ModelSerializer):
    # add validator to enforce unique email

    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This email is already in use."
            )
        ])
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user




# Serializer for Checklist items
class CheckListItemSerializer(serializers.ModelSerializer):
    # Include the check list items as nested data
    class Meta:
        model = CheckListItem
        fields = ['id', 'title', 'completed']
        


# Serializer for Label items
class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = ['id', 'title']


# Ser9alizer for Todo items
class TodoSerializer(serializers.ModelSerializer):
    checklist_items = CheckListItemSerializer(many=True, read_only=True)
    
    labels = LabelSerializer(many=True, required=False, read_only=True)

     # Make description optional
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'checklist_items', 'labels']
        read_only_fields = ['id', 'created_at']



