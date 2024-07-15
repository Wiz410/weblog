from django.contrib import admin
from .models import Tag, Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Регистрация модели тегов в админ-зоне."""
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Регистрация модели постов в админ-зоне."""
    pass
