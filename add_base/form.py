from django import forms

class AddForm(forms.Form):
    address = forms.CharField(label='Address')
    contacts = forms.CharField(widget=forms.Textarea)
    #pos_x = forms.CharField()
    #pos_y = forms.CharField()
    name = forms.CharField(label='Base name', max_length=100)
    price = forms.DecimalField()
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
