from datetime import datetime
from django.shortcuts import render


# Create your views here.
def hello(request):
    return render(
        request,
        'review/hello.html',
    )


def is_it_monday(request):
    is_monday = False
    weekday = datetime.now().weekday()
    if weekday == 0:
        is_monday = True

    return render(
        request,
        'review/monday.html',
        context={
            "is_monday": is_monday,
        }
    )
