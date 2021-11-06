import random

from django.shortcuts import render


# Create your views here.
def toto_lotek(request):
    random_list = random.sample(range(1,50), 6)

    return render(
        request,
        'draw/toto-lotek.html',
        context={
            'random_list': random_list,
        }
    )
