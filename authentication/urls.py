from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='authentication/login.html',
        authentication_form=LoginForm,
    ), name='login'),
    path('logout/', views.logout, name='logout'),
]