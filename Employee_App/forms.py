from django import forms

class Registration(forms.Form):
    Number = forms.IntegerField(max_length=2)