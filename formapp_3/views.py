from django.shortcuts import render
from django.shortcuts import redirect


TASKS = []

# Create your views here.
def register(request):
    if request.method =="POST":
        task = request.POST.get('task')
        if task:
            TASKS.append(task)

        return redirect('formapp_3:tasks-list')

    return render(
        request,
        'formapp_3/register.html',
    )


def tasks_list(request):
    return render(
        request,
        'formapp_3/tasks_list.html',
        context={
            'tasks': TASKS,
        }
    )
