from Vol.models import  Compagnie
from django import forms

class compagnieForm(forms.ModelForm):
   class Meta:
    model = Compagnie
    fields = ['nom','logo']


    