from django.contrib import admin

from blog.models import Entry, Tag, Category, Comment
from blog.forms import EntryForm, TagForm, CategoryForm, CommentForm

from django.utils.translation import ugettext as _


class EntryAdmin(admin.ModelAdmin):
    form = EntryForm
    list_display = ['title', 'author', 'category', 'get_tags', 'count_comment', 'dt_add']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    def get_tags(self, obj):
        return ", ".join([t.name for t in obj.tag.all()])
    get_tags.short_description = _('Tags')

    def count_comment(self, obj):
        return obj.entry.all().count()
    count_comment.short_description = _('Number of comments')


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ['name', 'slug']


class TagAdmin(admin.ModelAdmin):
    form = TagForm
    list_display = ['name', 'slug']


class CommentAdmin(admin.ModelAdmin):
    form = CommentForm
    list_display = ['user', 'email', 'site', 'dt']

    def has_add_permission(self, request):
        return False

admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
