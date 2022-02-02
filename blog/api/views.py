from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.serializers import BlogSerializer, UserSerializer
from blog.models import Blog, User
from rest_framework import status
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import permissions, generics


class BlogListAPIView(APIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    
    
    def get(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (status=status.HTTP_400_BAD_REQUEST, message = {'message': 'Bad request message'})
    
    
class UserList(generics.ListCreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    
    
class BlogDetailAPIView(APIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST',])
# def blog_list_create(request):
#     if request.method == 'GET':
#         blog = Blog.objects.all()
#         serializer = BlogSerializer(blog, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response (status=status.HTTP_400_BAD_REQUEST, message = {'message': 'Bad request message'})


# @api_view(['GET','PUT','DELETE'])
# def blog_detail(request,pk):
#     try:
#         blog = Blog.objects.get(pk=pk)
#     except Blog.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    