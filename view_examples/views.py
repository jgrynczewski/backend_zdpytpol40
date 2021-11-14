from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.views.generic import CreateView

from view_examples.models import Person
from view_examples.forms import PersonForm

# Widok funkcyjny
def hello(request):
    return HttpResponse("Hello, world!")


# Widok klasowy
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# Widok funkcyjny
def person_detail(request, id):
    p = get_object_or_404(Person, id=id)

    return render(
        request,
        'view_examples/person.html',
        context={
            'person': p,
        }
    )


# Widok klasowy
class PersonView(View):
    def get(self, request, id):
        p = get_object_or_404(Person, id=id)

        return render(
            request,
            'view_examples/person2.html',
            context={
                'person': p,
            }
        )


# Widok generyczny
class PersonDetailView(DetailView):
    model = Person


# Widok funkcyjny
def create_person(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('view_examples:hello')

    return render(
        request,
        'view_examples/person_create.html',
        context={
            "form": form,
        }
    )


# Widok klasowy
class PersonCreate(View):
    def get(self, request):
        form = PersonForm()

        return render(
            request,
            'view_examples/person_create2.html',
            context={
                "form": form
            }
        )

    def post(self, request):
        form = PersonForm(request.POST or None)
        if form.is_valid():
            form.save()

        return redirect('view_examples:hello')


# Widok generyczny
class PersonCreateView(CreateView):
    model = Person
    fields = "__all__"
