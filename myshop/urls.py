from django.urls import path, re_path
from myshop import views

app_name = 'auth'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('sent/', views.activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('signin/', views.signin_view, name="signin"),
    path('logout/', views.logout_view, name="logout"),
    path('passforget/', views.password_forget_view, name="passforget"),
    path('passreset/', views.password_reset_view, name="passreset")
    ]