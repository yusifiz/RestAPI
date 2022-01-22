from django.urls import path
from .views import blog_list_create

app_name = 'blog'

urlpatterns = [
    path('', blog_list_create, name='blog')
]