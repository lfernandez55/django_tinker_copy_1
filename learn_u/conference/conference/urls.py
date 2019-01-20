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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homeward'),
    path('apply/', views.apply, name='new_presentation'),
    path('presentations/', views.presentations, name='all_presentations'),
    path('presentations_list_view/', views.presentations_list_view.as_view(), name='all_presentations_list_view'),
    path('foo/', views.foo, name='foo'),
    path('presentation/<int:presentation_id>/', views.presentation, name="presentation"),
    path('<int:pk>/presentation_detail_view/', views.presentation_detail_view.as_view(), name="presentation_detail_view")
]
