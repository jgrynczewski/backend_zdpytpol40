from django.urls import path

from form_examples import views

app_name = 'form_examples'

urlpatterns = [
    path("contact1/", views.contact1, name='contact1'),
    path("contact2/", views.contact2, name='contact2'),
]
