from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from blog.models import Entry, Category, Tag


class Test(TestCase):

    def tests(self):
        c = Client()
        User.objects.create_superuser(username='Admin', email='test@mail.com', password='123superpass')
        c.login(username="Admin", password='123superpass')

        response = c.post(reverse('admin:blog_category_add'), data={
            'name': 'First category',
        })
        self.assertEqual(response.status_code, 302)
        category = Category.objects.get(name='First category')
        self.assertTrue(category)

        response = c.post(reverse('admin:blog_tag_add'), data={
            'name': 'First tag',
        })
        self.assertEqual(response.status_code, 302)
        tag = Tag.objects.get(name='First tag')
        self.assertTrue(tag)

        response = c.post(reverse('admin:blog_entry_add'), data={
            'author': User.objects.get(username='Admin').id,
            'title': 'Entry 1',
            'category': Category.objects.get(name='First category').id,
            'tag': Tag.objects.get(name='First tag').id,
            'text': 'Some entry text',
        })
        self.assertEqual(response.status_code, 302)
        entry = Entry.objects.get(title='Entry 1')
        self.assertTrue(entry)

        response = c.get(reverse('blog:category_detail', kwargs={
            'cat_slug': category.slug
        }))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('blog:tag_detail', kwargs={
            'tag_slug': tag.slug
        }))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('blog:entry_detail', kwargs={
            'entry_slug': entry.slug
        }))
        self.assertEqual(response.status_code, 200)
