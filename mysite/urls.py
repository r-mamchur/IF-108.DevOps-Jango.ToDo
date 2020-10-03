"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import url

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^todo/(?P<pk>\d+)/$', views.todo_detail, name='todo_detail'),
    re_path(r'^todo/new/$', views.todo_new, name='todo_new'),
    re_path(r'^todo/(?P<pk>[0-9]+)/edit/$', views.todo_edit, name='todo_edit'),
    path('', views.home, name='home'),
]
