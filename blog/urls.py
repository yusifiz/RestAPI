from .views import blog
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog')
]