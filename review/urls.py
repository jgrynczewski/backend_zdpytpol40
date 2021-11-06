from django.urls import path

from review import views


urlpatterns = [
    path('hello/', views.hello),
    path('isitmonday', views.is_it_monday),
]