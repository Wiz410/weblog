from django.contrib.auth.models import AbstractUser
from django.db import models


class WeBlogUser(AbstractUser):
    """Модель пользователя."""
    image = models.ImageField(
        upload_to='images/',
        blank=True,
    )
    is_block = models.BooleanField(
        'блокировка пользователя',
        default=False,
    )


class Follow(models.Model):
    """Модель подписок."""
    user = models.ForeignKey(
        WeBlogUser,
        on_delete=models.CASCADE,
        related_name='follow_user',
        verbose_name='кто подписан',
    )
    following = models.ForeignKey(
        WeBlogUser,
        on_delete=models.CASCADE,
        related_name='follow_following',
        verbose_name='на кого подписан',
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
