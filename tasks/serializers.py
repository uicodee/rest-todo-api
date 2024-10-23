from django.utils import timezone
from rest_framework import serializers
from .models import Task, Comment


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date', 'created_at', 'updated_at', 'user']

    # Validate due_date so it's not in the past
    def validate_due_date(self, value):
        if value and value < timezone.now().date():
            raise serializers.ValidationError("The due date cannot be in the past.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'task', 'user']
