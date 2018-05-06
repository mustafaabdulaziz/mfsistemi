from django.contrib.auth.models import User
from django import forms
from .models import Ogrenci, Okul
	

class OgrenciForm(forms.ModelForm):
	ogr_okul= forms.CharField(widget=forms.Select(attrs={'class':'form-control' ,'id':'form-Okul-Adi'}, choices=[(x.okul_name, x.okul_name) for x in Okul.objects.all()]))
	ogr_bolum= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'bölüm adı','id':'form-bolumAdi'}))
	ogr_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'adı','id':'form-adi'}))
	ogr_surname= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'soyadı','id':'form-soyadi'}))
	ogr_number= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'öğrenci numarası','id':'form-ogrNo'}))
	ogr_email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'E-posta','id':'form-email'}))
	ogr_password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','id':'form-password'}))


	
	class Meta:
		model = Ogrenci
		fields = ['ogr_okul','ogr_bolum','ogr_name','ogr_surname','ogr_number','ogr_email','ogr_password']

	def clean_ogr_number(self):
			ogr_number = self.cleaned_data.get('ogr_number')
			for char in ogr_number :
				if char.isalpha():
					raise forms.ValidationError("öğrenci numarası sadece sayılardan oluşmalı")
			return ogr_number	

