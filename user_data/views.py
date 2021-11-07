from django.shortcuts import render

# Create your views here.
def test(request):
    return render(
        request,
        'user_data/test.html',
    )


def passenger_detail(request, id):
    return render(
        request,
        'user_data/passenger_detail.html',
        context={
            'passenger_id': id,
        }
    )


def flights_list(request, year):
    return render(
        request,
        'user_data/flights_list.html',
        context={
            'year': int(year),  # year jest stringiem
        }
    )


def tasks_list(request, year):
    return render(
        request,
        'user_data/tasks_list.html',
        context={
            'year': year,  # year już jest intem (YearConverter)
        }
    )