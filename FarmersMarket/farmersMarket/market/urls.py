from . import views
from django.urls import path
from django.contrib import admin

app_name = 'market'
urlpatterns = [
    path('', views.index, name='home'),
    path('registration/sign_up/', views.sign_up, name="sign_up")
]