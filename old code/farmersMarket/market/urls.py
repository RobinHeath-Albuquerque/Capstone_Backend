from . import views
from django.urls import path



app_name = 'market'
urlpatterns = [
  path('', views.index, name="index"),
  path('', views.home, name='home')

]