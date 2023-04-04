from todo.models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'todo_text', 'completed')
        read_only_fields = ["user"]


class MarkAsCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('completed',)

