from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.serializers import BlogSerializer
from blog.models import Blog
from rest_framework import status
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST',])
def blog_list_create(request):
    if request.method == 'GET':
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (status=status.HTTP_400_BAD_REQUEST, message = {'message': 'Bad request message'})


@api_view(['GET','PUT','DELETE'])
def blog_detail(request,pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    