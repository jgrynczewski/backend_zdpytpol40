from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def register(request):
    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            with open("tasks.txt", "a+") as f:
                f.write(f"{task}\n")

        return redirect('formapp_4:tasks-list')

    return render(
        request,
        'formapp_4/register.html'
    )


def tasks_list(request):

    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    return render(
        request,
        'formapp_4/tasks-list.html',
        context={
            'tasks': tasks,
        }
    )
