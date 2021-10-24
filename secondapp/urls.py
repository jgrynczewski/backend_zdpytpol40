from django.urls import path

from secondapp import views

urlpatterns = [
    path('adam/', views.hello_adam),
    path('ewa', views.hello_ewa),

    # Konwerter scieżki:
    # <typ_zmiennej:nazwa_zmiennej>
    path('<str:name>', views.hello_name),
]