from django.urls import path

from formapp_6 import views

app_name = 'formapp_6'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks-list/', views.tasks_list, name='tasks-list'),
]
