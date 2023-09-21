from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import redirect

def instructor_required(func):
    def wrapper(request,*args, **kwargs):
        if not request.user.role == 'instructor':
            messages.error(request,"You have no permission this oparation")
            return redirect('login')
        return func(request,*args, **kwargs)
    return wrapper

def signin_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"please login")
            return redirect('login')
        return fn(request,*args, **kwargs)
    return wrapper
