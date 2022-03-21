from django.shortcuts import render
from django.http import HttpResponse
# from .models import Task
from my_todo import models, serializers
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User



# Create your views here.


class TaskAPIView(APIView): 
    model = models.Task
    queryset = models.Task.objects.all()
    serializers_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        tasks = self.queryset.all()
        serializer = self.serializers_class(tasks, many = True)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, pk):
        print(request.data.get('title'))
        task = models.Task.objects.create(
            title = request.data.get('title'),
            description = request.data.get('description'),
            user = request.user,
            due_date = request.data.get('due_date'),
            task_state = request.data.get('task_state')
        )
        serializer = self.serializers_class(task)
        return Response(data = serializer.data, status = status.HTTP_201_CREATED)

    def patch(self, request, pk): 
        try: 
            task = self.queryset.get(id = int(pk))
        except: 
            return Response(data = f"Task with id {pk} does not exist!")
        
        for key, value in request.data.items():
            if key in ['title', 'description']:
                setattr(task, key, value)
        
        task.save()
        serializer = self.serializers_class(task)
        return Response(data = serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, pk):
        try: 
            task = self.queryset.get(id = int(pk))
        except:
            return Response(data = f"Task with id {pk} does not exist!")

        task.delete()
        serializer = self.serializers_class(task)
        return Response(data = serializer.data, status = status.HTTP_200_OK)


class TaskFilterApiView(ListAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('id', 'title', 'description', 'user__username', 'user__id', 'task_state', 'due_date')