from django.shortcuts import render


# Create your views here.


def contact(request):
    context = dict()

    return render(request, 'contact/contact.html', context)
