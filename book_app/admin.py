from django.contrib import admin

from .models import (
    BookCategory,
    Book,
    Author,
    BookOrder
)

# Register your models here.


admin.site.register(Author)
admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(BookOrder)
