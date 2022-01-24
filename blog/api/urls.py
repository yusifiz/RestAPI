from unicodedata import name
from django.urls import path
from .views import BlogListAPIView ,BlogDetailAPIView
# from .views import blog_list_create, blog_detail

app_name = 'blog'

# urlpatterns = [
#     path('', blog_list_create, name='blog'),
#     path('<int:pk>', blog_detail, name='blog')
# ]

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blog'),
    path('<int:pk>', BlogDetailAPIView.as_view(), name='blog')
]