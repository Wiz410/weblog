from django.db import models


class BlockModel(models.Model):
    """Абстрактная модель блокировки.
    Добавляет поле `is_block`.
    """
    is_block = models.BooleanField(
        'блокировка',
        default=False,
    )

    class Meta:
        abstract = True
