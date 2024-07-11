from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from core.forms import BootstrapFormMixin

User = get_user_model()


class WeBlogUserCreationForm(BootstrapFormMixin, UserCreationForm):
    """Форма регистрации пользователя."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
        )


class WeBlogAuthenticationForm(BootstrapFormMixin, AuthenticationForm):
    """Форма aутентификации пользователя."""
    pass
