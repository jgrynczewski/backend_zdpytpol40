from django.urls import path

from formapp_4 import views

app_name = 'formapp_4'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks-list/', views.tasks_list, name='tasks-list'),
]