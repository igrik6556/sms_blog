from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from uuslug import slugify

from django.utils.translation import ugettext as _


class Tag(models.Model):
    class Meta:
        db_table = 'Tag'
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    name = models.CharField(
        _('Tag name'),
        max_length=50,
        unique=True
    )
    slug = models.SlugField(_('Slug'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:tag_detail', kwargs={'tag_slug': self.slug})


class Category(models.Model):
    class Meta:
        db_table = 'Category'
        ordering = ['name']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    name = models.CharField(
        _('Category'),
        max_length=50,
        unique=True
    )
    slug = models.SlugField(_('Slug'))

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Category, self).save()

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'cat_slug': self.slug})


class Entry(models.Model):
    class Meta:
        db_table = 'Entry'
        ordering = ['-dt_add']
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')

    author = models.ForeignKey(User,
                               verbose_name=_('Entry author'),
                               related_name='entries',
                               on_delete=models.CASCADE,
                               blank=True)
    title = models.CharField(_('Entry title'), max_length=100)
    text = models.TextField(_('Entry text'))
    tag = models.ManyToManyField(Tag,
                                 verbose_name=_('Entry tags'),
                                 related_name='tag',
                                 blank=True)
    category = models.ForeignKey(Category,
                                 verbose_name=_('Entry Category'),
                                 related_name='category',
                                 on_delete=models.CASCADE)
    slug = models.SlugField(_('Slug'))
    dt_add = models.DateTimeField(_('Creation time'), auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:entry_detail', kwargs={'entry_slug': self.slug})


class Comment(models.Model):
    class Meta:
        db_table = 'Comment'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    user = models.CharField(_('Author of a commentary'),
                            max_length=150,
                            blank=True)
    email = models.EmailField(_('Email of user'),
                              blank=True,
                              null=True)
    site = models.URLField(_('Site address'),
                           blank=True,
                           null=True)
    text = models.TextField(_('Text of commentary'))
    dt = models.DateTimeField(_('Creation time'),
                              auto_now_add=True)
    entry = models.ForeignKey(Entry,
                              verbose_name=_('Comment for entry'),
                              related_name='entry',
                              on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.text[:30].strip(), self.user)

    def get_absolute_url(self):
        return reverse('blog:entry_detail', kwargs={'entry_slug': self.entry.slug}) + '#{}'.format(self.id)
