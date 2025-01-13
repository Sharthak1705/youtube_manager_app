from django import forms
from .models import Chai

class ChaiForm(forms.ModelForm):
    class Meta:
        model = Chai
        fields = ['text', 'photo']