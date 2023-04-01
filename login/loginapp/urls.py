from django.urls import path
from . import views

urlpatterns = [
    path('',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("home",views.home,name="home"),
    path("pulldown1",views.pulldown1,name="pulldown1"),
    path("faculty_and_department/<str:name>",views.enginiering_detail,name="dennki"),
]