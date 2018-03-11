from django.contrib import admin
from django.urls import path, include
from django.utils.functional import curry
from django.views.defaults import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

handler404 = curry(page_not_found, template_name='errors/404.html')
