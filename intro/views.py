from django.shortcuts import HttpResponse


# Widok - funkcja/klasa, która przyjmuje żądanie http
# (http request), a zwraca odpowiedź http (http response)
def hello(request):  # -> HttpResponse
    return HttpResponse("Witaj, świecie")

# Ale to jest antywzorzec.
# W Django kod umieszczamy w aplikacjach Django.