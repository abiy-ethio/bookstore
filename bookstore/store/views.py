from django.shortcuts import render
from .models import Book, Review
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string
import string, random
from forms import ReviewForm





def index(request):
    return render(request, 'template.html')


def store(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }

    return render(request, 'base.html', context)


def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        'book': book,
    }
    if request.user.is_authenticated():
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = Review.objects.create (
                    user= request.user,
                    book= context['book'],
                    text=form.cleaned_data.get('text')
                )
                new_review.save()
        else:
            if Review.objects.filter(user=request.user, book=context['book']).count()==0:
                form = ReviewForm()
                context['form']= form
    context['reviews']= book.review_set.all()
    return render(request, 'store/detail.html', context)