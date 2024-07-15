from django.db import models
from django.conf import settings
from core import constants
from core.models import BlockModel


class TitleModel(models.Model):
    """Абстрактная модель названия.
    Добавляет поле `title`.
    """
    title = models.CharField(
        'Название',
        max_length=constants.MODELS_MAX_LENGTH,
    )

    class Meta:
        abstract = True


class Tag(TitleModel):
    slug = models.SlugField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'slug'],
                name='unique_tag'
            )
        ]
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.title


class Post(TitleModel, BlockModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор поста',
    )
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag
    )
    text = models.TextField(
        'тест поста',
        blank=True,
    )
    is_published = models.DateTimeField(
        'дата публикации',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.title
