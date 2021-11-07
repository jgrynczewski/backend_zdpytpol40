from django.shortcuts import render

TASKS = []

# Create your views here.
def register(request):

    task = request.POST.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'formapp_2/register.html',
        context={
            'tasks': TASKS,
        }
    )
