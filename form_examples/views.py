from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse

from form_examples.models import Message


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
