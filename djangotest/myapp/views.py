from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render , redirect
from django.views import View
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request, 'home.html')
    
    
class AboutView(View):
    def get(self,request,username):
        return render(request, 'about.html')    
    
class UserRegisterView(View):
    form_class=UserRegistrationForm
    template_name='form_register.html'
    def dispatch(self, request, *args: Any, **kwargs: Any):
        if request.user.is_authenticated:
            return redirect('myapp:home')
        return super().dispatch(request, *args, **kwargs)
    
    
    def get(self,request):
        context= {'form':self.form_class}
        return render(request, self.template_name , context)
    
    
    def post(self,request):
        form=self.form_class(request.POST)    
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'] ,email=cd['email'] , password=cd['password1'])
            messages.success(request,'you registered succcesfully','success')
            return redirect('myapp:home')
        return render(request, self.template_name ,{'form':form})