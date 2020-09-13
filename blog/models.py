from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Url', max_length=100, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('Url', max_length=100, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Url', max_length=100, unique=True)
    author = models.CharField('Автор', max_length=100)
    content = models.TextField('', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    photo = models.ImageField('Изображение', upload_to='photos/%Y/%m/%d', blank=True)
    views = models.PositiveIntegerField('Кол-во просмотров', default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.CharField('Текст комментария', max_length=600)
    author = models.CharField('Автор', max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.post} was commented by {self.author}'