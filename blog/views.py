from django.urls import reverse
from django.contrib.sites.models import Site
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from blog.models import Entry, Tag, Category
from blog.forms import CommentForm, CommentAuthorForm

from django.utils.translation import ugettext as _


class EntryDetail(DetailView):
    model = Entry
    slug_url_kwarg = 'entry_slug'
    template_name = 'blog/entry_detail.html'

    def get_context_data(self, **kwargs):
        entry = Entry.objects.get(slug=self.kwargs['entry_slug'])
        context = super(EntryDetail, self).get_context_data(**kwargs)
        context['comments'] = entry.entry.all()
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentAuthorForm
        else:
            context['comment_form'] = CommentForm
        return context


class EntriesList(ListView):
    model = Entry
    template_name = 'blog/entries_list.html'
    context_object_name = 'entries'


class TagList(ListView):
    model = Tag
    template_name = 'blog/cat_tag_list.html'

    def get_context_data(self, **kwargs):
        context = super(TagList, self).get_context_data(**kwargs)
        context['values_list'] = Tag.objects.all()
        context['url'] = 'blog:tag_detail'
        context['title'] = _('Blog - List of tags')
        context['header'] = _('Tags')
        return context


class CategoryList(ListView):
    model = Category
    template_name = 'blog/cat_tag_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['values_list'] = Category.objects.all()
        context['url'] = 'blog:category_detail'
        context['title'] = _('Blog - List of categories')
        context['header'] = _('Categories')
        return context


class CategoryDetail(DetailView):
    model = Category
    slug_url_kwarg = 'cat_slug'
    template_name = 'blog/cat_tag_detail.html'

    def get_context_data(self, **kwargs):
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['values_list'] = cat.category.all()
        context['url'] = 'blog:entry_detail'
        context['title'] = _('Blog - Category: {}'.format(cat))
        context['header'] = _('Category: {}'.format(cat))
        return context


class TagDetail(DetailView):
    model = Tag
    slug_url_kwarg = 'tag_slug'
    template_name = 'blog/cat_tag_detail.html'

    def get_context_data(self, **kwargs):
        tag = Tag.objects.get(slug=self.kwargs['tag_slug'])
        context = super(TagDetail, self).get_context_data(**kwargs)
        context['values_list'] = tag.tag.all()
        context['url'] = 'blog:entry_detail'
        context['title'] = _('Blog - Tag: {}'.format(tag))
        context['header'] = _('Tag: {}'.format(tag))
        return context


class CommentCreate(SuccessMessageMixin, CreateView):
    form_class = CommentForm
    template_name = 'blog/_comment_form.html'
    success_message = _("Comment successfully added!")

    def get_success_url(self):
        self.success_url = reverse('blog:entry_detail',
                                   kwargs={
                                       'entry_slug': self.object.entry.slug,
                                   })
        return self.success_url

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            if not form.instance.user:
                form.instance.user = _('Anonymous')
        else:
            form.instance.user = self.request.user.username
            form.instance.email = self.request.user.email
            form.instance.site = '{}://{}'.format(self.request.scheme,
                                                  Site.objects.get_current().domain)
        form.instance.entry_id = Entry.objects.get(slug=self.kwargs['entry_slug']).id
        return super(CommentCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['entry'] = Entry.objects.get(slug=self.kwargs['entry_slug'])
        return context
