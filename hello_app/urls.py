from django.urls import path

from hello_app import views

urlpatterns = [
    path('pierwsze', views.hello),
    path('drugie', views.hello_2),
    path('trzecie', views.hello_3),

    path('adam', views.hello_adam),
    path('ewa', views.hello_ewa),

    # Konwerter scieżki:
    # <typ_zmiennej:nazwa_zmiennej>
    path('<str:name>', views.hello_name),
]