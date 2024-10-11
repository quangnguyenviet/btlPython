from django.urls import path
from . import views  

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<str:username>', views.profile, name='profile'),

    path('', views.home, name='home'),
]
