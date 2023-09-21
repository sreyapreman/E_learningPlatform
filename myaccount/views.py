from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View,CreateView,FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import formset_factory
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


from myaccount.forms import RegisterForm,LoginForm
from myaccount.decorators import signin_required
    

@signin_required
def log_out_view(request, *args, **kwargs):
    logout(request)
    messages.success(request,'logout successfully')
    return redirect('login')

class RegistrationView(CreateView):
    model=User
    template_name="register.html"
    form_class=RegisterForm
    success_url=reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request,"Account has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create an account")
        return super().form_invalid(form)
    
class LoginView(View):
    model=User
    template_name="login.html"
    form_class=LoginForm

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                print(usr)
                messages.success(request,"login successfully")
                return redirect("index")
            messages.error(request,"login failed")
        return render(request,self.template_name,{"form":form})