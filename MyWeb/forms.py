from django import forms

from .models import Numsum


class PostForm(forms.Form):
    Number_of_Costomers = forms.IntegerField()
    Number_of_Receptionists = forms.IntegerField()
    Min_serving_time_of_the_receptionits = forms.IntegerField()
    Max_serving_time_of_the_receptionits = forms.IntegerField()
    MinCustonArrivalTime = forms.IntegerField()
    MaxCustonArrivalTime = forms.IntegerField()
    CustomerSwitchTime = forms.FloatField()
