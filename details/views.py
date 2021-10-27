from django.shortcuts import render, redirect
from django.views import View
from accounts.models import User
# Create your views here.

class Details(View):
   
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            usrs = User.objects.all()
            context = {
                'usrs' : usrs
            }
            return render(request,'details.html',context)
        else:
            return render(request,'login.html')


class Del(View):
   
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            obj = User.objects.get(id=request.POST.get('user_id'))
            obj.delete()
            usrs = User.objects.all()
            context = {
                'usrs' : usrs
            }
            return render(request,'details.html',context)
        else:
            return render(request,'login.html')


class Edit(View):
   
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:

            username = request.POST.get('username')
            email = request.POST.get('email')
            address = request.POST.get('address')
            user_id = request.POST.get('user_id')
            obj = User.objects.get(id=user_id)
            obj.username = username
            obj.email = email
            obj.address = address
            obj.save()
            usrs = User.objects.all()
            context = {
                'usrs' : usrs
            }
            return render(request,'details.html',context)
        else:
            return render(request,'login.html')
