
from django.contrib import admin
from django.conf.urls import url,include
from muafiyetogr import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^signup$', views.Signup,name="Signup"),
    url(r'^$', views.Login,name="Login"),
]
