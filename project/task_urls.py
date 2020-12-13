from django.urls import path  # imported path
from . import views
from .views import (  # imported task views to make url patterns for all of them
    TaskDetailView,
    TaskUpdateView,
    TaskCreateView,
)

# url patterns for task views
urlpatterns = [
    # url for update view of task
    path('task/<int:pk1>/', TaskDetailView.as_view(), name='task-detail'),
    # url pattern for new project creation
    path('new/', TaskCreateView.as_view(), name='task-create'),
    # url for update view of project
    path('task/update/', TaskUpdateView.as_view(), name='task-update'),
]
