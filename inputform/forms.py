from django import forms

class Inputforms(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    age = forms.IntegerField(label="Age")
    email = forms.EmailField(label="Email", max_length=100)
    phone = forms.CharField(label="Phone", max_length=100)
    password = forms.CharField(label="Password", max_length=100)