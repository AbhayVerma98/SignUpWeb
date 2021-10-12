from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('post/', views.post, name='post'),
    path('home/', views.Home, name='home'),
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('details/', views.ShowUserData, name='details'),


    # Forget Password
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='Signup_App/change_password.html', success_url='/Signup_App/home/'), name='change_password'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='Signup_App/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='Signup_App/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Signup_App/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='Signup_App/password_reset_complete.html'),
         name='password_reset_complete'),

]

'''
'''
