"""prime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from primeExchange import views
from primeExchange.forms import LoginForm
from django.contrib.auth import views as view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^primeDataExchangeAPI/$', include('primeExchange.urls')), 
    url(r'^$',views.home),
    url(r'^login/$',view.login,{'template_name':'primeExchange/login.html','authentication_form':LoginForm}),
    #url(r'^logout/$', views.logout, {'next_page': '/login'}),  
]
