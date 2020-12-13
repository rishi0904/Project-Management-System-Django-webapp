from django.urls import path  # imported path
from django.urls import include  # imported to include task_urls.py
from . import views
from .views import (  # imported project views to make url patterns for all of them
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

# url patterns for project views
urlpatterns = [
    # List view of projects at home page
    path('', PostListView.as_view(), name='project-home'),

    path('about/', views.about, name='project-about'),  # About page url

    path('project/<int:pk>/', PostDetailView.as_view(),
         name='project-detail'),  # Detail page url for project

    # url pattern for new project creation
    path('project/new/', PostCreateView.as_view(), name='project-create'),

    path('project/<int:pk>/update/',
         PostUpdateView.as_view(), name='project-update'),  # url for update view of project

    path('project/<int:pk>/delete',
         PostDeleteView.as_view(), name='project-delete'),  # url for delete view of a project

    # These url patterns are for the task views the are included here from task_urls.py
    path('project/<int:pk>/', include('project.task_urls')),
]
