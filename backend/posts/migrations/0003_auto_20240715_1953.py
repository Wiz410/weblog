# Generated by Django 3.2.16 on 2024-07-15 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата публикации'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=1, verbose_name='тест поста'),
            preserve_default=False,
        ),
    ]
