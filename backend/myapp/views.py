from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum, Q, Value, Min, DecimalField
from django.db.models.functions import Coalesce
from datetime import datetime, time, timedelta, date
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
import calendar
from openpyxl import Workbook 
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, get_object_or_404
import json
from django.db import connection
from django.shortcuts import redirect
from django.conf import settings
import stripe
import traceback
from django.utils.timezone import now
import logging
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods
import io
from collections import defaultdict
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.db.models import Count
# xoa import core

# stripe.api_key = settings.STRIPE_SECRET_KEY
# logger = logging.getLogger(__name__)


@csrf_exempt
def khach_dangnhap_view(request):
    if request.method == 'GET':
        return render(request, 'Khach/DangNhap.html')

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            role_input = data.get('role')

            if not email or not password:
                return JsonResponse({'status': 'fail', 'message': 'Thiếu email hoặc mật khẩu.'}, status=400)

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT user_id, username, email, full_name, role
                    FROM users
                    WHERE email = %s AND role = %s
                    AND password = crypt(%s, password)
                """, [email, role_input, password])
                user = cursor.fetchone()

            if user:
                request.session['user_id'] = str(user[0])
                request.session['username'] = user[1]
                request.session['email'] = user[2]
                request.session['full_name'] = user[3]
                request.session['role'] = user[4]

                return JsonResponse({
                    'status': 'success',
                    'redirect_url': '/Khach',
                    'user': {
                        'email': user[2],
                        'fullname': user[3],
                        'username': user[1],
                        'role': user[4]
                    }
                })
            else:
                return JsonResponse({'status': 'fail', 'message': 'Sai email, mật khẩu hoặc quyền truy cập.'}, status=401)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
def khach_homepage(request):
    return render(request, 'Khach/HomePage.html')

def nhanvien_bacsi_login_view(request):
    if request.method == 'GET':
        # Giao diện dùng chung: login.html nằm ngoài thư mục Nhanvien/Bacsi
        return render(request, 'login.html')

    if request.method == 'POST':
        try:
            print("Request body:", request.body)  # Ghi log để debug

            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'status': 'fail', 'message': 'Dữ liệu không hợp lệ (không phải JSON).'}, status=400)

            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            role_input = data.get('role')

            if not username or not password:
                return JsonResponse({'status': 'fail', 'message': 'Thiếu username hoặc mật khẩu.'}, status=400)

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT user_id, username, email, full_name, role
                    FROM users
                    WHERE username = %s AND role = %s
                    AND password = crypt(%s, password)
                """, [username, role_input, password])
                user = cursor.fetchone()

            if user:
                # Lưu thông tin người dùng vào session
                request.session['user_id'] = str(user[0])
                request.session['username'] = user[1]
                request.session['email'] = user[2]
                request.session['full_name'] = user[3]
                request.session['role'] = user[4]

                return JsonResponse({
                    'status': 'success',
                    'redirect_url': get_redirect_url(user[4]),
                    'user': {
                        'email': user[2],
                        'fullname': user[3],
                        'username': user[1],
                        'role': user[4]
                    }
                })
            else:
                return JsonResponse({'status': 'fail', 'message': 'Sai email, mật khẩu hoặc quyền truy cập.'}, status=401)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def nhanvien_homepage(request):
    return render(request, 'Nhanvien/HomePage.html')

def bacsi_homepage(request):
    return render(request, 'Bacsi/danhsachbenhan.html')

def nhanvien_danhsachlichhen(request): 
    return render(request, 'Nhanvien/danhsachlichhen.html')

def get_redirect_url(role):
    if role == 'staff':
        return '/Nhanvien'
    elif role == 'vet':
        return '/Bacsi'
    return '/login'