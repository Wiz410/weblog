from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import BlockModel


class WeBlogUser(BlockModel, AbstractUser):
    """Модель пользователя."""
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.username


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

    def __str__(self) -> str:
        return (
            f'{self.user.username} подписан на {self.following.username}'
        )
