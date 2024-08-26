from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('student_data/', views.StudentData, name = 'StudentData'),
    path('student_api/', StudentAPI.as_view()),
    path('users/', UserAPI.as_view()),
    path('api/register/', UserRegistrationView.as_view(), name='user-register'),
    path('generic-student/', StudentGeneric.as_view()),
    path('generic-student/<id>/', StudentGenerics.as_view()),
    ]