from todo.models import Task
from django.shortcuts import render

from todo.views import edit_task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('updated_at')
    
    completed_tasks = Task.objects.filter(is_completed=True)
    # print(completed_tasks)

    context = {
        'tasks' : tasks,
        'completed_tasks': completed_tasks,

    }
    return render(request, 'home.html', context)
