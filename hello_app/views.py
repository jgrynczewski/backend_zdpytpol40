from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("Witaj, świecie!")


def hello_2(request):
    return HttpResponse("<!DOCTYPE html><html><head></head><body><h3>Witaj, świecie!</h3></body></html>")


def hello_3(request):
    return render(
        request,
        'hello_app/hello.html'
    )


def welcome(request):
    return render(
        request,
        'hello_app/welcome.html'
    )

