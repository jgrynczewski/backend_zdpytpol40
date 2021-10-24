from django.shortcuts import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("Witaj, świecie!")


def hello_2(request):
    return HttpResponse("<!DOCTYPE html><html><head></head><body><h3>Witaj, świecie!</h3></body></html>")


def hello_adam(request):
    return HttpResponse("Witaj, Adam!")


def hello_ewa(request):
    return HttpResponse("Witaj, Ewa!")


def hello_name(request, name):
    return HttpResponse(f"Witaj {name}")
