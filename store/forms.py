from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'輸入使用者名稱'}))
  email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'輸入電子郵件'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'輸入密碼'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'確認密碼'}))
  class Meta:
    model = User
    fields=["username","email",'password1',"password2"]