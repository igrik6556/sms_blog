# Generated by Django 2.0.3 on 2018-03-11 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Категория')),
                ('slug', models.SlugField(verbose_name='Слаг')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'db_table': 'Category',
                'verbose_name': 'Категория',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=150, verbose_name='Автор комментария')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Адрес электронной почты пользователя')),
                ('site', models.URLField(blank=True, null=True, verbose_name='Адрес сайта')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('dt', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name_plural': 'Комментарии',
                'db_table': 'Comment',
                'verbose_name': 'Комментарий',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок записи')),
                ('text', models.TextField(verbose_name='Текст записи')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('dt_add', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL, verbose_name='Автор записи')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blog.Category', verbose_name='Категория записи')),
            ],
            options={
                'verbose_name_plural': 'Записи',
                'db_table': 'Entry',
                'verbose_name': 'Запись',
                'ordering': ['-dt_add'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя тэга')),
                ('slug', models.SlugField(verbose_name='Слаг')),
            ],
            options={
                'verbose_name_plural': 'Тэги',
                'db_table': 'Tag',
                'verbose_name': 'Тэг',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tag', to='blog.Tag', verbose_name='Тэги записи'),
        ),
        migrations.AddField(
            model_name='comment',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry', to='blog.Entry', verbose_name='Комментарий к записи'),
        ),
    ]
