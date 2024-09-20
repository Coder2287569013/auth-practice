from django.urls import path
from auth_system import views

urlpatterns = [
    path('accounts/register/', views.register_user, name="register"),
    path('accounts/login/', views.login_user, name="login"),
]
