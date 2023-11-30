# p371
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, StrategyModel
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


class StrategyForm(ModelForm):
    class Meta:
        model = StrategyModel
        fields = ['category', 'title', 'comment', 'image1']
