from django import forms

class Memberform(forms.Form):
    name = forms.CharField(label="member name",max_length=250)
    age = forms.IntegerField(label="age")