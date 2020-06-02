# from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',signUp,name="signup"),
    path('signup/manager', ManagerSignUpView.as_view(),name='manager_signup'),
    path('signup/customer', CustomerSignUpView.as_view(),name='customer_signup'),
    path('about/',aboutPage,name="about")
]
