from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path('review',views.ReviewLabolatory.as_view(), name='review'),
    
]