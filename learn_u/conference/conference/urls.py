"""conference URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from accounts import views as accounts_views
from u2 import views

from accounts import views as accounts_views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homeward'),
    path('apply/', views.apply, name='new_presentation'),
    path('new_presentation_a/', views.new_presentation_a, name='new_presentation_a'),
    path('new_presentation_diff_formats/', views.new_presentation_diff_formats, name='new_presentation_diff_formats'),


    path('presentations/', views.presentations, name='all_presentations'),
    path('presentations_list_view/', views.presentations_list_view.as_view(), name='all_presentations_list_view'),
    path('foo/', views.foo, name='foo'),
    path('presentation/<int:presentation_id>/', views.presentation, name="presentation"),
    path('<int:pk>/presentation_detail_view/', views.presentation_detail_view.as_view(), name="presentation_detail_view"),

    path('signup', accounts_views.signup, name='signup'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('protected_view/', views.protected_view, name='protected_view'),

    # path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='accounts_login'),

    path('warning/', views.warning, name="warning"),

]
