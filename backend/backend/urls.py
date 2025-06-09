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
from myapp.views import khach_dangnhap_view, khach_homepage, nhanvien_bacsi_login_view
from myapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.khach_dangnhap_view, name='dangnhap'),
    path('Khach/', views.khach_homepage, name='khach_homepage'),
    path('employee_login/', views.nhanvien_bacsi_login_view, name='employee_login'),
    path('Bacsi/', views.bacsi_homepage, name='bacsi_homepage'),
    path('Nhanvien/', views.nhanvien_homepage, name='nhanvien_homepage'),
    path('Lichhen/', views.nhanvien_danhsachlichhen, name='danhsachlichhen'),

]

