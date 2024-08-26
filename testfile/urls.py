"""
URL configuration for testfile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from home.views import *
from university.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('univ/', univ, name = "univ"),
    path('delete_Uni/<id>', delete_Uni, name = "delete_Uni"),
    path('Update_Uni/<id>', Update_Uni, name = "Update_Uni"),
    path('login/', loginpage, name = "loginpage"),
    path('register/', registerpage, name = "registerpage"),
    path('students/', get_students, name = "get_students"),
    path('see_marks/<student_id>', see_marks, name = "see_marks"),
    path('index/', send_email, name = "index"),
    path('', include('university.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('login_djoser/', login_view, name = "login_view"),
    path('register_djoser/', register_view, name = "register_view"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns() 