from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from formapp_6.models import Task


# Create your views here.
def register(request):
    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            Task.objects.create(name=task)

        return redirect("formapp_6:tasks-list")

    return render(
        request,
        'formapp_6/register.html',
    )


def tasks_list(request):
    tasks = Task.objects.all()

    return render(
        request,
        'formapp_6/tasks-list.html',
        context={
            'tasks': tasks,
        }
    )


def update(request, id):
    # try:
    #     task = Task.objects.get(id=id)
    # except ObjectDoesNotExist:
    #     raise Http404
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        modified_task_name = request.POST.get('task')
        if modified_task_name:
            # Task.objects.filter(id=id).update(name=modified_task_name)  # - tak

            task.name = modified_task_name  # - lub tak
            task.save()

        return redirect('formapp_6:tasks-list')

    return render(
        request,
        'formapp_6/update.html',
        context={
            'task': task,
        }
    )
