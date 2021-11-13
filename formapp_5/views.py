from django.shortcuts import render
from django.shortcuts import redirect

from formapp_5.models import Task


# Create your views here.
def register(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            Task.objects.create(name=task)

        return redirect("formapp_5:tasks-list")

    return render(
        request,
        'formapp_5/register.html',
    )


def tasks_list(request):
    tasks = Task.objects.all()

    return render(
        request,
        'formapp_5/tasks-list.html',
        context={
            'tasks': tasks,
        }
    )