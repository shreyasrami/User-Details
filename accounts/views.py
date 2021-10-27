from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.views import View
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

class Register(View):
   
    def get(self,request,*args,**kwargs):
        return render(request,'register.html')


    def post(self,request,*args,**kwargs):
             
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 == password2 :
            if User.objects.filter(username__exact=username).exists() : 
                err = 'Username already taken'
                message_class = 'alert-danger'
                    
            elif User.objects.filter(email__exact=email).exists() :
                err = 'Email already taken'
                message_class = 'alert-danger'
                    
            else:
                username = request.POST.get('username')
                email = request.POST.get('email')
                address = request.POST.get('address')
                user = User.objects.create(username=username,email=email,password=make_password(password1),address=address)
                user.save()
                context = {
                    'username'  : username,
                    'message'   : "User Successfully Registered",
                    'message_class' : 'alert-success'
                    
                }
                return render(request,'login.html',context)
                
        else:
            err = 'Passwords does not match'
            message_class = 'alert-danger'
        
        context = {
            'message' : err,
            'message_class' : message_class
            
        }
        
        return render(request,'register.html',context)
        

class Login(View):

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('details/')
        else:
            return render(request,'login.html')

    
    def post(self,request,*args,**kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('details/')

        else:
            context = {
                'message' : 'Invalid Email or Password',
                'message_class' : 'alert-danger'
            }
            return render(request,'login.html',context)

        
class Logout(View):
    def get(self,request,*args,**kwargs):
        auth.logout(request)
        return redirect('/')

