from book_app.models import BookCategory


def book_app_context_processors(request):

    context = dict()
    context['categories'] = BookCategory.objects.all()

    return context




