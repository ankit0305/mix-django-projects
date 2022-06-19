from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    name = widget=forms.TextInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "First Name"})
    class Meta:
        model = Contact
        fields = ('name', 'city', 'gender',)
