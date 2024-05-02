"""
URL configuration for lokiproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home,name='home page'),
    path('ADDWEBPAGE',views.add_w,name='Add product page'),
    path('go',views.result,name='view page'),
    path('VIEWWEBPAGE',views.view_w,name='View products page'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('welcome', views.welcome, name='welcome page'),
    path('addCart',views.addCart,name="add cart"),
    path('shopping',views.shop,name='shop'),
    path('viewCart',views.viewCart,name='view cart'),
    path('payment',views.payment,name='view cart'),
    path('profile',views.profile,name='view profile')
]
