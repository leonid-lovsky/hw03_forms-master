from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Model

User = get_user_model()


class Group(Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='slug',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
    )

    def __str__(self) -> str:
        return f'{self.title}'


class Post(Model):
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Текст нового поста',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Имя автора',
        related_name='posts',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться пост',
        related_name='posts',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('-pub_date',)
