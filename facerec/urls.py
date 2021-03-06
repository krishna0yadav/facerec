"""facerec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import RedirectView
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home_view'),
    path('save-licence/', views.save_licence_view, name='save_licence_view'),
    path('verify/', views.verify_view, name='verify_view'),
    url('favicon.ico',RedirectView.as_view(url='/static/favicon.ico')),
    url('img1.png',RedirectView.as_view(url='/static/img1.png')),
    url('img2.jpg',RedirectView.as_view(url='/static/img2.jpg')),
]
