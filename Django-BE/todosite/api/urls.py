from . import views
from django.urls import path

urlpatterns = [
    path('', views.apiOverview, name='API-overview'),
    path('tasks/', views.tasklist, name='API-Tasks-List'),
    path('task-detail/<str:pk>/', views.taskDetails, name='API-Tasks-List'),
    path('task-create/', views.taskCreate, name='API-Tasks-Create'),
    path('task-update/<str:pk>', views.taskUpdate, name='API-Tasks-Update'),
    path('task-delete/<str:pk>', views.taskDelete, name='API-Tasks-Delete'),
]