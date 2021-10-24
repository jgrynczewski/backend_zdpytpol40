from django.urls import path

from hello_app import views

urlpatterns = [
    path('pierwsze', views.hello),
    path('drugie', views.hello_2),
    path('trzecie', views.hello_3),

    path('welcome', views.welcome),
]