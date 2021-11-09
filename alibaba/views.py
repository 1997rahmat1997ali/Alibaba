from django.shortcuts import render
from django.http import HttpResponse
from alibaba.forms import UserForm
from django.contrib import messages
from django import forms
from alibaba.models import userinfo
# Create your views here.

def new(r):
    return HttpResponse('testing')
def signupin(r):
    context = {}
    context["mismatch"] = 0
    return render(r,'signupin.html', context)
def sig(r):
    if r.method=='POST':
        pd = r.POST.get('pd')
        cpd = r.POST.get('cpd')
        if pd and cpd and pd != cpd:
            context = {}
            context["mismatch"] = 1
            context["message"] = 'Password and confirm password is not matching'
            return render(r,'signupin.html', context)
        _mutable = r.POST._mutable
        r.POST._mutable = True
        r.POST.pop('cpd')
        r.POST._mutable = _mutable
        form=UserForm(r.POST)
        if form.is_valid():
            try:
                form.save()
                return render(r,'signupin.html')
            except:
                return HttpResponse('form not saved')
        else:
            form=UserForm()
            context = {}
            context["mismatch"] = 1
            context["message"] = 'provide correct email'
            return render(r,'signupin.html',context)
def log_in(r):
    x=0
    u=userinfo.objects.all()
    if(r.method=='POST'):
        email=r.POST['email']
        pd=r.POST['pd']
        for i in u:
            if i.email==email:
                if i.pd==pd:
                    x=1
                    break
        if(x==1):
            return HttpResponse('welcome')
        else:
            context = {}
            context["mismatch"] = 1
            context["message"] = 'your email or password is incorrect'
            return render(r,'signupin.html',context)
    
    
    
