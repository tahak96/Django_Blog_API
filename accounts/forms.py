from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Manager,Customer

class ManagerRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Enter email address", required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    def save(self):
        user = super().save(commit=False)
        user.is_Manager = True
        user.save()
        manager = Manager.objects.create(user=user)
        return user

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Enter email address", required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    def save(self):
        user = super().save(commit=False)
        user.is_Customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user