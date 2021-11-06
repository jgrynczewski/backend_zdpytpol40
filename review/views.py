from datetime import datetime
from django.shortcuts import render


# Create your views here.
def hello(request):
    return render(
        request,
        'review/hello.html',
    )


def is_it_monday(request):

    weekday = datetime.now().weekday()
    is_monday = True if weekday == 0 else False

    return render(
        request,
        'review/monday.html',
        context={
            "is_monday": is_monday,
        }
    )
