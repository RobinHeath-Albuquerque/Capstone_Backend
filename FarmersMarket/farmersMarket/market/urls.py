from . import views
from django.urls import path

app_name = 'market'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='create_new_market')
]