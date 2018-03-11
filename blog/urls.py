from django.urls import path

from blog.views import (
    EntriesList, CategoryList, TagList, EntryDetail,
    CategoryDetail, TagDetail, CommentCreate
)


app_name = 'blog'
urlpatterns = [
    path('', EntriesList.as_view(), name='main'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('tag/', TagList.as_view(), name='tag_list'),
    path('comment_add/<str:entry_slug>/', CommentCreate.as_view(), name='comment_add'),
    path('category/<str:cat_slug>/', CategoryDetail.as_view(), name='category_detail'),
    path('tag/<str:tag_slug>/', TagDetail.as_view(), name='tag_detail'),
    path('<str:entry_slug>/', EntryDetail.as_view(), name='entry_detail'),
]
