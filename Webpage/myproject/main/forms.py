from django import forms

class RestaurantForm(forms.Form):
    sido = forms.CharField()
    sigugun = forms.CharField()
    dong = forms.CharField()
    img = forms.IntegerField()
    food = forms.CharField()