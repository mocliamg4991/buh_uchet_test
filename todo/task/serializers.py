from .models import Task
from rest_framework import serializers

class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('__all__')
    
    

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id','title','deadline','executed')

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'text','deadline')
        extra_kwargs = {
            'owner': {'read_only': True}
        }

    def create(self, validated_data):
        validated_data["owner"] = self.context.get('request').user
        return super().create(validated_data)