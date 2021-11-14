from django.urls import path

from view_examples import views

app_name = 'view_examples'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello_2'),

    path('person/<int:id>/', views.person_detail, name='person_detail_1'),
    path('person2/<int:id>/', views.PersonView.as_view(), name='person_detail_2'),
    path('person3/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail_3'),

    path('create-person/', views.create_person, name='create_person_1'),
    path('create-person2/', views.PersonCreate.as_view(), name='create_person_2'),
    path('create-person3/', views.PersonCreateView.as_view(), name='create_person_3'),
]