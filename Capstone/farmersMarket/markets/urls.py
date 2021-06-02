from . import views
from django.urls import path

app_name = 'markets'
urlpatterns = [
    path('', views.index, name ='index')
]