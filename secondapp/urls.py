from django.urls import path

from secondapp import views

urlpatterns = [
    path('adam/', views.hello_adam),
    path('ewa/', views.hello_ewa),

    path('time/', views.current_datetime),
    path('time2/', views.current_datetime_2),

    path('isitchristmas/', views.is_it_christmas),

    # Konwerter scieżki:
    # <typ_zmiennej:nazwa_zmiennej>
    path('<str:name>/', views.hello_name),
    # Dostępne konwertery:
    # str, int, slug, uuid, path
    # https://docs.djangoproject.com/en/3.2/topics/http/urls/

    # XSS vulnerability
    # path('<str:name>/', views.xss_vulnerability),
    # path('<str:name>/', views.xss_vulnerability_templates),

]