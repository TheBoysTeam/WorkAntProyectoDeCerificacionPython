"""WorkAnt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#from . import views
from FuncionesBasicas import views
#from FuncionesBasicas.views import login, registerempleado, registerempresa, recordsempleado, homeempleador, homeempleado, descripcionempleado, e404, forgotpassword,


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('registerempleado/', views.registerempleado),
    path('registerempresa/', views.registerempresa),
    path('recordsempleado/', views.recordsempleado),
    path('homeempleador/', views.homeempleador),
    path('descripcionempleado/', views.descripcionempleado),
    path('homeempleado/', views.homeempleado),
    path('forgotpassword/', views.forgotpassword),
    path('e404/', views.e404),
    path("loginEm",views.loginEm)
]
