from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import WeBlogUserCreationForm, WeBlogAuthenticationForm


User = get_user_model()


class WeBlogUserCreateView(CreateView):
    """Регистарция пользователя."""
    template_name = 'registration/registration_form.html'
    form_class = WeBlogUserCreationForm
    success_url = reverse_lazy('posts:list')


class WeBlogUserLoginView(LoginView):
    """Аутентификации пользователя."""
    form_class = WeBlogAuthenticationForm


class WeBlogUserLogoutView(LogoutView):
    """Выход из системы пользователя."""
    success_url = reverse_lazy('posts:list')