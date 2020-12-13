from django.db import models
from django.urls import reverse

# Model for project


class Project_post(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(default=2)

    def __str__(self):
        return self.name
    # Reverse url for project model

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

# Model for task


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    project_post = models.ForeignKey(  # foreign key for project model
        'Project_post', related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    # Reverse url for task model

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk, 'pk1': self.pk})
