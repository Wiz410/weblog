from django.urls import path
from .views import (
    UserCreateView, UserLoginView, UserLogoutView, UserListView,
    UserUpdateView, UserPasswordChangeView
)

app_name = 'users'

urlpatterns = [
    path(
        'registration/',
        UserCreateView.as_view(),
        name='registration',
    ),
    path(
        'login/',
        UserLoginView.as_view(),
        name='login',
    ),
    path(
        'logout/',
        UserLogoutView.as_view(),
        name='logout',
    ),
    path(
        'settings/',
        UserUpdateView.as_view(),
        name='settings',
    ),
    path(
        'password_change/',
        UserPasswordChangeView.as_view(),
        name='password_change',
    ),
    path(
        '<slug:username>/',
        UserListView.as_view(),
        name='profile',
    ),
]
