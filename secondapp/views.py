from datetime import datetime

from markupsafe import escape

from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_adam(request):
    return render(
        request,
        'secondapp/adam.html',
    )


def hello_ewa(request):
    return HttpResponse("Witaj, Ewa!")


def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")


def xss_vulnerability(request, name):
    # XSS (Cross-Site Scripting)
    # Always sanitize data from user
    print(name)  # przed "odkarzeniem"
    name = escape(name)
    print(name)  # po "odkarzeniu"
    return HttpResponse(f"Witaj, {name}! &#x1F60A;")


def current_datetime(request):
    now = datetime.now()
    formatted_datetime = datetime.strftime(now, "%d.%m.%Y %H:%M:%S")
    return HttpResponse(f"Aktualny czas: {formatted_datetime}")


# Ale jak to zrobić z wykorzystaniem szablonu?
# Jak przekazać formatted_datetime do szablonu?
def current_datetime_2(request):
    now = datetime.now()
    formatted_datetime = datetime.strftime(now, "%d.%m.%Y %H:%M:%S")
    return render(
        request,
        'secondapp/time.html',
        context={
            "datetime": formatted_datetime,
        }
    )


def xss_vulnerability_templates(request, name):
    return render(
        request,
        'secondapp/hello.html',
        context={
            'name': name,
        }  # Django w funkcji render automatycznie
        # "odkarza" zmienne. Czyli dopóki używamy szablonów
        # nie musimy sami martwić się o podatność XSS
    )


def is_it_christmas(request):
    is_it_christmas = False

    now = datetime.now()
    if now.month == 12 and now.day == 24:
        is_it_christmas = True

    return render(
        request,
        'secondapp/isitchristmas.html',
        context={
            'christmas': is_it_christmas,
        }
    )


def is_it_monday(request):

    is_it_monday = False

    now = datetime.now()
    if now.weekday() ==0:
        is_it_monday = True

    return render(
        request,
        'secondapp/isitmonday.html',
        context={
            'monday': is_it_monday,
        }
    )
