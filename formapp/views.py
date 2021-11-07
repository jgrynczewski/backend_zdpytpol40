from django.shortcuts import render

TASKS = []


# Create your views here.
def register(request):

    task = request.GET.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'formapp/register.html',
        context={
            "tasks": TASKS,
        }
    )
