from django import forms

class ContactSearchForm(forms.Form):
    name = forms.CharField(max_length=20)

