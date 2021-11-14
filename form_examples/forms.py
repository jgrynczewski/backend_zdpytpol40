from django import forms


class ContactForm(forms.Form):

    choices = [
        ("", "--------------"),
        ("question", "Pytanie"),
        ("other", "Inne")
    ]

    name = forms.CharField()
    email = forms.EmailField()
    category = forms.ChoiceField(
        choices=choices
    )
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
