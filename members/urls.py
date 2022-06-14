from django.urls import path
from . import views

urlpatterns = [
    path('Signup/', views.signup,name="signup"),
    path('Signin/', views.signin,name="signin"),
    path('Signout/', views.signout,name="signout"),

]