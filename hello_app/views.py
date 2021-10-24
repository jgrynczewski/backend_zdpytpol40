from django.shortcuts import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("<!DOCTYPE html><html><head></head><body><h3>Witaj, świecie!</h3></body></html>")