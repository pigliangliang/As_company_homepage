from django import forms

class Addform(forms.Form):
    s = forms.IntegerField()
    h = forms.IntegerField()

