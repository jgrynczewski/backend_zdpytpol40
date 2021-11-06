from django.urls import path

from links import views

app_name = 'links'

urlpatterns = [
    path('pierwsza/', views.first, name="first"),
    path('druga/', views.second, name="second"),
    path('trzecia/<str:foo>', views.third, name="third"),
]
