from django.forms import forms

__author__ = 'DarKnight'

class ContactForm(forms.Form):
    subject = forms.CharField();
    email = forms.EmailField(required=False);
    message = forms.CharField();
