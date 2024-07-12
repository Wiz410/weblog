from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
                'placeholder': 'Имя пользовятеля',
            })
        self.fields['email'].widget.attrs.update({
                'placeholder': 'Почта',
            })
        self.fields['password1'].widget.attrs.update({
                'placeholder': 'Пароль',
            })
        self.fields['password2'].widget.attrs.update({
                'placeholder': 'Подтверждение пароля',
            })


class WeBlogAuthenticationForm(BootstrapFormMixin, AuthenticationForm):
    """Форма aутентификации пользователя."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
                'placeholder': 'Имя пользовятеля',
            })
        self.fields['password'].widget.attrs.update({
                'placeholder': 'Пароль',
            })


class UserForm(BootstrapFormMixin, forms.ModelForm):
    """Форма настройки пользователя."""
    class Meta:
        model = User
        fields = (
            'image',
            'username',
            'first_name',
            'last_name',
            'email',
        )
