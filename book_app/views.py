from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.base import TemplateView

from django.db.models import Q

# Create your views here.
from book_app.forms import BookOrderForm
from book_app.models import Book, BookCategory, BookOrder


class HomeView(TemplateView):
    template_name = 'book_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_books'] = Book.objects.all()[:5]
        return context


# class BookCategoryView(ListView):
#     model = Book
#     # paginate_by = 5
#

def book_category_view(request, category_pk):
    context = dict()

    context['category'] = get_object_or_404(BookCategory, id=category_pk)
    context['books'] = Book.objects.filter(category_id=category_pk)

    return render(request, 'book_app/category.html', context)


def search_books_view(request):

    category_pk = request.GET.get("category", None)
    keywords = request.GET.get("keywords", None)

    context = dict()

    # title__icontains = BOOK ::: book, book1, "This is a book"
    # title = book ::: book

    context['books'] = Book.objects.filter(
        Q(category_id=category_pk) |
        Q(title__icontains=keywords) |
        Q(description__icontains=keywords)
    )

    return render(request, 'book_app/search.html', context)


class BookDetailOrderCreateView(CreateView):
    model = BookOrder
    template_name = 'book_app/book_detail.html'
    form_class = BookOrderForm

    def get_success_url(self):
        return reverse('book_app:book_order_success', kwargs={'pk': self.kwargs['pk'] })

    def form_valid(self, form):
        book = get_object_or_404(Book, id=self.kwargs['pk'])
        form.instance.book = book
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = get_object_or_404(Book, id=self.kwargs['pk'])
        return context


class BookOrderSuccessView(DetailView):
    model = Book
    template_name = 'book_app/book_order_success.html'
