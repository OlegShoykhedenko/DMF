from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta: 
        model = Task
        fields = '__all__'