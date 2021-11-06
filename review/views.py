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


def fruits(request):

    fruits = [
        'ananas',
        'banan',
        'mandarynka',
        'cytryna',
    ]

    passenger = {
        'id': 12345,
        'name': "Adam",
        'age': 20,
    }

    class Dog:
        def __init__(self, name):
            self.name = name

    dog = Dog("Azor")

    return render(
        request,
        'review/fruits.html',
        context={
            'fruits': fruits,
            'passenger': passenger,
            'dog': dog,
            'text': '<p style="color:red;">hello</p>',
        }
    )
