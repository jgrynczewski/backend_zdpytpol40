from django.urls import path

from formapp_2 import views

app_name = 'formapp_2'

urlpatterns = [
    path('register/', views.register, name='register')
]
