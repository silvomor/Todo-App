from .models import Task
from django.http.response import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
# Create your views here.

@api_view(['GET', ])
def apiOverview(request, format=None):
    api_urls = {
    'List': '/api/tasks/',
    'Detail': '/api/task-detail/<str:pk>/',
    'Create': '/api/task-create/',
    'Update': '/api/task-update/<str:pk>/',
    'Delete': '/api/task-delete/<str:pk>/',
    }
    return Response(api_urls)


# GET ENTIRE LIST OF TASKS
@api_view(['GET', ])
def tasklist(request, format=None):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# GET A PARTICULAR TASK
@api_view(['GET', ])
def taskDetails(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


# CREATE NEW TASK
@api_view(['POST', ])
def taskCreate(request, format=None):
    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response({'Success': 'New task created!'})



# UPDATE A TASK
@api_view(['PUT', ])
def taskUpdate(request, pk, format=None):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'Success': 'Task Updated!'})
    return JsonResponse(serializer.errors, status=400)
 


# DELETE A TASK
@api_view(['DELETE', ])
def taskDelete(request, pk, format=None):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response({'Success': 'Task Deleted!'})