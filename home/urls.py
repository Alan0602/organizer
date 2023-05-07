from django.urls import path
from . import views

urlpatterns = [
 path('',views.home, name='home'),
 path('main_page/',views.home, name='main_page'),
]
