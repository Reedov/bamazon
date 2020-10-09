from django.shortcuts import render,get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from apps.book.models import Author,Book

from django.core.paginator import Paginator,PageNotAnInteger

def book_detail_view(request,book):
    book = get_object_or_404(Book, id=book)


    return render(request, 'book/book_detail.html', {'book':book})

def book_list_view(request):
    all_books = Book.objects.all().order_by('-name')

    paginator = Paginator(all_books, 2)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)

    return render(request, 'book/book_list.html', {'books':books})



def author_detail_view(request,author):
    book_author = get_object_or_404(Author, id=author)
    books = Book.objects.filter(author = book_author)

    return render(request, 'book/author_detail.html', {'author':author,'books':books})