from django.shortcuts import render,redirect
from .models import Book,Review
from .forms import BookForm,ReviewFom

# Create your views here.
# create crud opertion   by function based view     to book model  
'''
  1- list   detail    create  update   delete
'''
def list_book(request):
    books=Book.objects.all()
    context={'book_list':books}
    return render(request,'books/book_list.html',context)

def detail_book(request,pk):

    book=Book.objects.get(id=pk)
    review=Review.objects.filter(book=book)
    if request.method=='POST':
        form=ReviewFom(request.POST)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.book=book
            my_form.save()
    else:
        form=ReviewFom()

    context={
        'book':book,
        'review':review,
        'form':form
             }
    return render(request,"books/book_detail.html",context)

def create_book(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/books/')
    else:



        form=BookForm()
    context={'form':form}
    return render(request,'books/create.html',context)
def update_book(request,pk):
    book=Book.objects.get(id=pk)
    if request.method=='POST':
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
         form=BookForm(instance=book)
    context={'form':form}
    return render(request,'books/update.html',context)
def delete_book(request,pk):
    book=Book.objects.get(id=pk)
    book.delete()
    return redirect('/books/')


