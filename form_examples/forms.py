from django import forms

from form_examples.models import Message


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


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

