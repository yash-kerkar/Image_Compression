from django import forms

class HomeForm(forms.Form):
    img = forms.ImageField()
    cluster = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '150'}))