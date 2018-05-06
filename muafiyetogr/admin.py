from django.contrib import admin
from muafiyetogr.models import Ogrenci , Okul , bolumler , Ders , Ogretimuyesi ,OnayFormu
# Register your models here.

class OgrenciView(admin.ModelAdmin):
	list_display = ('ogr_number','ogr_name', 'ogr_surname','ogr_okul','ogr_bolum','ogr_telefon','ogr_photo' ,'date_created')


class bolumlerView(admin.ModelAdmin):
	list_display = ('bolum_name','fakulte_name')

class DersView(admin.ModelAdmin):
	list_display = ('bolum','ders_kodu','ders_name','kredi_sayisi','icerik')


class OgretimuyesiView(admin.ModelAdmin):
	list_display = ('ogretim_uyesi_name','ogretim_uyesi_surname','unvan','bolum','email','ogretim_uyesi_telefon')


class OnayFormuView(admin.ModelAdmin):
	list_display = ('ders1','kredi_sayisi1','harf_notu1','ders2','OnayDurumu','harf_notu2')



admin.site.register(Okul)
admin.site.register(Ogrenci,OgrenciView)
admin.site.register(bolumler,bolumlerView)
admin.site.register(Ders,DersView)
admin.site.register(Ogretimuyesi,OgretimuyesiView)
admin.site.register(OnayFormu,OnayFormuView)