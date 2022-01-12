from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name + " " + self.last_name


class BookCategory(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    pages = models.IntegerField()
    publication_date = models.DateField()

    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    cover_image = models.ImageField(upload_to='book_cover', null=True)
    cover_thumbnail = ImageSpecField(source='cover_image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})

    cover_thumbnail_big = ImageSpecField(source='cover_image',
                                      processors=[ResizeToFill(500, 300)],
                                      format='JPEG',
                                      options={'quality': 60})

    def __str__(self):
        return self.title


class BookOrder(models.Model):
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    message = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
