from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetConfirmView, PasswordResetDoneView
from accounts.views import user_page
from django.urls import path
from django.contrib.auth import authenticate, views as auth_view
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user/', views.user_page, name="user"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_order/<str:pk>/', views.create_order, name="create_order"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('reset_password/', auth_view.PasswordResetView.as_view(
        template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_done.html"), name="password_reset_complete")

]
