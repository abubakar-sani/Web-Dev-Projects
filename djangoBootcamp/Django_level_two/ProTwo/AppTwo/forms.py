from django import forms
from AppTwo.models import WaitingList

class NewUserForm(forms.ModelForm):
    """docstring for NewUser"""
    class Meta:
        model = WaitingList
        fields = '__all__'
