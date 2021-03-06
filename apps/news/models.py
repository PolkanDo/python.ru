from django.conf import settings
from django.db import models
from django.db.models import QuerySet
from model_utils import Choices
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField


class ArticleQuerySet(QuerySet):

    def active(self):
        return self.filter(is_active=True)

    def featured(self):
        article = self.active().filter(is_featured=True).first()
        if not article:
            article = self.active().first()
        return article


class Article(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField('HashTag', blank=True, related_name='news')
    url = models.URLField('URL', blank=True, null=True)
    name = models.CharField('Заголовок', max_length=1024)
    description = models.TextField('Описание', blank=True)
    text = RichTextUploadingField('Текст', blank=True, default='')
    is_our = models.BooleanField('Наш пост?', default=False)
    published_at = models.DateTimeField('Дата публикации')
    section = models.CharField('Категория', max_length=100, blank=True)
    language = models.CharField('Язык', max_length=2, choices=Choices(('ru', '🇷🇺'), ('en', '🇬🇧')))
    source = models.CharField('Источник', max_length=32, choices=Choices('pythondigest', 'python.ru'))
    external_id = models.CharField('Внешний ID', max_length=32, unique=True, blank=True, null=True, editable=False)
    image = models.ImageField('Изображение', blank=True, upload_to='articles')
    is_active = models.BooleanField('Показывать', default=False)
    is_featured = models.BooleanField('Главная новость', default=False)

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_at', '-id']


class HashTag(models.Model):
    name = models.CharField('ХешТэг', max_length=100, unique=True)

    def __str__(self):
        return {self.name}
