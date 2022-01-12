from django.urls import path
from . import views


app_name = "book_app"

urlpatterns = [
    path('category/<int:category_pk>/', views.book_category_view, name='category'),
    path('search/', views.search_books_view, name='search'),

    path('book/<int:pk>/order-success/', views.BookOrderSuccessView.as_view(), name='book_order_success'),
    path('book/<int:pk>/', views.BookDetailOrderCreateView.as_view(), name='book_detail'),

    path('', views.HomeView.as_view(), name='home_page'),
]

