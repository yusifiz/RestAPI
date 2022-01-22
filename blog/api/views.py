from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.serializers import BlogSerializer
from blog.models import Blog
from rest_framework import status
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST',])
def blog_list_create(request):
    
    blogs = Blog.objects.all()
    serializers = BlogSerializer(blogs, many = True)
    return JsonResponse(serializers.data, safe=False) 
