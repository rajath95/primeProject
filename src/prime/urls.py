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
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.contrib import admin
from primeExchange.views import signup,login_view,logout_view,base,process_login,clientaccess
from primeExchange.views import reports,primeadmin,analytics,contact,xreport,monthly,tables
from primeExchange.views import delete_row,new_row,edit_row,dreports,delete_drow1,delete_drow2
from primeExchange.views import edit_drow1,edit_drow2,new_drow1,new_drow2,display,apilogin
from primeExchange.views import PrimeAppLoginAPI,api_process_login,nothing,addendum,PrimeAppLoginAPI2

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^primeDataExchangeAPI/$', include('primeExchange.urls')),
    url(r'^signup/$',signup),
    url(r'^process_login',process_login),
    url(r'^login/$',login_view,name="login"),
    url(r'^logout/$',logout_view,name="logout"),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^base/$',base),
    url(r'^clientaccess/$',clientaccess,name="clientaccess"),
    url(r'^reports/$',reports,name="reports"),
    url(r'^analytics/$',analytics,name="analytics"),
    url(r'^primeadmin/$',primeadmin,name="primeadmin"),
    url(r'^contact/$',contact,name="contact"),
    url(r'^base/reports/$',xreport),
    url(r'^filter/$',monthly),
    url(r'^tables/$',tables),
    url(r'^delete_row/(?P<id>[A-z0-9_]+)/$',delete_row),
    url(r'^edit_row/(?P<id>[A-z0-9_]+)/$',edit_row),
    url(r'^new_row/$',new_row),
    url(r'^dreports/$',dreports),
    url(r'^delete_drow1/(?P<id>[0-9_]+)/$',delete_drow1),
    url(r'^delete_drow2/(?P<id>[0-9_]+)/$',delete_drow2),
    url(r'^edit_drow1/(?P<id>[0-9_]+)/$',edit_drow1),
    url(r'^edit_drow2/(?P<id>[0-9_]+)/$',edit_drow2),
    url(r'^new_drow1/$',new_drow1),
    url(r'^new_drow2/$',new_drow2),
    url(r'^visual/(?P<id>[0-9]+)$',display),
    #url(r'^populatemastertable/$',populate),
    #url(r'^pop/$',populate),
    #url(r'^ret/$',retreive),
    url(r'^apilogin/$',apilogin),
    url(r'^api_process_login/$',api_process_login),
    url(r'^PrimeAppLoginAPI/$',PrimeAppLoginAPI),
    url(r'^PrimeAppLoginAPI2/$',PrimeAppLoginAPI2),
    url(r'^nothing/$',nothing),
    url(r'^adder/$',addendum),



]
