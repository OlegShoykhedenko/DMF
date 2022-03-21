from django.urls import path 
from . import views

urlpatterns = [
    # http://localhost:8000/api/task/getTasks/11/
    path('getTasks/<str:pk>/', views.TaskAPIView.as_view(), name='task-view'), 
    path('getFilteredTask', views.TaskFilterApiView.as_view(), name='task-filter-view')
]