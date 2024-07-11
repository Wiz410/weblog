from django.urls import path
from .views import WeBlogUserCreateView, WeBlogUserLoginView, WeBlogUserLogoutView

app_name = 'users'

urlpatterns = [
    path(
        'registration/',
        WeBlogUserCreateView.as_view(),
        name='registration',
    ),
    path(
        'login/',
        WeBlogUserLoginView.as_view(),
        name='login',
    ),
    path(
        'logout/',
        WeBlogUserLogoutView.as_view(),
        name='logout',
    ),
]
