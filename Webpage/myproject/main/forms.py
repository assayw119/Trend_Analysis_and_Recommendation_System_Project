from django import forms

class RestaurantForm(forms.Form):
    sido = forms.CharField()
    sigugun = forms.CharField()
    img = forms.IntegerField()
    food = forms.CharField()

# class RestaurantForm:
#     def __init__(self, sido, sigugun, img, food):
#         self.sido = sido
#         self.sigugun = sigugun
#         self.img = img
#         self.food = food