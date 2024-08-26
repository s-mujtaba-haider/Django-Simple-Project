from django.shortcuts import render, redirect
from django.http import HttpResponse 
from university.seed import *
from home.utils import *
# Create your views here.

def home(request):
    pass
    
    
def send_email(request):
    send_email_to_client()
    return redirect('/index/')
    