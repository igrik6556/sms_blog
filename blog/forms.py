from django import forms
from pagedown.widgets import AdminPagedownWidget, PagedownWidget

from blog.models import Entry, Tag, Category, Comment

from django.utils.translation import ugettext as _


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('author', 'title', 'category', 'tag', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'size': 85}),
            'text': AdminPagedownWidget(),
            'author': forms.HiddenInput,
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email', 'site', 'text')
        widgets = {
            'user': forms.TextInput(attrs={
                'size': 40,
                'placeholder': _('Enter your name here (Not necessary)')
            }),
            'email': forms.EmailInput(attrs={
                'size': 40,
                'placeholder': _('Enter Email address here (Not necessary)')
            }),
            'site': forms.URLInput(attrs={
                'size': 40,
                'placeholder': _('Enter your site url here (Not necessary)')
            }),
            'text': forms.Textarea(attrs={
                'placeholder': _('Enter your commentary here (allow markdown syntax)')
            }),
        }


class CommentAuthorForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'user': forms.HiddenInput(),
            'email': forms.HiddenInput(),
            'site': forms.HiddenInput(),
            'text': forms.Textarea(attrs={
                'placeholder': _('Enter your commentary here (allow markdown syntax)')
            }),
        }
