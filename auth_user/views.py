from django.shortcuts import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

# ciasteczka
def cookies(request):
    print(dir(request))
    print(request.COOKIES)

    res = HttpResponse("Ok")
    res.set_cookie("ciasteczko1", 5)
    res.set_cookie("ciasteczko2", 10, max_age=1000)

    return res


# sesja
def session(request):
    print(request.COOKIES)
    # print(dir(request))
    # print(dir(request.session))
    print(request.session.session_key)

    sessionId = request.session._get_or_create_session_key()
    print(sessionId)


    num_visit = request.session.get('num_visit', 0) + 1
    request.session['num_visit'] = num_visit

    res = HttpResponse(f"Ok, liczba wizyt: {num_visit}")
    res.set_cookie("sessionId", sessionId)

    return res


def auth(request):

    users = User.objects.all()
    print(users)

    # Tworzenie nowego użytkownika (rejestracja)
    # adam = User.objects.create(username='adam', password='tajne')

    # adam = User.objects.get(username='adam')
    # adam.set_password('abcABC123!@#')
    # adam.save()

    # Uwierzytelnianie (sprawdzanie poświadczeń)
    # result = authenticate(username='adam', password='abcABC123!@#')
    # print(result)

    # Logowanie
    # login(request, user=result)

    # Wylogowanie
    # logout(request)

    return render(
        request,
        'auth_user/auth.html'
    )
