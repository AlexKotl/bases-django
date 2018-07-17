from django import forms

class AddForm(forms.Form):
    name = forms.CharField(label='Base name', max_length=100)
