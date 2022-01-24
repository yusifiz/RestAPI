from unicodedata import name
from django.urls import path
from .views import blog_list_create, blog_detail

app_name = 'blog'

urlpatterns = [
    path('', blog_list_create, name='blog'),
    path('<int:pk>', blog_detail, name='blog')
]