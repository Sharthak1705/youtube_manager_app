from django import forms
from .models import Chai
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChaiForm(forms.ModelForm):
    class Meta:
        model = Chai
        fields = ['text', 'photo']
class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model =  User
        fields = ('username', 'email', 'password1', 'password2')

