from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages, auth
from myapp.models import User, Pet, Appointment, BeautyServiceHistory, HotelServiceHistory, MedicalHistory, NutritionPlan, VaccinationHistory
from django.db import connection
from django.http import JsonResponse




@api_view(['POST'])
def register(request):
    fullname = request.data.get('fullname')
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not fullname or not email or not password or not username:
        return Response({'error': 'Họ và tên, Username, Email và Password là bắt buộc'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email đã tồn tại'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username đã tồn tại'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user( #create
        email=email,
        username=username,
        password=password, # Hash mat khau trg db co san ham hash r 
        full_name=fullname,
        role='owner',
        phone='0123456789'
    )
    user.save()
    return Response({'message': 'Đăng ký thành công'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        # Tìm user theo email
        user = User.objects.get(email=email)
        if user:
            username = user.username
            print("User found:", username)
            if check_password(password, user.password):
                return Response({
                    'message': 'Đăng nhập thành công',
                }, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'Email không tồn tại'}, status=status.HTTP_401_UNAUTHORIZED)


def dangnhap_page(request):
    return render(request, 'Khach/DangNhap.html')


@login_required
def khach_homepage(request):
    return render(request, 'Khach/HomePage.html')


# tạo staff or bac sĩ 
def create_staff(username, password, role , full_name, email, phone):
    hashed_password = make_password(password)

    new_user = User.objects.create(
        username=username,
        password=hashed_password,
        role=role, 
        full_name=full_name,
        email=email,
        phone=phone,
    )
    
    print("Tạo staff thành công:", new_user)
    return new_user


def create_vet(username = 'vet1', password = '123', role = 'vet', full_name='Vet 1', email='', phone=''):
    hashed_password = make_password(password)

    new_user = User.objects.create(
        username=username,
        password=hashed_password,
        role=role, 
        full_name=full_name,
        email=email,
        phone=phone,
    )
    
    print("Tạo vet thành công:", new_user)
    return new_user

# Login cho bác sĩ và nhân viên 
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user and check_password(password, user.password):
            if user.role == "staff":
                # ✅ Chuyển UUID sang chuỗi
                request.session['user_id'] = str(user.user_id)
                request.session['username'] = user.username
                request.session['fullname'] = user.full_name
                request.session['email'] = user.email
                request.session['role'] = user.role

                return JsonResponse({
                    'success': True,
                    'redirect_url': get_redirect_url(user.role),
                    'message': 'Đăng nhập thành công',
                    'user': {
                        'fullname': user.full_name,
                        'username': user.username,
                        'role': user.role
                    }
                })
            else:
                return JsonResponse({'success': False, 'message': 'Chỉ nhân viên mới được đăng nhập'}, status=403)
        else:
            return JsonResponse({'success': False, 'message': 'Sai tài khoản hoặc mật khẩu'}, status=400)

    return render(request, "login.html")



def Nhanvien_homepage(request):
        return render(request, 'Nhanvien/login.html')

def danhsachlichhen(request):
    appointments = Appointment.objects.all()
    return render(request, 'Nhanvien/danhsachlichhen.html', {'appointments': appointments})

def formthemlichhen(request):
    return render(request, 'Nhanvien/formthemlichhen.html')

def formsualichhen(request): 
    appointments = Appointment.objects.all()
    return render(request, 'Nhanvien/formsualichhen.html', {'appointments': appointments})

def get_redirect_url(role):
    if role == 'staff':
        return '/Nhanvien/login/'
    elif role == 'vet':
        return '/admin/'

    return '/login'
