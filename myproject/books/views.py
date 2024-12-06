from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    query = request.GET.get('query')
    
    if query:
        books = Books.objects.filter(title__icontains=query) or Books.objects.filter(author__icontains=query) or Books.objects.filter(genre__icontains=query)
    else:
       books=Books.objects.all()
    paginator=Paginator(books,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request, 'bookpage.html', {'page': 'Home', 'books':page_obj, 'query': query})

def deletebook(request,book_id):
   if request.method=='GET': 
    queryset=Books.objects.get(book_id=book_id)
    queryset.delete()
    return redirect('home')

def addbook(request):
    context={'page':'ShelfIn'}
    if request.method=='POST':
        title=request.POST.get('title')
        genre=request.POST.get('genre')
        isbn=request.POST.get('isbn')
        author = request.POST.get('author')
        price = request.POST.get('price')
        quantity=request.POST.get('quantity')
        Books.objects.create(title=title, author=author, price=price, genre=genre, quantity=quantity, isbn=isbn)
        return redirect('home')
    return render(request, 'add_book.html',context)

def updatebook(request, book_id):
    book = get_object_or_404(Books, book_id=book_id)
    context={'page':'ShelfUpdate','book': book}
    if request.method == 'POST':
        title=request.POST.get('title')
        genre=request.POST.get('genre')
        isbn=request.POST.get('isbn')
        author = request.POST.get('author')
        price = request.POST.get('price')
        quantity=request.POST.get('quantity')
        book.title = title
        book.author = author
        book.genre=genre
        book.isbn=isbn
        book.quantity=quantity
        book.price = price
        book.save()
        return redirect('home')
    return render(request, 'updatebook.html', context)


def salespage(request):
    sales = Sales.objects.select_related('book')
    context={'page':'$ales', 'sales':sales}
    return render(request,'salespage.html',context)

def deletesale(request,sale_id):
   if request.method=='GET': 
    queryset=Sales.objects.get(sale_id=sale_id)
    queryset.delete()
    return redirect('salespage')
   
def updatesale(request, sale_id):
    sale = get_object_or_404(Sales, sale_id=sale_id)

    context={'page':'Update','sale': sale}
    if request.method == 'POST':
        title=request.POST.get('title')
        sold=request.POST.get('sold')
        quantity_sold=request.POST.get('quantity_sold')
        sale.book.title = title
        sale.sold=sold
        sale.quantity_sold=quantity_sold
        sale.save()
        return redirect('salespage')
    return render(request, 'updatesale.html',context)


def addsale(request, book_id):
    book = Books.objects.get(pk=book_id)
    if request.method == 'POST':
        quantity_sold = request.POST.get('quantity_sold')
        sold = request.POST.get('sold')
        Sales.objects.create(book=book, quantity_sold=quantity_sold, sold=sold)
        return redirect('salespage')  
    return render(request, 'add_sale.html', {'book': book})