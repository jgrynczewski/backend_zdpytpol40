from django.urls import path
from django.urls import re_path
from django.urls import register_converter

from user_data import views
from user_data import converters

register_converter(converters.YearConverter, 'yyyy')

app_name = 'user_data'

urlpatterns = [
    path('test', views.test, name='test'),
    path(
        '<int:id>/passenger-detail/',
        views.passenger_detail,
        name='passenger-detail',
    ),  # build-in path converters
    re_path(
        'flights/(?P<year>2[0-1][0-9]{2})/$',
        views.flights_list,
        name='flights-list',
    ),  # regex
    path(
        'tasks/<yyyy:year>/',
        views.tasks_list,
        name='tasks-list',
    ),  # custom path converters
]