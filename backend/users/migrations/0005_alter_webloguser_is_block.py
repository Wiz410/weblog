# Generated by Django 3.2.16 on 2024-07-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webloguser',
            name='is_block',
            field=models.BooleanField(default=False, verbose_name='блокировка пользователя'),
        ),
    ]
