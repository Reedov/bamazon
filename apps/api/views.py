from apps.book.models import Book, Author
from django.shortcuts import get_object_or_404

from .serializers import BookSerializer,AuthorSerializer

from rest_framework import viewsets
from rest_framework.response import Response


class BookViewSet(viewsets.ViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    

class AuthorViewSet(viewsets.ViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)







book_list = BookViewSet.as_view({'get': 'list'})
book_detail = BookViewSet.as_view({'get': 'retrieve'})
author_list = AuthorViewSet.as_view({'get': 'list'})
author_detail = AuthorViewSet.as_view({'get': 'retrieve'})




