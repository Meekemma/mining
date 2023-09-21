from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/<str:referral_code>/<str:pk>/', views.register_with_referrer_view, name='register_with_referrer'),
    path('login/', views.login_page, name= "login"),
    path('logout/', views.logoutUser, name= "logout"),
    path('register/', views.register_page, name = "register"),
    

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="mining/password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="mining/password_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="mining/password_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="mining/password_complete.html"), name='password_reset_complete'),


    path('', views.index, name='home'),
    path('contact/', views.contact_info, name='contact'),
    path('about/', views.about_info, name='about'),
    path('diversity_info/', views.diversity_info, name='diversity'),
    path('privacy/', views.privacy_info, name='privacy'),
    path('sponsoring/', views.sponsoring_info, name='sponsoring'),
    path('terms/', views.term_info, name='terms'),
    path('profile/', views.profile_settings, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deposit/', views.deposit_info, name='deposit'),
    path('create_payment/<str:pk>/', views.create_payment, name='create_payment'),
    path('invoice/<str:pk>/', views.track_invoice, name='invoice'),
    path('receive/', views.receive_payment, name='receive'),
    path('withdrawal/', views.withdrawal_info, name='withdrawal'),
    path('support/', views.support_page, name='support'),
    path('plans/', views.plan_view, name='plans'),
    path('share/', views.share_view, name='share'),
    path('referral/', views.referal_view, name='referral'),
    path('transaction/', views.transactionPage, name='transaction'),
]