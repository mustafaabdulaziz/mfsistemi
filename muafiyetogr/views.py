from django.shortcuts import render , redirect
from .models import Okul
from django.http import HttpResponse
from .forms import OgrenciForm
from django import forms


def Signup(request):
	all_okul = Okul.objects.all()
	form = OgrenciForm(request.POST or None)
	if form.is_valid():
		form.save()
		#instance = form.save(commit=False)
#		instance.save()
	return render(request,"signup.html",{"okuls":all_okul , "form":form})

def Login(request):
	return render(request,"login.html",{})


