"""
from rest_framework.views import APIView #Generar vista de la API (get, post, put y del)
from rest_framework.response import Response # Devolución de la ApiView
from rest_framework import status #Estado de respuesta
from posts.models import Posts
from posts.serializers.serializer import PostSeralizer

class PostApiView(APIView):
    def get(self, request):
        all_posts = PostSeralizer(Posts.objects.all(), many=True) #Devuelve array de datos

        return Response(status=status.HTTP_200_OK, data=all_posts.data)
    
    def post(self, request):
        new_post = PostSeralizer(data=request.POST) #Castea los datos
        new_post.is_valid(raise_exception=True) # Valida los datos
        new_post.save()
        return Response(status=status.HTTP_200_OK, data=new_post.data)
"""

from rest_framework.viewsets import ViewSet #Generar vista de la API (get, post, put y del)
from rest_framework.response import Response # Devolución de la ApiView
from rest_framework import status #Estado de respuesta
from posts.models import Posts
from posts.serializers.serializer import PostSeralizer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class PostViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly] #Permisos del endpoint
    def list(self, request):
        all_posts = PostSeralizer(Posts.objects.all(), many=True) #Devuelve array de datos

        return Response(status=status.HTTP_200_OK, data=all_posts.data)
    
    def retrieve(self, request, pk:int):
        #Solo obtiene un elemento
        post = PostSeralizer(Posts.objects.get(pk=pk))
        return Response(status= status.HTTP_200_OK, data=post.data)
        
    
    def create(self, request):
        new_post = PostSeralizer(data=request.POST) #Castea los datos
        new_post.is_valid(raise_exception=True) # Valida los datos
        new_post.save()
        return Response(status=status.HTTP_200_OK, data=new_post.data)

        
