from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import ManagerRegistrationForm,CustomerRegistrationForm
from .models import User

# Create your views here.
def signUp(request):
    return render(request,'accounts/signup.html')

def aboutPage(request):
    return render(request,'accounts/about.html')

class ManagerSignUpView(CreateView):
    model = User
    form_class = ManagerRegistrationForm
    template_name = "accounts/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_type"] = "manager" 
        return context
    
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('about')

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerRegistrationForm
    template_name = "accounts/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_type"] = "customer" 
        return context
    
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('about')