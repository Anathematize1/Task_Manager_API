from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = ('__all__')
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')


    def validate_deadline(self, value):
        return value
