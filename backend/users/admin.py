from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import WeBlogUser, Follow


@admin.register(WeBlogUser)
class WeBlogUserAdmin(UserAdmin):
    """Регистрация модели пользователя в админ-зоне."""
    list_display = (
        'username',
        'email',
        'is_block',
        'is_staff',
    )
    list_editable = (
        'is_block',
    )
    list_filter = (
        'is_block',
        'is_staff',
    )
    search_fields = (
        'username',
        'email',
    )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Регистрация модели подписок в админ-зоне."""
    list_display = (
        'user',
        'following',
    )
    list_filter = (
        'following',
    )
    search_fields = (
        'user__username',
    )
