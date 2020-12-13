from .models import Project_post, Tasks  # imported both the models
from django.views.generic import (  # importing generic class based views
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# This view is for listing all projects at the Home page


class PostListView(ListView):
    model = Project_post
    template_name = 'project/home.html'
    context_object_name = 'posts'
    ordering = ['duration']

# This view renders the detail page of the project


class PostDetailView(DetailView):
    model = Project_post

# This view generates a form for creating the project


class PostCreateView(CreateView):
    model = Project_post
    fields = ['name', 'description', 'duration']

# This view generates a form to update an existing project


class PostUpdateView(UpdateView):
    model = Project_post
    fields = ['name', 'description', 'duration']

# This view is used to delete a existing project


class PostDeleteView(DeleteView):
    model = Project_post
    success_url = '/'

# This view creates a new task


class TaskCreateView(CreateView):
    model = Tasks
    fields = ['name', 'description', 'start_date', 'end_date', 'project_post']

# This view renders the detail page of the task


class TaskDetailView(DetailView):
    model = Tasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk1 = self.kwargs['pk1']
        context["task"] = Tasks.objects.filter(id=pk1).first()
        print(context)
        return context

# This view is used to render the update view form of the specific task


class TaskUpdateView(UpdateView):
    model = Tasks
    fields = ['name', 'description']

# About page


def about(request):
    return render(request, 'project/about.html', {'title': 'About'})
