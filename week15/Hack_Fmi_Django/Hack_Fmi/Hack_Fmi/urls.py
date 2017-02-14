"""Hack_Fmi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Hack_Fmi.user import views as user_views
from Hack_Fmi.courses.views import courses_table

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^course/', include('Hack_Fmi.courses.urls')),
    url(r'^lecture/', include('Hack_Fmi.lectures.urls')),
    url(r'^$', courses_table, name="index"),
    url(r'^register/$', user_views.register, name='register'),
    url(r'^login/$', user_views.login, name='login'),
    url(r'^profile/', user_views.profile, name='profile'),
]
