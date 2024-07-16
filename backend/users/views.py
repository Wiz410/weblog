from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse, reverse_lazy
from .forms import WeBlogUserCreationForm, WeBlogAuthenticationForm, UserForm, UserPasswordChangeForm

from core import constants

User = get_user_model()


class UserCreateView(CreateView):
    """Регистарция пользователя."""
    template_name = 'registration/registration_form.html'
    form_class = WeBlogUserCreationForm
    success_url = reverse_lazy('posts:list')


class UserLoginView(LoginView):
    """Вход в систему пользователя."""
    form_class = WeBlogAuthenticationForm


class UserLogoutView(LogoutView):
    """Выход из системы пользователя."""
    success_url = reverse_lazy('posts:list')


class UserListView(ListView):
    """Страница пользователя."""
    model = User
    template_name = 'users/user.html'
    paginate_by = constants.OBJECTS_PER_PAGE
    slug_url_kwarg = 'username'

    def get_queryset(self):
        self.author = get_object_or_404(User, username=self.kwargs['username'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.author
        return context


class UserUpdateView(UpdateView):
    """Страница настройки пользователя."""
    model = User
    template_name = 'users/settings.html'
    form_class = UserForm

    def get_object(self):
        return self.request.user

    def get_success_url(self) -> str:
        return reverse(
            'users:profile',
            kwargs={'username': self.request.user.username}
        )


class UserPasswordChangeView(PasswordChangeView):
    """Страница смены пароля."""
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:settings')
