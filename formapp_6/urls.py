from django.urls import path

from formapp_6 import views

app_name = 'formapp_6'

urlpatterns = [
    path('register/', views.register, name='register'),  # C
    path('tasks-list/', views.tasks_list, name='tasks-list'),  # R
    path('update/<int:id>/', views.update, name='update'),  # U
    path('delete/<int:id>/', views.delete, name='delete'),  # D
]
