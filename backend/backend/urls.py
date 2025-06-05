"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import login
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.register),
    path('api/login/', views.login),
    path('', views.dangnhap_page, name='dangnhap'),
    path('Khach/HomePage.html', views.khach_homepage, name='khach_homepage'),
    # gd đăng nhập cho vet và staff
    path('login/', views.login_view, name='login'),

    # gd Staff
    path('Nhanvien/login/', views.Nhanvien_homepage, name='Nhanvien_homepage'),
    path('Nhanvien/login/danhsachlichhen.html', views.danhsachlichhen, name='danhsachlichhen'),
    # path('Nhanvien/danhsachcutru.html', views.danhsachcutru, name='danhsachcutru'),
    # path('Nhanvien/formthemlichhen.html', views.formthemlichhen, name='formthemlichhen'),
    # path('Nhanvien/formthemlichcutru.html', views.formthemlichcutru, name='formthemlichcutru'),
    # path('Nhanvien/giaodienlich.html', views.lichhen, name='giaodienlich'),

    # gd Vet
]

