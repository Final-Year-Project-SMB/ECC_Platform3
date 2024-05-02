from django.urls import path

from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('home', views.home, name='home'),
      path('login', views.login, name='login'),
      path('engineer', views.engineer, name='engineer'),
      path('about', views.about, name='about'),
      path('account', views.account, name='account'),
      path('register', views.register, name='register'),
]