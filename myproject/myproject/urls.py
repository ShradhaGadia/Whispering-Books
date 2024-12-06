"""
URL configuration for myproject project.

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
from django.urls import path
from books.views import *

urlpatterns = [
    path('',home, name="home"),
    path('sales/',salespage,name="salespage"),
    path('addbook/',addbook,name="addbook"),
    path('addsale/<int:book_id>/',addsale,name="addsale"),
    path('updatebook/<int:book_id>/',updatebook,name="updatebook"),
    path('updatesale/<int:sale_id>/',updatesale,name="updatesale"),
    path('deletebook/<int:book_id>/',deletebook,name="deletebook"),
    path('deletesale/<int:sale_id>/',deletesale,name="deletesale"),
    path('recommend/',recommend,name="getRec"),
    path('admin/', admin.site.urls),
]
