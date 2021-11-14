from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse

from form_examples.models import Message
from form_examples.forms import ContactForm
from form_examples.forms import MessageForm


# Formularz HTML
def contact1(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        category = request.POST.get("category")
        subject = request.POST.get("subject")
        body = request.POST.get("body")

        if category not in ['question', 'other']:
            return HttpResponse("Niepoprawna wartość parametru category")

        Message.objects.create(
            name=name,
            email=email,
            category=category,
            subject=subject,
            body=body,
        )

        return redirect('form_examples:contact1')

    return render(
        request,
        'form_examples/contact1.html'
    )


# Formularz Django
def contact2(request):

    if request.method == "POST":
        form = ContactForm(request.POST)  # bound form
        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                category=data.get('category'),
                subject=data.get('subject'),
                body=data.get('body'),
            )

        return redirect('form_examples:contact2')

    form = ContactForm()  # unbound form
    return render(
        request,
        'form_examples/contact2.html',
        context={
            'form': form,
        }
    )


# Formularz modelu
def contact3(request):

    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('form_examples:contact3')

    return render(
        request,
        'form_examples/contact3.html',
        context={
            'form': form,
        }
    )
