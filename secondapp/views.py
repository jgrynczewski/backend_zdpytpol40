from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_adam(request):
    return render(
        request,
        'adam.html',
    )


def hello_ewa(request):
    return HttpResponse("Witaj, Ewa!")


def hello_name(request, name):
    return HttpResponse(f"Witaj {name}")
