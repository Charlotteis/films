from django.shortcuts import render
from films.models import Film


def index(request):
    films = Film.objects.all().order_by('rating').reverse()
    return render(request, 'index.html', {
        'films': films,
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
