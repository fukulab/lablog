from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("home",views.home,name="home"),
    path("<str:faculty>_<str:department>",views.facaluty_department,name="facaluty_department"),
    path("detail",views.detail,name='detail'),
   
]