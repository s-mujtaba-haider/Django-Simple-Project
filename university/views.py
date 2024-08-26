from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics
import requests

# from django.contrib.auth import get_user_model

# User = get_user_model()

class UserAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all().order_by('id')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            user = User.objects.get(id = request.data['id'])
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            user = User.objects.get(id = request.data['id'])
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        try:
            id = request.GET.get('id')
            user = User.objects.get(id = id)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class UserRegistrationView(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    
    permission_classes = [AllowAny]
    
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
    
class StudentGenerics(generics.UpdateAPIView, generics.DestroyAPIView):
    
    permission_classes = [AllowAny]
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


class StudentAPI(APIView):
    
    permission_classes = [AllowAny]
    
    def get(self, request):
        student_objs = Student.objects.all().order_by('id')
        stu_serializer = StudentSerializer(student_objs, many = True)
        return Response({'student' : stu_serializer.data})

    def post(self, request):
        stu_serializer = StudentSerializer(data = request.data)
        
        if not stu_serializer.is_valid():
            print(stu_serializer.errors)
            return Response({'status' : 403, 'errors' : stu_serializer.errors})
            
        stu_serializer.save()
        return Response({'student' : stu_serializer.data})
    
    def put(self, request):
        try:
            student_objs = Student.objects.get(id = request.data['id'])
            stu_serializer = StudentSerializer(student_objs, data = request.data, partial = False)
            
            if not stu_serializer.is_valid():
                print(stu_serializer.errors)
                return Response({'status' : 403, 'errors' : stu_serializer.errors})
            
            stu_serializer.save()
            return Response({'student' : stu_serializer.data})
        
        except Exception as e:
            print(e)
            return Response({'status' : 403, 'message' : 'Invalid Id'})
            
    
    def patch(self, request):
        try:
            student_objs = Student.objects.get(id = request.data['id'])
            stu_serializer = StudentSerializer(student_objs, data = request.data, partial = True)
            
            if not stu_serializer.is_valid():
                print(stu_serializer.errors)
                return Response({'status' : 403, 'errors' : stu_serializer.errors})
            
            stu_serializer.save()
            return Response({'student' : stu_serializer.data})
        
        except Exception as e:
            print(e)
            return Response({'status' : 403, 'message' : 'Invalid Id'})
    
    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_objs = Student.objects.get(id = id)
            student_objs.delete()
            
            return Response({'status' : 200, 'message' : 'Deleted'})
        
        except Exception as e:
            print(e)
            return Response({'status' : 403, 'message' : 'Invalid Id'})
            
            
@api_view()
def StudentData(request):
    student_objs = Student.objects.all()
    stu_serializer = StudentSerializer(student_objs, many = True)
    
    uni_objs = uni.objects.all()
    uni_serializer = UniSerializer(uni_objs, many = True)
    
    dep_objs = Department.objects.all()
    dep_serializer = DepSerializer(dep_objs, many = True)
    
    sub_objs = Subject_Marks.objects.all()
    sub_serializer = Subject_Marks_Serializer(sub_objs, many = True)
    
    rep_objs = ReportCard.objects.all()
    rep_serializer = ReportCard_Serializer(rep_objs, many = True)
    
    return Response({'University' : uni_serializer.data, 'Department' : dep_serializer.data , 'student' : stu_serializer.data , 'Report_Card' : rep_serializer.data})

# Create your views here.
def univ(request):
    
    if request.method == "POST":
        data = request.POST
        uni_name = data.get('university_name')
        uni_year = data.get('make_year')
        uni_logo = request.FILES['logo']
        
        uni.objects.create(
            uni_name = uni_name,
            uni_year = uni_year,
            uni_logo = uni_logo,
        )
        
        
    
    queryset = uni.objects.all()
    context = {"uni":queryset}

    return render(request, "uni.html", context)
        
        
def delete_Uni(request, id):
    
    queryset = uni.objects.get(id=id)
    queryset.delete()
    
    return redirect('/univ')
    
def Update_Uni(request, id):
    queryset = uni.objects.get(id=id)
    context = {"uni":queryset}
    
    if request.method == "POST":
        data = request.POST
        uni_name = data.get('university_name')
        uni_year = data.get('make_year')
        uni_logo = request.FILES.get('logo')
        
        queryset.uni_name = uni_name
        queryset.uni_year = uni_year
        
        if uni_logo:
            queryset.uni_logo = uni_logo
    
        queryset.save()
        return redirect('/univ')
        
    
    context = {"uni":queryset}

    return render(request, "update_uni.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        login_url = "http://127.0.0.1:8000//auth/token/login/"
        response = requests.post(login_url, data={"username": username, "password": password})

        if response.status_code == 200:
            token = response.json().get('auth_token')
            request.session['auth_token'] = token
            return redirect('/univ/')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Call the Djoser registration API
        registration_url = "http://127.0.0.1:8000/auth/users/"
        response = requests.post(registration_url, data={
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "password": password
        })

        if response.status_code == 201:
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('loginpage')
        else:
            # Show all error messages from the response
            error_data = response.json()
            for key, value in error_data.items():
                messages.error(request, f"{key}: {', '.join(value)}")

    return render(request, "register.html")

def loginpage(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('/univ/')
            
    return render(request, "login.html")

def registerpage(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "Username ALready Exists")
            return redirect('/register/')
            
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        
        user.set_password(password)
        user.save()
        
        messages.info(request, "Account Created Successfully")
        return redirect('/login/')
        
    return render(request, "register.html")

def get_students(request):
    
    
    queryset = Student.objects.all()

    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search)
        )
    
    paginator = Paginator(queryset, 20)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'report/students.html', {'queryset' : page_obj})

from .seed import generate_report_card
def see_marks(request, student_id):
    queryset = Subject_Marks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    
    return render(request, 'report/see_marks.html', {'queryset' : queryset, 'total_marks' : total_marks })

    
    
    