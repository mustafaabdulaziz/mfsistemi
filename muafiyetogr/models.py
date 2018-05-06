from django.db import models
from django import forms

class Okul(models.Model):
	okul_name = models.CharField(max_length=100)

	def __str__(self):
		return self.okul_name



class Ogrenci(models.Model):
	
	ogr_name = models.CharField(max_length=50)
	ogr_surname = models.CharField(max_length=50)
	ogr_okul = models.CharField(max_length=100, choices=[(x.okul_name, x.okul_name) for x in Okul.objects.all()])
	ogr_bolum = models.CharField(max_length=100)
	ogr_number = models.CharField(max_length=9,unique=True)
	ogr_email = models.EmailField(max_length=100,unique=True)
	ogr_password = models.CharField(max_length=50)
	ogr_telefon = models.CharField(max_length=15)
	ogr_photo = models.ImageField(upload_to='ogr_resim')
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.ogr_number


class bolumler(models.Model):
	bolum_name = models.CharField(max_length=50)
	fakulte_name = models.CharField(max_length=50)

	def  __str__(self):
		return self.bolum_name



class Ders(models.Model):
	bolum = models.ForeignKey(bolumler,on_delete=models.CASCADE)
	ders_kodu = models.CharField(max_length=8)
	ders_name = models.CharField(max_length=50)
	kredi_sayisi = models.IntegerField()
	icerik = models.CharField(max_length=500)


	def __str__(self):
		return self.ders_name


class Ogretimuyesi(models.Model):
	ogretim_uyesi_name = models.CharField(max_length=50)
	ogretim_uyesi_surname = models.CharField(max_length=50)
	unvan = models.CharField(max_length=20)
	bolum = models.ForeignKey(bolumler,on_delete=models.CASCADE)
	email = models.EmailField(unique=True)
	ogretim_uyesi_telefon = models.CharField(max_length=15)
	ogretim_uyesi_password = models.CharField(max_length=50)

	def __str__(self):
		return self.ogretim_uyesi_name

Harf_notu_list = ["AA","BA","BB","CB","CC","DC","DD","FF","---"]
class OnayFormu(models.Model):
	ogrenci = models.ForeignKey(Ogrenci,on_delete=models.CASCADE)
	ders1 = models.CharField(max_length=75)
	kredi_sayisi1 = models. IntegerField()
	harf_notu1 = models.CharField(max_length=2,choices=[(x, x) for x in Harf_notu_list])
	ders2 = models.ForeignKey(Ders, on_delete=models.CASCADE)
	OnayDurumu = models.CharField(max_length=6,choices=[(x,x) for x in ["onay","Red","bekleniyor"]],default="bekleniyor")
	harf_notu2 = models.CharField(max_length=2,choices=[(x, x) for x in Harf_notu_list],default="---")
	ogretim_uyesi = models.ForeignKey(Ogretimuyesi,on_delete=models.CASCADE)


	def __str__(self):
		return self.ders1



