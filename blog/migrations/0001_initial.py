# Generated by Django 3.1 on 2020-09-12 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Url')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('content', models.TextField(blank=True, verbose_name='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Изображение')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-created_at'],
            },
        ),
    ]
